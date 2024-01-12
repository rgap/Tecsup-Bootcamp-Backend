import cors from "cors";
import express, { type Application } from "express";
import { userRouter } from "./components";

export const app = express();
// cors para que el cliente pueda hacer peticiones

app.use(cors());
app.use(express.json());

app.use("/api/v1/users", userRouter);

export default app;
