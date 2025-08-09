// Line 1: Import React state to keep the demo button interactive
import { useState } from "react";

function App() {
  // Line 4: Tiny state just to prove React is live (hot reload + interactivity)
  const [count, setCount] = useState(0);

  // Line 7: Use semantic markup + CSS classes (no inline layout styles)
  return (
    <div className="center-wrap">
      {/* Line 10: Constrain width and center text */}
      <div className="center-col">
        {/* Line 12: Title */}
        <h1>AetherOps</h1>

        {/* Line 15: Tagline with muted tone */}
        <p className="lead">A mystical force meets modern operations.</p>

        {/* Line 18: Demo button */}
        <button onClick={() => setCount((c) => c + 1)}>Clicks: {count}</button>

        {/* Line 22: Small helper text */}
        <p className="small">
          API health will be at <code>http://localhost:8000/health</code>{" "}
          (coming soon)
        </p>
      </div>
    </div>
  );
}

export default App;
