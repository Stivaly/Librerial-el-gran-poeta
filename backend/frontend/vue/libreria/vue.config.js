const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  devServer: {
    proxy: {
        '/api': {
          target: 'http://127.0.0.1:8000/', // Cambia esto a tu backend Django si lo necesitas
          changeOrigin: true
        }
      },
  }
});
