# Design Philosophy

## 🎯 Problem Definition

Terminal games are often seen as "toy" projects with limited scope and visual appeal. Most CLI Snake implementations are either too simple (static colors/shapes) or too complex to set up (requiring specific terminal emulators or heavy libraries).

## 💡 Why This Solution?

**Snake CLI** aims to strike a balance between **Retro Simplicity** and **Modern Customizability**. It acknowledges that while the core mechanic of Snake is simple, the *satisfaction* of the game comes from visual feedback and personal progression.

## 🛠️ Design Principles

1.  **Zero-Configuration Launch**: Using `.bat` and `.sh` launchers ensures the game "just works" regardless of the user's familiarity with Python environments.
2.  **Extensible Visuals**: By decoupling entity logic from rendering, we allow for complex "Mixed Modes" (Mixed shapes/colors) that are rarely seen in terminal games.
3.  **Persistence as Priority**: A game is only as good as its history. Explicit support for stats logging, leaderboards, and **full game history browsing** makes every session feel meaningful.
4.  **Terminal Constraints as Assets**: Instead of fighting the grid-based nature of the terminal, we lean into it with ASCII-based themes (**Matrix**, **Neon**) that feel native to the environment.
5.  **Visual Consistency**: Horizontal 2x scaling ensures the snake moves at equal perceived speeds in all directions, eliminating the common "faster vertical movement" issue in terminal games.

## 👥 Target Audience

-   **Developers**: Those looking for a quick distraction during compile times.
-   **Retro Enthusiasts**: Players who appreciate the aesthetic of the command prompt.
-   **SSH Users**: Players looking for a game that can be played over remote connections.
-   **Competitive Players**: Those who enjoy climbing leaderboards and tracking personal bests.

## ⚖️ Trade-offs & Constraints

-   **Frame Rate**: Limited by the terminal's refresh rate and `curses` overhead. We prioritize logic consistency over high-frequency rendering.
-   **Color Depth**: Extended to 7-color palette (including Cyan and Magenta) while maintaining compatibility with standard `curses` terminals.
-   **Input Handling**: We use non-blocking polls which can vary slightly in latency depending on the terminal emulator's buffer settings. Numpad Enter is explicitly handled for wider keyboard support.
-   **Horizontal Scaling**: Using 2 characters per logical X unit creates square "pixels" but halves the effective horizontal resolution.

## 🚀 Real-World Workflow

The game is designed to be a "drop-in" executable. You can add it to your `PATH` or keep it in a tools folder, launch it, play a strategic 3-minute session to climb the leaderboard, and exit back to your terminal workflow instantly.

## 🔮 Future Considerations

-   **Network Leaderboards**: Shared leaderboards across machines.
-   **Power-ups**: Temporary speed boosts or invincibility.
-   **AI Snake**: Computer-controlled opponent for competitive mode.
