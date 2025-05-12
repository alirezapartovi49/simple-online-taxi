const path = require("path");
const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    compress: false,
  },
  configureWebpack: {
    resolve: {
      alias: {
        "@": path.resolve(__dirname, "src"),
        "@stores": path.resolve(__dirname, "src/stores"),
        "@views": path.resolve(__dirname, "src/views"),
        "@router": path.resolve(__dirname, "src/router"),
        "@client": path.resolve(__dirname, "src/client"),
      },
      extensions: [
        ".mjs",
        ".js",
        ".jsx",
        ".ts",
        ".vue",
        ".json",
        ".wasm"
      ],
    },
    module: {
      rules: [
        {
          test: /\.vue$/,
          loader: "vue-loader"
        },
        // JavaScript
        {
          test: /\.js$/,
          loader: "babel-loader",
          exclude: /node_modules/
        },
        {
          test: /\.ts$/,
          loader: "ts-loader",
          exclude: /node_modules/,
          options: {
            appendTsSuffixTo: [/\.vue$/]
          }
        }
      ]
    }
  }
});
