// Author: Somiona Tian (17ht13@queensu.ca)
import { createRequestClient } from "apis/requests";
import { APISchema } from "apis/type";

export type NullableStr = void | string;

interface ExampleAPISchema extends APISchema {
  foo: {
    request: void;
    response: void;
  };
}

const ExampleAPI = createRequestClient<ExampleAPISchema>({
  baseURL: "https://www.baidu.com",
  apis: {
    foo: "GET server/path/to/foo",
  },
  headers: {
    "Content-Type": "application/json",
  },
});

export default ExampleAPI;
