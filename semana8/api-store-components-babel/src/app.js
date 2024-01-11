import cors from "cors";
import express from "express";
import { productRouter, userRouter } from "./components";
import { apiVersion } from "./config";

export const app = express();

app.use(cors());
app.use(express.json());

app.use(`${apiVersion}/users`, userRouter);
app.use(`${apiVersion}/products`, productRouter);
