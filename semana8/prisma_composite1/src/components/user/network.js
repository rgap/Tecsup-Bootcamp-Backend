import { Router } from "express";
import * as Controller from "./controller.js";

const userRouter = Router();

// READ
userRouter.route("/").get(Controller.list);
// CREATE
userRouter.route("/").post(Controller.store);
// UPDATE
userRouter.route("/:userId/:email").put(Controller.update);
// DELETE
userRouter.route("/:userId/:email").delete(Controller.destroy);

///////////

// READ BY ID
userRouter.route("/:userId/:email").get(Controller.getByCompositeKey);

export default userRouter;
