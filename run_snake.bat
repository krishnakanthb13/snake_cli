@echo off
setlocal enabledelayedexpansion

:: ==========================================
:: Snake CLI Game Launcher
:: ==========================================

title Snake CLI Game
echo Starting Snake CLI Game...

:: Check for Python
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Python not found in PATH. Please install Python 3.10+.
    pause
    exit /b 1
)

:: Check for dependencies
if not exist "requirements.txt" (
    echo [WARNING] requirements.txt not found. Skipping dependency check.
) else (
    :: Check if windows-curses is installed
    python -c "import curses" >nul 2>nul
    if %errorlevel% neq 0 (
        echo [INFO] Installing required dependencies...
        python -m pip install -r requirements.txt
        if %errorlevel% neq 0 (
            echo [ERROR] Failed to install dependencies.
            pause
            exit /b 1
        )
    )
)

:: Run the game
echo Launching game...
python main.py

if %errorlevel% neq 0 (
    echo.
    echo [INFO] Game exited with code %errorlevel%.
    pause
)

endlocal
