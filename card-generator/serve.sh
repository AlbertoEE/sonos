#!/bin/bash
cd "$(dirname "$0")"
PORT=${1:-8080}
echo "Serving at http://localhost:$PORT"
echo "  cards.html      -> http://localhost:$PORT/cards.html"
echo "  cards-full.html -> http://localhost:$PORT/cards-full.html"
python3 -m http.server "$PORT"
