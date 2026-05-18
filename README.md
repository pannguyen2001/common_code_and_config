# Store common code and config for all projects and languages I learnt
This is root config for all projects. If have any update, please update in both project and this branch.

## JS/TS
Source:
- https://github.com/pannguyen2001/learn-ts
- https://github.com/pannguyen2001/capstone_prj_sqlite (work for common ts config and jest config)

### 1. Common config tsconfig.json
1. Install typescript
```
npm install -D typescript
```
2. Install ts-node
```
npm install -D ts-node
```
3. Install @types/node
```
npm install -D @types/node
```

### 2. Common config tsconfig.json


## ReactJS/ ReactTS

## Jest
Source: https://github.com/pannguyen2001/capstone_prj_sqlite
### 1. Common config Jest.config.json, tsconfig.test.json
1. Install pnpm globaly
```
npm install -g pnpm
```
2. Install jest
```
pnpm add -D jest ts-jest @types/jest
```


## Vitest
Source:
- https://github.com/pannguyen2001/react-ts-common

### 1. Common config Vitest.config.json, tsconfig.test.json

## Python
### 1. Install and setup .venv using uv, pyproject.toml or poetry

## Pytest
### 1. Install and setup pytest and allure report

## Playwright ts
Source: https://github.com/pannguyen2001/playwright_ts_learn
### 1. Install and setup playwright typescript
1. Install npm
2. Install pnpm
3. Install playwright
```
pnpm add -D playwright
```
4. Install typescript
```
pnpm add -D typescript
```
5. Install ts-node
```
pnpm add -D ts-node
```
6. Install @types/node
```
pnpm add -D @types/node
```
### 2. Install allure report

### 3. Run test
```
npx playwright test
```

### 4. Generate report
```
allure generate ./allure-results -o ./allure-report

allure open ./allure-report
```

Source learning:

[][][] https://anhtester.com/lesson/playwright-typescript-bai-21-ky-thuat-debug-loi-voi-trace-viewer-va-cau-hinh-reporting-tu-co-ban-html-den-nang-cao-allure-custom


## Playwright python
### 1. Install and setup playwright python

## Selenium
### 1. Install and setup selenium

## Cypress
### 1. Install and setup cypress

## Docker

## CI/CD: Github action


## Which need to be created and updated
- folder structure
- common logger: stdout, file, logstash, log file, serialize log,...
- common report
- common function
- common config: constant, .env, datetime format, folder creation and deletion, etc
- app connection, db connection
- emal, slack/discord connection