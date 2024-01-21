import { PrismaClient } from "@prisma/client";
import { responseError, responseSuccess } from "../../network/responses.js";

const prisma = new PrismaClient();

// READ

export async function list(req, res) {
  try {
    const users = await prisma.user.findMany();
    return responseSuccess({ res, data: users });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
}

// READ by composite key

export async function getByCompositeKey(req, res) {
  try {
    const { userId, email } = req.params;
    const user = await prisma.user.findUnique({
      where: {
        userId_email: {
          userId: Number(userId),
          email: email,
        },
      },
    });

    if (!user) {
      return responseError({ res, data: "User not found" });
    }

    return responseSuccess({ res, data: user });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
}

// CREATE

export async function store(req, res) {
  try {
    await prisma.user.create({
      data: req.body,
    });

    return responseSuccess({ res, data: "User created", status: 201 });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
}

// UPDATE

export async function update(req, res) {
  try {
    const { userId, email } = req.params;
    const user = await prisma.user.update({
      where: {
        userId_email: {
          userId: Number(userId),
          email: email,
        },
      },
      data: req.body,
    });

    return responseSuccess({ res, data: "User updated" });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
}

// DESTROY

export async function destroy(req, res) {
  try {
    const { userId, email } = req.params;
    await prisma.user.delete({
      where: {
        userId_email: {
          userId: Number(userId),
          email: email,
        },
      },
    });

    return responseSuccess({ res, data: "User deleted" });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
}
