// Author: Somiona Tian (17ht13@queensu.ca)
import { createRequestClient } from "apis/requests";
import { APISchema } from "apis/type";

export type NullableStr = void | string;

interface TestAPI extends APISchema {
  test: {
    request: void;
    response: void;
  };
}

const TestAPI = createRequestClient<TestAPI>({
  apis: {
    test: "GET test",
  },
});

export default TestAPI;
