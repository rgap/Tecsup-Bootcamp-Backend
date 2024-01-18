import { Router } from "express";
import { storeFile } from "./controller";

const toolsRouter = Router();

toolsRouter.route("/upload").post(storeFile);

export default toolsRouter;
