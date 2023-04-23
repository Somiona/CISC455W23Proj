import { RawAxiosRequestHeaders } from "axios";

const appConfig = {
  site_name: "Stock Simulator",
  title: "Emotional Damage Stock Simulator",
  description: "CISC 455 Final Project - Emotional Damage Stock Simulator",
  locale: "en",
  authors: [
    "E Ching Kho",
    "Somiona Tian",
    "Peter"
  ]
}

interface IAPIBase {
  url: string;
  headers: RawAxiosRequestHeaders;
}

const serverConfig: Record<string, IAPIBase> = {
  devAPI: {
    url: "http://api.unifurse.cn:8000",
    // url: "http://localhost:8000",
    // url: "http://127.0.0.1:4523/mock/868521-0-default",
    headers: {},
  },
  prodAPI: {
    url: "https://api.unifurse.cn",
    headers: {},
  },
};

export { serverConfig, appConfig };
export type { IAPIBase };
