# Install and config Playwright TS

Source:
- https://playwright.dev/docs/intro
- https://autify.com/blog/playwright-tutorial
- https://github.com/pannguyen2001/playwright_ts_learn
- https://anhtester.com/lesson/playwright-typescript-bai-21-ky-thuat-debug-loi-voi-trace-viewer-va-cau-hinh-reporting-tu-co-ban-html-den-nang-cao-allure-custom
- https://allurereport.org/docs/playwright/

## 1. Install npm

## 2. Install pnpm
```
# Command prompt
npm i -g pnpm
```

## 3. Install playwright
```
pnpm create playwright
```

## 4. Install TypeScript
```
pnpm i -D typescript
```

## 5. Install ts-node
```
pnpm i -D ts-node
```

## 6. Run test
```
npx playwright test
or:
pnpm exec playwright test
with UI mode:
pnpm exec playwright test --ui
```

## 7. View Report
```
npx playwright show-report
or:
pnpm exec playwright show-report
```

## 9. Install allure report for Playwright
- Note that allure reports need java jdk and allure cli. Please install java jsk by openjdk first
- Download openjdk and set env:
https://jdk.java.net/archive/ (archived version, not used, but if you want, can install)
Newest version: https://jdk.java.net/26/ (Accessed date: 2026-05-18)
```
JAVA_HOME : C:\Users\ASUS\Downloads\openjdk-25.0.1_windows-x64_bin\jdk-25.0.1
JAVA: C:\Users\ASUS\Downloads\openjdk-25.0.1_windows-x64_bin\jdk-25.0.1\bin
```
- Open cmd and check:
```
echo %JAVA_HOME%
java -version
```
- Source: https://stackoverflow.com/questions/26434791/generating-allure-report-using-pytest
- Install allure playwright:
```
pnpm install -D allure-playwright
pnpm install -D allure
```

## 8. Generate Allure report
```
allure generate ./allure-results -o ./allure-report
or (if using npm):
npx allure generate allure-results --clean -o allure-report
or:
allure generate allure-results --clean -o allure-report

Open report:
allure open ./allure-report
```