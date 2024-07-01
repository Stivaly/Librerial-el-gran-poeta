const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/api': {
        // target: 'http://10.1.0.4:5000',
        target: 'http://127.0.0.1:8000/',
        changeOrigin: true,
      },
    },
  }
})
