module.exports = {
  "*.{js,jsx,ts,tsx,mdx}": ["prettier --write", "eslint"],
  "**/*.ts?(x)": () => "tsc --noEmit --pretty",
  "*.json": ["prettier --write"],
  "*.{css,scss,sass}": ["prettier --write"],
};
