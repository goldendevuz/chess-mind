import { useEffect, useMemo, useState } from "react";
import { Chess } from "chess.js";
import { ChessBoard } from "./components/ChessBoard";
import { createGame } from "./api/game";
import { useGameStore } from "./store/gameStore";

const GAME_ID = "demo-game";

export function App() {
  const [status, setStatus] = useState("connecting");
  const game = useGameStore((state) => state.game);
  const setGame = useGameStore((state) => state.setGame);
  const [socket, setSocket] = useState<WebSocket | null>(null);
  const chess = useMemo(() => new Chess(game?.fen), [game?.fen]);

  useEffect(() => {
    let socket: WebSocket | null = null;
    let mounted = true;

    (async () => {
      const created = await createGame(GAME_ID);
      if (!mounted) return;
      setGame(created);
      setStatus("ready");
      socket = new WebSocket(`ws://localhost:8000/games/${GAME_ID}/ws`);
      socket.onopen = () => setStatus("live");
      socket.onmessage = (event) => {
        const next = JSON.parse(event.data) as typeof created;
        setGame(next);
      };
      setSocket(socket);
    })().catch(() => setStatus("error"));

    return () => {
      mounted = false;
      socket?.close();
    };
  }, [setGame]);

  const sendMove = (uci: string) => {
    if (!chess.move({ from: uci.slice(0, 2), to: uci.slice(2, 4), promotion: "q" })) return;
    socket?.send(uci);
  };

  return (
    <div className="app">
      <div className="shell">
        <main className="board">
          <div className="hero">
            <p className="eyebrow">ChessMind</p>
            <h1>Calm training for serious chess improvement.</h1>
            <p className="subtle">Status: {status}</p>
          </div>
          <ChessBoard fen={game?.fen ?? "start"} onMove={sendMove} />
        </main>
        <aside className="side">
          <h2>Game state</h2>
          <p>{game ? `Moves: ${game.moves.length}` : "Loading game..."}</p>
          <pre className="fen">{game?.fen ?? "start"}</pre>
        </aside>
      </div>
    </div>
  );
}
