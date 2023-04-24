// Author: Somiona Tian (17ht13@queensu.ca)

import { RawAxiosRequestHeaders } from "axios";

const appConfig = {
  site_name: "EA Stock Simulator",
  title: "EA Stock Simulator",
  description:
    "CISC 455 Final Project - Emotional Damage Stock Simulator an Evolutionary Algorithm Approach By Team 26",
  locale: "en",
  authors: ["E Ching Kho", "Somiona Tian", "Wenqi Tang"],
};

interface IAPIBase {
  url: string;
  headers: RawAxiosRequestHeaders;
}

const serverConfig: Record<string, IAPIBase> = {
  devAPI: {
    url: "http://localhost:8000",
    headers: {},
  },
  prodAPI: {
    url: "https://example.com/api",
    headers: {},
  },
};

export { serverConfig, appConfig };
export type { IAPIBase };
