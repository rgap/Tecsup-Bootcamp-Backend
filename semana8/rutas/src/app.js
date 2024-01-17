import express from "express";

export const app = express();
app.use(express.json());

export function responseSuccess({ res, data, status = 200 }) {
  return res.status(status).json({
    ok: true,
    data,
  });
}

export function responseError({ res, data, status = 500 }) {
  return res.status(status).json({
    ok: false,
    data,
  });
}

app.get("/login1", async (req, res) => {
  try {
    const { email, password } = req.params;

    // const user = await prisma.user.findUnique({
    //   where: {
    //     email: email,
    //     password: password,
    //   },
    // });

    // Llamada de frontend correspondiente al endpoint del backend
    //////
    // const response = await fetch(`http://localhost:3000/login1/${email}/${password}`);
    // const data = await response.json();
    //////

    return responseSuccess({ res, data: "User authenticated successfully" });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
});

app.get("/login2", async (req, res) => {
  try {
    const { email, password } = req.query;

    // const user = await prisma.user.findUnique({
    //   where: {
    //     email: email,
    //     password: password,
    //   },
    // });

    // Llamada de frontend correspondiente al endpoint del backend
    //////
    // const response = await fetch(`http://localhost:3000/login2?email=${email}&password=${password}`);
    // const data = await response.json();
    //////

    return responseSuccess({ res, data: "User authenticated successfully" });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
});

app.post("/login3", async (req, res) => {
  try {
    const { email, password } = req.body;

    // const user = await prisma.user.findUnique({
    //   where: {
    //     email: email,
    //     password: password,
    //   },
    // });

    // Llamada de frontend correspondiente al endpoint del backend
    //////
    // const response = await fetch('http://localhost:3000/login3', {
    //   method: 'POST',
    //   headers: {
    //     'Content-Type': 'application/json',
    //   },
    //   body: JSON.stringify({ email, password }),
    // });
    // const data = await response.json();
    //////

    return responseSuccess({ res, data: "User authenticated successfully" });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
});
