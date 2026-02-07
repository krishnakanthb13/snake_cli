# Design Philosophy

## 🎯 Problem Definition

Terminal games are often seen as "toy" projects with limited scope and visual appeal. Most CLI Snake implementations are either too simple (static colors/shapes) or too complex to set up (requiring specific terminal emulators or heavy libraries).

## 💡 Why This Solution?

**Snake CLI** aims to strike a balance between **Retro Simplicity** and **Modern Customizability**. It acknowledges that while the core mechanic of Snake is simple, the *satisfaction* of the game comes from visual feedback and personal progression.

## 🛠️ Design Principles

1.  **Zero-Configuration Launch**: Using `.bat` and `.sh` launchers ensures the game "just works" regardless of the user's familiarity with Python environments.
2.  **Extensible Visuals**: By decoupling entity logic from rendering, we allow for complex "Mixed Modes" (Mixed shapes/colors) that are rarely seen in terminal games.
3.  **Persistence as Priority**: A game is only as good as its history. Explicit support for stats logging and leaderboards makes every session feel meaningful.
4.  **Terminal Constraints as Assets**: Instead of fighting the grid-based nature of the terminal, we lean into it with ASCII-based themes (**Matrix**, **Neon**) that feel native to the environment.

## 👥 Target Audience

-   **Developers**: Those looking for a quick distraction during compile times.
-   **Retro Enthusiasts**: Players who appreciate the aesthetic of the command prompt.
-   **SSH Users**: Players looking for a game that can be played over remote connections.

## ⚖️ Trade-offs & Constraints

-   **Frame Rate**: Limited by the terminal's refresh rate and `curses` overhead. We prioritize logic consistency over high-frequency rendering.
-   **Color Depth**: Restricted to the standard 8-color pallet supported universally by `curses`, ensuring broad compatibility across older terminals.
-   **Input Handling**: We use non-blocking polls which can vary slightly in latency depending on the terminal emulator's buffer settings.

## 🚀 Real-World Workflow

The game is designed to be a "drop-in" executable. You can add it to your `PATH` or keep it in a tools folder, launch it, play a strategic 3-minute session to climb the leaderboard, and exit back to your terminal workflow instantly.
