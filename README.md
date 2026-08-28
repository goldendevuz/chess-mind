# ChessMind

ChessMind is being rewritten from scratch as a FastAPI + TypeScript chess platform focused on calm UX, real-time play, and AI-assisted learning.

## Current state

- Domain-first backend layout is in place
- Game domain has real move validation via `python-chess`
- FastAPI routers and a WebSocket game endpoint are scaffolded
- React + Vite frontend skeleton is in place
- Docker Compose includes backend, frontend, postgres, and redis

## Next step

Wire the frontend to the backend WebSocket and expand persistence, auth, analysis, and matchmaking.
