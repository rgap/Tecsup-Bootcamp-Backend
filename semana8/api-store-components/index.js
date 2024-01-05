import { app } from "./src/app.js";

// se ejecuta al iniciar el server
app.listen(3000, function () {
  console.log("El servidor inicio en el puerto 3000 http://localhost:3000");
});
