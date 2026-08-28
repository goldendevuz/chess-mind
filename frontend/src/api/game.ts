export type GameState = {
  id: string;
  fen: string;
  moves: string[];
};

export async function createGame(gameId: string): Promise<GameState> {
  const response = await fetch(`http://localhost:8000/games/${gameId}`, { method: "POST" });
  if (!response.ok) throw new Error("failed to create game");
  return response.json() as Promise<GameState>;
}

