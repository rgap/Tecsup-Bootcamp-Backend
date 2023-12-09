"use client";

import { useState } from "react";

export default function Header() {
  const [counter, setCounter] = useState(0);

  return (
    <nav className="h-[10vh] bg-slate-600 flex justify-center">
      <div>
        <p>Header </p>
      </div>
      <div>
        <p>Counter: {counter}</p> {/* Displaying the counter value */}
        <button onClick={() => setCounter(counter + 1)}>Counter</button>
      </div>
    </nav>
  );
}
