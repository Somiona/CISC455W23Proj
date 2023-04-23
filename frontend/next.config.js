/* eslint-disable @typescript-eslint/no-unsafe-call */
/* eslint-disable @typescript-eslint/no-var-requires */
/* eslint-disable @typescript-eslint/no-unsafe-assignment */
const bundleAnalyzer = require("@next/bundle-analyzer");

const withBundleAnalyzer = bundleAnalyzer({
  enabled: process.env.ANALYZE === "true",
});

/**
 * @type {import('next').NextConfig}
 */
module.exports = withBundleAnalyzer({
  /* config options here */
  images: {
    formats: ["image/avif", "image/webp"],
    // domains: [],
  },
  swcMinify: true,
  poweredByHeader: false,
  basePath: "",
  // The starter code load resources from `public` folder with `router.basePath` in React components.
  // So, the source code is "basePath-ready".
  // You can remove `basePath` if you don't need it.
  reactStrictMode: true,
  compiler: {
    styledComponents: false,
    emotion: false,
  },
  experimental: {
    // appDir: true,
  },
  output: "standalone",
});
