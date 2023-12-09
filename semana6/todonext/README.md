## NEXTJS version APP ROUTER

/src
-- /app
-----|--- page.tsx
-----|--- layout.tsx (layout for default para todas las rutas)
-----|--- /info (localhost:info)
----------|--- page.tsx
----------|--- layout.tsx (opcional: para crear estructura propia)
--------| /contacto (localhost:contactanos)
----------|--- page.tsx
----------|--- layout.tsx (opcional)

Layer: CAPA
Layour: ENVOLTORIO DE LAS CAPAS - MAQUETA

(SSR) Server side rendering (forma del pasado pero nextjs lo usa)
(CSR) React js, Angular, Vue (nueva forma)

### Example

#### CSR

navegador (www.domain.com) ---> request ---> Server (Node)
......... navegador ...... <--- response --- Server (script.js)

script.js contiene una app web completa
que al llegar al navegador, comienza a renderizarse

Entrega un html + script.js

##### Desventajas:

- SEO
- Procesamiento irregular de la aplicación
- Solo para sitios NO PUBLICOS (que requiere login)
- Cosas: https://astro.build/

#### SSR

navegador (www.domain.com) ---> request ---> Server (Node)
......... navegador ...... <--- response --- Server (Procesa, RENDERIZA, y entrega un HTML completo + script.js)

script.js contiene partes de la app web que deben ejecutarse en el navegador. Pero HTML está completo con todo.

##### Desventajas:

- Algunos componentes requieren ser ejecutados en el cliente (ejm: modales)
- Aunque Next permite que algunos componentes sean renderizados en el cliente

## Default README

This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.
