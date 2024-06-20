const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/api': {
        target: 'https://el-gran-poeta-login-1515.azurewebsites.net',
        changeOrigin: true,
        pathRewrite: { '^/api': '' }, // Esto elimina el prefijo '/api' de la ruta
      },
    },
  }
})
