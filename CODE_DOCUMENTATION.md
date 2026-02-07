# Architecture & Code Walkthrough

## 📁 Project Structure

```text
snake_cli/
├── main.py                 # Application Entry Point
├── data/                   # Data Management & Persistence
│   ├── config.py           # Settings loader/saver
│   ├── stats.py            # Session statistics logger
│   └── leaderboard.py      # Leaderboard data formatting
├── game/                   # Core Logic
│   ├── loop.py             # Main Game Controller & execution flow
│   ├── snake.py            # Snake entity and movement logic
│   ├── food.py             # Food entity and spawning strategies
│   ├── state.py            # Session state tracking
│   └── obstacles.py        # Static obstacle management
├── ui/                     # Presentation Layer
│   ├── renderer.py         # Curses abstraction layer
│   ├── screens.py          # Menu, Pause, and Game Over screens
│   ├── colors.py           # Curses color definitions
│   └── themes.py           # Predefined color schemes
├── tests/                  # Unit tests (pytest)
├── run_snake.bat           # Windows Launcher
└── run_snake.sh            # Unix/macOS Launcher
```

## 🏗️ High-Level Architecture

The project follows a **Modified MVC (Model-View-Controller)** pattern adapted for terminal rendering:

1.  **Models (`game/*.py`, `data/*.py`)**: Encapsulate the state of the snake, food, obstacles, and historical stats.
2.  **View (`ui/*.py`)**: Handles all `curses` interactions, pixel rendering, and screen management.
3.  **Controller (`game/loop.py`)**: Orchestrates the input-update-draw cycle, managing the transitions between game states.

## 核心模块 (Core Modules)

| Module | Purpose | Key Responsibility |
| :--- | :--- | :--- |
| `GameController` | Orchestration | Manages the main game loop, input processing, and frame timing. |
| `Renderer` | abstraction | Provides a clean API for drawing characters and colors in the terminal. |
| `Snake` | Entity Logic | Handles coordinate math for movement, growth, and collision. |
| `ConfigManager` | Persistence | Synchronizes in-memory settings with `config.json`. |
| `StatsManager` | Persistence | Appends session summaries to `stats.json`. |

## 🔄 Data Flow

```mermaid
graph TD
    A[main.py] --> B[ConfigManager]
    A --> C[Renderer]
    A --> D[GameController]
    D --> E[Snake & Food]
    D --> F[ScreenManager]
    E --> G[State Manager]
    G --> H[StatsManager]
    H --> I[(stats.json)]
```

1.  **Input**: `Renderer.get_input()` captures non-blocking keystrokes.
2.  **Update**: `GameController.update()` moves entities and checks for collisions based on captured input.
3.  **Draw**: `Renderer` wipes the screen and draws the updated state.
4.  **Save**: On `Game Over`, `StatsManager` persists the `GameState` summary.

## 📦 Dependencies

-   **Runtime**: Python 3.10+, `windows-curses` (Windows only).
-   **Development**: `pytest` for running the automated test suite.

## 🏁 Execution Flow

1.  **Entry (`main.py`)**: `curses.wrapper` initializes the terminal and passes control to `main`.
2.  **Initialization**: Managers load configurations and historical stats.
3.  **Menu Loop**: `ScreenManager.show_start_page` captures user settings.
4.  **Active Loop**: `GameController.start_game` runs until collision or manual quit.
5.  **Termination**: `ScreenManager.show_end_page` collects player name and triggers statistics logging.
