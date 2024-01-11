import cors from "cors";
import express, { Request, Response, type Application } from "express";

const app = express();
// cors para que el cliente pueda hacer peticiones
app.use(cors());

app.get("/", (req: Request, res: Response): Response => {
  return res.json({
    message: "hola mundo",
  });
});

export default app;
