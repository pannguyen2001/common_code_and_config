import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
import tseslint from 'typescript-eslint'
import { defineConfig, globalIgnores } from 'eslint/config'

export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      js.configs.recommended,
      tseslint.configs.recommended,
      reactHooks.configs['recommended-latest'],
      reactRefresh.configs.vite,
    ],
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
    },
    settings: {
      'import/resolver': {
        alias: {
          map: [
            ['@assets', './src/assets'],
            ['@components', './src/components'],
            ['@configs', './src/configs'],
            ['@data', './src/data'],
            ['@helpers', './src/helpers'],
            ['@pages', './src/pages'],
            ['@routes', './src/routes'],
            ['@utils', './src/utils'],
          ],
          extensions: ['.ts', '.tsx', '.js', '.jsx', '.json']
        }
      }
    }
  },
])
