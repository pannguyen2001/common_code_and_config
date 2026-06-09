import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";
import tsconfigPaths from "vite-tsconfig-paths";

export default defineConfig({
  plugins: [react(), tsconfigPaths()],
  resolve: {
    alias: {
      "@/apis": path.resolve(__dirname, "src/apis"),
      "@/assets": path.resolve(__dirname, "src/assets"),
      "@/components": path.resolve(__dirname, "src/components"),
      "@/configs": path.resolve(__dirname, "src/configs"),
      "@/data": path.resolve(__dirname, "src/data"),
      "@/helpers": path.resolve(__dirname, "src/helpers"),
      "@/hooks": path.resolve(__dirname, "src/hooks"),
      "@/layouts": path.resolve(__dirname, "src/layouts"),
      "@/pages": path.resolve(__dirname, "src/pages"),
      "@/routes": path.resolve(__dirname, "src/routes"),
      "@/services": path.resolve(__dirname, "src/services"),
      "@/tests": path.resolve(__dirname, "src/tests"),
      "@/utils": path.resolve(__dirname, "src/utils"),
      "@/zustand": path.resolve(__dirname, "src/zustand"),
    },
  },
});
