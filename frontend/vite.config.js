import { fileURLToPath, URL } from 'node:url' // 用于处理文件URL
import path from 'path' // 用于处理文件路径

import { defineConfig } from 'vite' // Vite配置函数
import vue from '@vitejs/plugin-vue' // Vue插件，用于处理.vue文件
import vueDevTools from 'vite-plugin-vue-devtools' // Vue DevTools插件，用于开发调试

// https://vite.dev/config/
export default defineConfig({
  // 插件配置
  plugins: [
    vue(), // 启用Vue插件
    vueDevTools(), // 启用Vue DevTools插件
  ],
  
  // 路径解析配置
  resolve: {
    // 路径别名配置
    alias: {
      // 将@符号映射到src目录，简化导入路径
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  
  // 构建配置
  build: {
    // 打包输出目录，直接输出到Django的static目录
    // 这样Django可以直接 serve 前端打包文件
    outDir: path.resolve(__dirname, '../backend/static/frontend'),
    
    // 打包前清空输出目录
    emptyOutDir: true,
  },
})
