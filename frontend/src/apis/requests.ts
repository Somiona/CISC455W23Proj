// Author: Somiona Tian (17ht13@queensu.ca)
import axios, { AxiosInstance, AxiosError, AxiosHeaders, AxiosRequestHeaders } from "axios";
// import { cond, always, forEachObjIndexed, startsWith, defaultTo, either, isNil } from "ramda";
import { forEachObjIndexed, defaultTo } from "ramda";
import {
  APISchema,
  CreateRequestConfig,
  CreateRequestClient,
  RequestPath,
  APIConfig,
} from "./type";
import { serverConfig } from "utils/config";

const MATCH_METHOD = /^(GET|POST|PUT|DELETE|HEAD|OPTIONS|CONNECT|TRACE|PATCH)\s+/;
const MATCH_PATH_PARAMS = /:(\w+)/g;
const USE_DATA_METHODS = ["POST", "PUT", "PATCH", "DELETE"];

/** 在这里设置默认服务器路径和 Headers */
// const defaultAPIBase = cond([
//   [either(startsWith("dev"), isNil), always(serverConfig.devAPI)],
//   [startsWith("prod"), always(serverConfig.prodAPI)],
// ])(process.env.NODE_ENV);
const defaultAPIBase = serverConfig.devAPI;

function attachAPI<T extends APISchema>(
  client: AxiosInstance,
  apis: CreateRequestConfig<T>["apis"]
): CreateRequestClient<T> {
  const hostApi = Object.create(null) as CreateRequestClient<T>;

  forEachObjIndexed((config: APIConfig, entry) => {
    // 配置为一个函数
    if (typeof config === "function") {
      hostApi[entry] = config;
      return;
    }
    let apiOptions = {};
    let apiPath = config as RequestPath;
    // 配置为一个对象
    if (typeof config === "object") {
      const { path, ...rest } = config;
      apiPath = path as RequestPath;
      apiOptions = rest;
    }

    hostApi[entry] = (p, options) => {
      const params = { ...(p || {}) };
      // 匹配路径中请求方法，如：'POST /api/test'
      let [prefix, method] = apiPath.match(MATCH_METHOD) || ["GET ", "GET"];
      if (!prefix || !method) {
        [prefix, method] = ["GET ", "GET"];
      }
      // 剔除掉前缀
      let url = apiPath.replace(prefix, "");
      // 匹配路径中的参数占位符， 如 '/api/:user_id/:res_id'
      const matchParams = apiPath.match(MATCH_PATH_PARAMS);
      if (matchParams) {
        matchParams.forEach((match) => {
          const key = match.replace(":", "");
          if (Reflect.has(params, key)) {
            url = url.replace(match, Reflect.get(params, key) as string);
            Reflect.deleteProperty(params, key);
          }
        });
      }
      const requestParams = USE_DATA_METHODS.includes(method) ? { data: params } : { params };

      // eslint-disable-next-line @typescript-eslint/no-unsafe-argument
      return client.request({
        url,
        method: method.toLowerCase(),
        withCredentials: true,
        xsrfCookieName: "csrftoken",
        xsrfHeaderName: "X-CSRFToken",
        ...requestParams,
        ...apiOptions,
        ...options,
      });
    };
  }, apis);
  return hostApi;
}

// 创建请求客户端
function createRequestClient<T extends APISchema>(
  requestConfig: CreateRequestConfig<T>
): CreateRequestClient<T> {
  const client = axios.create({
    baseURL: defaultTo(defaultAPIBase?.url)(requestConfig.baseURL),
    headers: { ...defaultAPIBase?.headers, ...requestConfig?.headers },
  });

  // 附加各业务请求头
  client.interceptors.request.use(async (config) => {
    const headerHandlers = (requestConfig.headerHandlers || []).map(async (handler) => {
      return handler(config)
        .then((mixHeaders: AxiosRequestHeaders) => {
          if (!config.headers) {
            config.headers = new AxiosHeaders();
          }
          Object.assign(config.headers, mixHeaders);
        })
        .catch();
    });
    return Promise.all(headerHandlers).then(() => config);
  });

  // 拦截请求
  client.interceptors.response.use(
    (res) => res,
    (error: AxiosError) => {
      const requestError = requestConfig.errorHandler ? requestConfig.errorHandler(error) : error;
      return Promise.reject(requestError);
    }
  );

  return attachAPI<T>(client, requestConfig.apis);
}

export { createRequestClient, defaultAPIBase };
