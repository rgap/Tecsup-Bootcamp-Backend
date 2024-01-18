import Image from "next/image";
export default function Hero() {
  return (
    <section className="flex flex-col items-center gap-5">
      <h1 className="text-5xl text-center font-semibold">I'm a dev</h1>
      <Image
        src="https://avatars.githubusercontent.com/u/1432440?v=4"
        alt=""
        className="rounded-full"
        width={200}
        height={400}
      />
    </section>
  );
}
