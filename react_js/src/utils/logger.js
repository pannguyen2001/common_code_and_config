type LogLevel = 'debug' | 'info' | 'warning' | 'error' | 'critical' | 'table'

// const LOG_LEVELS: string[] = ['debug', 'info', 'warning', 'error', 'critical', 'table']

export const messageStyle = {
  debug: 'background-color: #bde3ff; color: #344bc1',
  info: 'background-color: #bdfac5; color: #005c22',
  warning: 'background-color: #fff687; color: #b86705',
  error: 'background-color: #fececa; color: #ba261b',
  critical: 'background-color: #f97970; color: rgb(58, 13, 10)',
  table: 'background-color: #202124; color: #fafbfb',
  dark: 'background-color: #202124; color: #fafbfb',
  light: 'background-color: #fafbfb; color: #202124',
  commonStyle:
    'border-radius: 4px;padding:4px;display:flex; justify-content:center;align-items:center;margin:4px 0px;font-weight:600;',
  reset: 'font-weight:600; margin-left:10px',
}

export const textStyle = {
  debug: 'color: #3499fd;',
  // 'background-color: #bde3ff; color: #344bc1',
  // 'color: #3499fd;',
  info: 'color: #00c04c;',
  // 'background-color: #bdfac5; color: #005c22',
  // 'color: #00c04c;',
  warning: 'color:rgb(225, 171, 6);',
  error: 'color: #F04A3E;',
  critical: 'color:rgb(166, 38, 28);',
  table: 'color:rgb(36, 127, 218);',
  dark: 'color: #202124;',
  light: 'color: #fafbfb;',
}

/**
 * Logger class for logging messages to the console.
 * @class Logger
 * @param {string} name - The name of the logger.
 * @param {LogLevel} level - The log level.
 * @returns {void} - No return value.
 */

export class Logger {
  #name: string
  #logLevel: LogLevel
  #isDebug: boolean
  #functionName: string
  #filePath: string

  constructor(
    name: string = '',
    level: LogLevel = 'debug',
    isDebug: boolean = true,
    functionName: string = "<anonymous>"
  ) {
    this.#name = name
    this.#logLevel = level
    this.#isDebug = isDebug
    this.#functionName = functionName
    this.#filePath = ''
  }

  get name(): string {
    return this.#name
  }

  get logLevel(): string {
    return this.#logLevel
  }

  get isDebug(): boolean {
    return this.#isDebug
  }

  get functionName(): string {
    return this.#functionName
  }

  get filePath(): string {
    return this.#filePath
  }

  set name(name: string) {
    this.#name = name
  }

  set logLevel(level: LogLevel) {
    this.#logLevel = level
  }

  set isDebug(isDebug: boolean) {
    this.#isDebug = isDebug
  }

  set functionName(functionName: string) {
    this.#functionName = functionName
  }

  private getCallerFile(): string {
    const stack = new Error().stack
    if (!stack) return 'Unknown'

    const lines = stack.split('\n').map((l) => l.trim())

    // Find first stack line that is NOT logger.ts
    const caller = lines.find(
      (line) => !line.includes('logger.ts') && line.includes('/src/'),
    )
    if (!caller) return 'Unknown'

    // Extract relative path from /src/ onwards
    // const match = caller.match(/\/src\/(.+\.[tj]sx?)/)
    // return match ? match[1] : 'Unknown'
    const match = caller.split("dev")[1].split("?")[0]
    return match ?? "Unknown"
  }

  static getFunctionNameAndLine(stack: string[]): string {
    let functionName: string = "<anonymous>"

    if (stack.length < 3) return functionName

    let temp: string = stack[3]
    if (temp.includes("(")) {
      let tempFunc: string = temp.split("(")[0].trim();
      // if (temp.includes(")")) {
      //   tempFunc = tempFunc.replace(")", "");
      //   let tempLine: string = temp
      //   .split(":")
      //   .slice(-2)
      //   .slice(-2)
      //   .join(":")
      //   .replace(")", "")
      //   return `${tempFunc}:${tempLine}`;
      // }
      return `${tempFunc.replace(")", "").replace("at", "").trim()}`;
    }
    // let tempLine: string = temp
    // .split(":")
    // .slice(-2)[0]
    // .replace(")", "");

    // return `${functionName}:${tempLine}`;
    return `${functionName.replace(")", "")}`;
    }

  private log(level: LogLevel, ...message: any) {
    // const timestamp = new Date().toLocaleString('en-GB', { timeZone: 'Asia/Ho_Chi_Minh' })
    if (!this.#isDebug) {
      console.log(...message)
      return
    }

    this.#filePath = this.getCallerFile()

    let stack = new Error().stack.split('\n');
    this.#functionName = Logger.getFunctionNameAndLine(stack)

    if (level === 'table' && typeof message === 'object') {
      console.table(message)
      return
    }

    let msg = message
    if (level === 'error' && message instanceof Error) {
      msg = message.stack
    }

    console.log(
      `%c ${level.toUpperCase()} %c ${this.#name}  ${this.#filePath}:${this.#functionName} %c ${msg} `,
      messageStyle.commonStyle + messageStyle[level],
      messageStyle.commonStyle,
      messageStyle.commonStyle + textStyle[level],
    )
  }

  // async sendLogToServer(level: string, message: string) {
  //   await fetch('/api/logs', {
  //     method: 'POST',
  //     headers: { 'Content-Type': 'application/json' },
  //     body: JSON.stringify({ level, message, timestamp: new Date().toISOString() }),
  //   })
  // }

  // addLog(level: string, message: string) {
  //   const timestamp = new Date().toLocaleString('en-GB', { timeZone: 'Asia/Ho_Chi_Minh' })
  //   const logFileName = `FE log ${timestamp}.log`
  //   const logs = JSON.parse(localStorage.getItem(logFileName) || '[]')
  //   logs.push(`[${timestamp}][${level}] ${message}`)
  //   localStorage.setItem(logFileName, JSON.stringify(logs))
  // }

  // saveLogToFile(filename: string, content: string) {
  //   const blob = new Blob([content], { type: 'text/plain' })
  //   const url = URL.createObjectURL(blob)
  //   const a = document.createElement('a')
  //   a.href = url
  //   a.download = filename
  //   document.body.appendChild(a)
  //   a.click()
  //   document.body.removeChild(a)
  //   URL.revokeObjectURL(url)
  // }

  debug(...message: any) {
    this.log('debug', ...message)
  }

  info(...message: any) {
    this.log('info', ...message)
  }

  warning(...message: any) {
    this.log('warning', ...message)
  }

  error(...message: any) {
    this.log('error', ...message)
  }

  critical(...message: any) {
    this.log('critical', ...message)
  }

  table(...message: any) {
    this.log('table', ...message)
  }
}

const logger = new Logger('React App', 'debug')

export default logger
