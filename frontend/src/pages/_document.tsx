import { Html, Head, Main, NextScript } from "next/document";
import { appConfig } from "utils/config";

export default function Document() {
  return (
    <Html lang={appConfig.locale}>
      <Head />
      <body className="antialiased">
        <Main />
        <NextScript />
      </body>
    </Html>
  );
}
