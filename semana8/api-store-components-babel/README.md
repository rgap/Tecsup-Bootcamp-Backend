## Node JS

```
npm init
node app.js
npm install express
```

```
"type": "module" en package.json habilita ES6 para usar "import"
```

```
Nodemon -> node js en debug mode
```

```
Forma nativa

node --watch app.js

Para ejecutarlo con npm run dev

"dev": "node --watch app.js"
```

```
Prisma ORM

 npm install prisma --save-dev
 npx prisma
 npx prisma init

```

```
npx prisma migrate dev --name create_user_table
```

Prisma Client

```
npm install @prisma/client
npx prisma generate
```

Babel para usar js "moderno". Por ejemplo sin el js al hacer import

```
npm install -D @babel/cli @babel/core @babel/preset-env @babel/node
NO ----> npm i -D babel-watch
```

Nodemon

```
npm i -D nodemon
```
