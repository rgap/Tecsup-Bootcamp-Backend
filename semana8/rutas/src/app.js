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
    //// result = {
    ////   data,
    ////   status: response.status
    //// };
    //// id (result.status == 200) { ... }
    //////

    return responseSuccess({ res, data: "User authenticated successfully" });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
});

app.get("/stock/:productId/:colorId/:sizeId", async (req, res) => {
  try {
    /*
    const stock = await prisma.stock.findUnique({
      where: {
        productId: req.params.productId,
        colorId: req.params.colorId,
        sizeId: req.params.sizeId,
      },
      select: {
        stock_quantity: true,
        price: true,
      },
    });

    if (!stock) {
      return responseError({ res, data: "Stock not found" });
    }
    */

    // This seems like placeholder data. Replace it with the actual query result
    const stock = {
      stock_quantity: 10,
      price: 49.99,
    };

    return responseSuccess({ res, data: stock });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
});

app.post("/stock/quantity-and-price", async (req, res) => {
  try {
    const { productId, colorId, sizeId } = req.body;

    /*
    const stock = await prisma.stock.findUnique({
      where: {
        productId: productId,
        colorId: colorId,
        sizeId: sizeId,
      },
      select: {
        stock_quantity: true,
        price: true,
      },
    });

    if (!stock) {
      return responseError({ res, data: "Stock not found" });
    }
    */

    const stock = {
      stock_quantity: 10,
      price: 49.99,
    };

    return responseSuccess({ res, data: stock });
  } catch (error) {
    return responseError({ res, data: error.message });
  }
});
