import react from "@vitejs/plugin-react-swc";
import { defineConfig } from "vite";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  // server changes
  server: {
    port: 3000,
    open: true,
  },
  test: {
    // simulated browser
    environment: "jsdom",
    setupFiles: "./src/__test__/setup.js",
    // window variable in the browser
    globals: true,
  },
});
