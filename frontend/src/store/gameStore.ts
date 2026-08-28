import { create } from "zustand";
import type { GameState } from "../api/game";

type GameStore = {
  game: GameState | null;
  setGame: (game: GameState) => void;
};

export const useGameStore = create<GameStore>((set) => ({
  game: null,
  setGame: (game) => set({ game }),
}));

