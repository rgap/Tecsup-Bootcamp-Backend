import "@testing-library/jest-dom/vitest";
import { cleanup } from "@testing-library/react";
import { afterEach } from "vitest";

// se va a ejecutar despues de cada test
afterEach(() => {
  cleanup();
});
