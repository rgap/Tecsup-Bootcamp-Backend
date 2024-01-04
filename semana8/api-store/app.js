// console.log("holass");

// se debe crear un servidor que se ejecute en un puerto de la compu
// crear servidor con express

// Forma antigua de Express JS
// const express = require("express");

// Forma moderna
import express from "express";
// import { responseError, responseSuccess } from "./responses.js";
import { searchById } from "./utils.js";

const app = express();
// para entender json
// body-parser es la manera antigua
app.use(express.json());

const users = [
  {
    id: 1,
    name: "Rel",
    lastname: "Guzman",
    email: "rgap@gmail.com",
    password: "rgap123",
  },
];

// Metodo HTTP GET
// app.get("/", function (request, response) {
//   //   return response.send("Hola mundo");
//   //   return response.json("Hola mundo 2");

//   return response.json({
//     ok: true,
//     data: users,
//   });
// });

// READ

// minificado
app.get("/", (req, res) => {
  return res.status(200).json({
    ok: true,
    data: users,
  });
});

// parametros por URL
app.get("/:id", (req, res) => {
  const user = searchById(users, Number(req.params.id));
  // si no encuentra, retorna undefined

  if (!user) {
    return res.status(404).json({
      ok: false,
      data: "User not found",
    });
  }

  return res.status(200).json({
    ok: true,
    data: user,
  });
});

// CREATE

app.post("/", (req, res) => {
  const user = req.body;
  user.id = users.length + 1;
  users.push(user);

  return res.status(201).json({
    ok: true,
    data: user,
  });
});

// UPDATE

app.put("/:id", (req, res) => {
  const user = searchById(users, Number(req.params.id));

  if (!user) {
    return res.json({
      ok: false,
      data: "User not found",
    });
  }

  const body = req.body;

  Object.entries(body).forEach(([key, value]) => {
    user[key] = value;
  });

  return res.status(200).json({
    ok: true,
    data: user,
  });
});

// DELETE

app.delete("/:id", (req, res) => {
  const user = searchById(users, Number(req.params.id));

  if (!user) {
    return res.json({
      ok: false,
      data: "User not found",
    });
  }

  users.splice(user, 1);

  return res.status(200).json({
    ok: true,
    data: "User deleted",
  });
});
// se ejecuta al iniciar el server
app.listen(3000, function () {
  console.log("El servidor inicio en el puerto 3000 http://localhost:3000");
});
