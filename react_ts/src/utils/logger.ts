// Allowed log levels
// const LOG_LEVELS = ['debug', 'info', 'warning', 'error', 'critical', 'table'];

export const messageStyle = {
  debug: "background-color: #bde3ff; color: #344bc1",
  info: "background-color: #bdfac5; color: #005c22",
  warning: "background-color: #fff687; color: #b86705",
  error: "background-color: #fececa; color: #ba261b",
  critical: "background-color: #f97970; color: rgb(58, 13, 10)",
  table: "background-color: #202124; color: #fafbfb",
  dark: "background-color: #202124; color: #fafbfb",
  light: "background-color: #fafbfb; color: #202124",
  commonStyle:
    "border-radius: 4px;padding:4px;display:flex;justify-content:center;align-items:center;margin:4px 0px;font-weight:600;",
  reset: "font-weight:600; margin-left:10px",
};

export const textStyle = {
  debug: "color: #3499fd;",
  info: "color: #00c04c;",
  warning: "color:rgb(225, 171, 6);",
  error: "color: #F04A3E;",
  critical: "color:rgb(166, 38, 28);",
  table: "color:rgb(36, 127, 218);",
  dark: "color: #202124;",
  light: "color: #fafbfb;",
};

/**
 * Logger class for logging messages to the console.
 * @class Logger
 */

export class Logger {
  #name;
  #logLevel;
  #isDebug;

  constructor(name = "", level = "debug", isDebug = true) {
    this.#name = name;
    this.#logLevel = level;
    this.#isDebug = isDebug;
  }

  get name() {
    return this.#name;
  }

  get logLevel() {
    return this.#logLevel;
  }

  get isDebug() {
    return this.#isDebug;
  }

  set name(name) {
    this.#name = name;
  }

  set logLevel(level) {
    this.#logLevel = level;
  }

  set isDebug(isDebug) {
    this.#isDebug = isDebug;
  }

  getCallerFile() {
    const stack = new Error().stack;
    if (!stack) return "Unknown";

    const lines = stack.split("\n").map((l) => l.trim());

    // Find first stack line that is NOT logger.js
    const caller = lines.find(
      (line) => !line.includes("logger.js") && line.includes("/src/"),
    );
    if (!caller) return "Unknown";

    // Extract relative path from /src/ onwards
    const match = caller.match(/\/src\/(.+\.[tj]sx?)/);
    return match ? match[1] : "Unknown";
  }

  log(level, message) {
    if (!this.#isDebug) {
      console.log(message);
      return;
    }

    this.#name = this.getCallerFile();

    let msg = message;

    if (level === "error" && message instanceof Error) {
      msg = message.stack;
    }

    if (level === "table" && typeof message === "object") {
      console.table(message);
    } else {
      console.log(
        `%c${level.toUpperCase()}%c ${this.#name} %c${msg}`,
        messageStyle.commonStyle + messageStyle[level],
        messageStyle.commonStyle,
        messageStyle.commonStyle + textStyle[level],
      );
    }
  }

  debug(message) {
    this.log("debug", message);
  }

  info(message) {
    this.log("info", message);
  }

  warning(message) {
    this.log("warning", message);
  }

  error(message) {
    this.log("error", message);
  }

  critical(message) {
    this.log("critical", message);
  }

  table(message) {
    this.log("table", message);
  }
}

const logger = new Logger("Learn react core", "debug");

export default logger;
