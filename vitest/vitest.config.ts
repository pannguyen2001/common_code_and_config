import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import * as path from 'path' // Import the path module: npm install --save-dev @types/node

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@/assets': path.resolve(__dirname, 'src/assets'),
      '@/components': path.resolve(__dirname, 'src/components'),
      '@/configs': path.resolve(__dirname, 'src/configs'),
      '@/data': path.resolve(__dirname, 'src/data'),
      '@/helpers': path.resolve(__dirname, 'src/helpers'),
      '@/zustand': path.resolve(__dirname, 'src/zustand'),
      '@/pages': path.resolve(__dirname, 'src/pages'),
      '@/routes': path.resolve(__dirname, 'src/routes'),
      '@/utils': path.resolve(__dirname, 'src/utils'),
    },
  },
})
