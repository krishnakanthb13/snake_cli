#!/bin/bash

# ==========================================
# Snake CLI Game Launcher (Unix/Mac)
# ==========================================

APP_NAME="Snake CLI Game"
ENTRY_POINT="main.py"

echo "Starting $APP_NAME..."

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 not found. Please install Python 3.10+."
    exit 1
fi

# Check for dependencies
if [ -f "requirements.txt" ]; then
    # Check if curses (native on unix) is available or if we need to install extras
    # Usually standard python3 has curses on unix
    python3 -c "import curses" &> /dev/null
    if [ $? -ne 0 ]; then
        echo "[INFO] Installing required dependencies..."
        python3 -m pip install -r requirements.txt
    fi
fi

# Graceful shutdown handler
trap "echo 'Cleaning up...'; exit" SIGINT SIGTERM

# Run the game
echo "Launching game..."
python3 "$ENTRY_POINT"

EXIT_CODE=$?
if [ $EXIT_CODE -ne 0 ]; then
    echo ""
    echo "[INFO] Game exited with code $EXIT_CODE."
    read -n 1 -s -r -p "Press any key to close..."
fi
