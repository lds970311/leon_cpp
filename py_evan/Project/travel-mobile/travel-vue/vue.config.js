const {defineConfig} = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    lintOnSave: false,

    devServer: {
        proxy: {
            '/api': {
                // target: 'http://localhost:8000',
                target: 'http://localhost:18081',
                changeOrigin: true,
                pathRewrite: {
                    '^/api': ''   //需要rewrite重写的URL
                }
            }
        }
    }
})
