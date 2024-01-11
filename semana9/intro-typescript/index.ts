const nombre: string = "Linder";
const edad: number = 99;
const esMayor: boolean = true;
let nombreAny: any = "rgap"; // solo cuando no se puede saber su tipo
// nombre = 10

function sumar(n1: number, n2: number): number {
  return n1 + n2;
}

console.log(sumar(10, 1));

if (esMayor) {
  console.log(`Hola me llamo ${nombre} y tengo ${edad} años`);
} else {
  console.log(`Te falta crecer`);
}

// INTERFACE
interface User {
  name: string;
  lastname: string;
  email: string;
  password: string;
}

interface UserOptionalAddress {
  name: string;
  lastname: string;
  email: string;
  password: string;
  address: string;
}

const user: User = {
  name: "Rel",
  lastname: "Guzman",
  email: "rgap@gmail.com",
  password: "1312312",
  address: "av mi casa",
};

const user2: UserOptionalAddress = {
  name: "Rel",
  lastname: "Guzman",
  email: "rgap@gmail.com",
  password: "1312312",
  address: "av mi casa",
};

const users: User[] = [];

function insertUser(user: User): void {
  users.push(user);
}

function getNameFromUser(user: User): string {
  return `${user.name} ${user.lastname}`;
}

// type
type Status = "created" | "on-hold" | "in-progress" | "done";

interface Task {
  title: string;
  date: Date;
  status: Status;
}

const task: Task = {
  title: "Pagar cuentas",
  date: new Date(),
  status: "",
};
