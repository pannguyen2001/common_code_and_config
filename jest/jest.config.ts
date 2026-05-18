import type { Config } from 'jest';
import { pathsToModuleNameMapper, JestConfigWithTsJest } from "ts-jest";
import { compilerOptions } from "./tsconfig.json";
import * as path from "path";


const config: Config = {
  preset: 'ts-jest',
  moduleDirectories: ["node_modules", "<rootDir>"],
  moduleNameMapper: {
    ...pathsToModuleNameMapper(compilerOptions.paths, { prefix: '<rootDir>/src/' }),
    // "^@/configs/(.*)$": path.resolve(__dirname, "./src/configs/$1"),
    // "^@/constants/(.*)$": path.resolve(__dirname, "./src/constants/$1"),
    // "^@/utils/(.*)$": path.resolve(__dirname, "./src/utils/$1"),
  },
  testTimeout: 30000, // 30s - db connection or some func can be slow, need wait
  setupFilesAfterEnv: ['<rootDir>/tests/setupTests.ts'],
  moduleFileExtensions: ['ts', 'tsx', 'js', 'jsx', 'json', 'node'],
  modulePaths: ['<rootDir>'],
  testEnvironment: 'node',
  transform: {
    '^.+\\.(ts|tsx)$': ['ts-jest', {
      tsconfig: 'tsconfig.test.json',
      // useESM: true
    }],
    '^.+\\.(js|jsx|mjs)$': 'babel-jest',
  },
  testMatch: ['<rootDir>/tests/**/*.test.(ts|tsx)'],
  // allow Jest to transform these ESM-only packages instead of ignoring them
  transformIgnorePatterns: [
    // 'node_modules/(?!(bson|mongodb|mongoose|@faker-js/faker)/)'
    'node_modules/(?!(\\@faker-js/faker)/)'
  ],
  // extensionsToTreatAsEsm: ['.ts'],
};

export default config;