import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Vite config: enable the official React plugin so JSX in .js files is handled
export default defineConfig({
  plugins: [react()],
})
