// Forma moderna
import { PrismaClient } from "@prisma/client";
import express from "express";
import { responseError, responseSuccess } from "./network/responses.js";

export const app = express();
app.use(express.json());

const prisma = new PrismaClient();

// READ

app.get("/", async (req, res) => {
  try {
    const users = await prisma.user.findMany(); // SELECT * FROM users
    return responseSuccess({ res, data: users });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
});

// READ by id

app.get("/:id", async (req, res) => {
  try {
    const user = await prisma.user.findUnique({
      where: {
        id: Number(req.params.id),
      },
    });

    if (!user) {
      return responseError({ res, data: "User not found" });
    }

    return responseSuccess({ res, data: user });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
});

// CREATE

app.post("/", async (req, res) => {
  try {
    await prisma.user.create({
      data: req.body,
    });

    return responseSuccess({ res, data: "User created", status: 201 });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
});

// UPDATE

app.put("/:id", async (req, res) => {
  try {
    const user = await prisma.user.update({
      where: { id: Number(req.params.id) },
      data: req.body,
    });

    if (!user) {
      return responseError({ res, data: "User not found" });
    }

    return responseSuccess({ res, data: user });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
});

// DELETE

app.delete("/:id", async (req, res) => {
  try {
    await prisma.user.delete({
      where: {
        id: Number(req.params.id),
      },
    });

    return responseSuccess({ res, data: "User deleted" });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
});
