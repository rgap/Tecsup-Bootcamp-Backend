import cors from "cors";
import "dotenv/config";
import express, { type Application } from "express";
import fileUpload from "express-fileupload";
import { productRouter, toolsRouter, userRouter } from "./components";

const app: Application = express();

// cors para que el cliente pueda hacer peticiones
app.use(cors());
app.use(fileUpload());
app.use(express.json());

// console.log(process.env.DATABASE_URL);

app.use("/api/v1/users", userRouter);
app.use("/api/v1/products", productRouter);
app.use("/api/v1/tools", toolsRouter);

export default app;
