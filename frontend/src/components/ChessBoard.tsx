import { useEffect, useRef } from "react";
import { Chessground } from "@lichess-org/chessground";
import "@lichess-org/chessground/assets/chessground.base.css";
import "@lichess-org/chessground/assets/chessground.brown.css";
import "@lichess-org/chessground/assets/chessground.cburnett.css";

type Props = {
  fen: string;
  onMove: (uci: string) => void;
};

export function ChessBoard({ fen, onMove }: Props) {
  const ref = useRef<HTMLDivElement | null>(null);
  const groundRef = useRef<any>(null);

  useEffect(() => {
    if (!ref.current) return;
    if (!groundRef.current) {
      groundRef.current = Chessground(ref.current, {
        fen,
        coordinates: true,
        movable: {
          free: false,
          color: "both",
        },
        events: {
          move: (orig, dest) => onMove(`${orig}${dest}`),
        },
      } as any);
    } else {
      groundRef.current.set({ fen });
    }
    return () => undefined;
  }, [fen, onMove]);

  return <div ref={ref} className="chessboard" />;
}
