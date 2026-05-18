module.exports = {
    settings: {
      "import/resolver": {
        typescript: {
          project: "./tsconfig.json"
        },
  
        alias: {
          map: [
            ["@", "./src"],
            ["@configs", "./src/configs"],
            ["@constants", "./src/constants"],
            ["@utils", "./src/utils"]
          ],
  
          extensions: [".ts", ".js", ".jsx", ".json"]
        }
      }
    }
  }