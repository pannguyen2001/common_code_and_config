import js from "@eslint/js";
import globals from "globals";
import reactHooks from "eslint-plugin-react-hooks";
import reactRefresh from "eslint-plugin-react-refresh";
import { defineConfig, globalIgnores } from "eslint/config";

export default defineConfig([
  globalIgnores(["dist"]),
  {
    files: ["**/*.{js,jsx}"],
    extends: [
      js.configs.recommended,
      reactHooks.configs["recommended-latest"],
      reactRefresh.configs.vite,
      "airbnb",
      "airbnb/hooks",
      "plugin:react/recommended",
      "plugin:import/errors",
      "plugin:import/warnings",
    ],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
      parserOptions: {
        ecmaVersion: "latest",
        ecmaFeatures: { jsx: true },
        sourceType: "module",
      },
    },
    rules: {
      "no-unused-vars": ["error", { varsIgnorePattern: "^[A-Z_]" }],
    },
    settings: {
      "import/resolver": {
        alias: {
          map: [
            ["@assets", "./src/assets"],
            ["@components", "./src/components"],
            ["@configs", "./src/configs"],
            ["@data", "./src/data"],
            ["@helpers", "./src/helpers"],
            ["@pages", "./src/pages"],
            ["@routes", "./src/routes"],
            ["@utils", "./src/utils"],
          ],
          extensions: [".js", ".jsx", ".ts", ".tsx", ".json"],
        },
      },
    },
  },
]);
