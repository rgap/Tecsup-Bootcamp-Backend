import { menu } from "@/mock/menu";
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import Link from "next/link";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

const metadata: Metadata = {
  title: "Mi marca personal",
  description: "Hola soy Linder Hassinger, senior software developer",
};

export { metadata };

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <nav>
          <ul className="flex bg-black mx-10 my-5 justify-around rounded-full">
            {menu.map((item) => (
              <li
                key={item.id}
                className="hover:bg-orange-600 cursor-pointer hover:rounded-full px-6 py-3 my-1 transition-all duration-500"
              >
                <Link href={item.href} className="text-white">
                  {item.title}
                </Link>{" "}
              </li>
            ))}
          </ul>
        </nav>
        {children}
      </body>
    </html>
  );
}
