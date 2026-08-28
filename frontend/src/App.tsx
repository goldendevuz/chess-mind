export function App() {
  return (
    <div className="app">
      <div className="shell">
        <main className="board">
          <h1>ChessMind</h1>
          <p>Real-time board skeleton with calm, dark UI.</p>
          <div id="board-root" />
        </main>
        <aside className="side">
          <h2>Game state</h2>
          <p>WebSocket integration comes next.</p>
        </aside>
      </div>
    </div>
  );
}

