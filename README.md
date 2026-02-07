# 🐍 Snake CLI Game

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A highly customizable, feature-rich, cross-platform Snake game designed to run beautifully in your command prompt or terminal.

## ✨ Features

- **🎨 High Customizability**: 
  - Choose individual snake shapes (`█`, `■`, `●`, `@`, `#`, `░`).
  - Configure colors (Green, Blue, Red, Yellow, White).
  - **Mixed Rendering Modes**: Same Shape/Color, Mixed Colors, Mixed Shapes, or even Mixed Shapes + Colors!
- **🍎 Strategic Gameplay**: 
  - **Small Food**: Common, steady growth.
  - **Big Food**: Rare, higher points, and faster growth.
- **📊 Persistent Stats & Leaderboards**: 
  - Sessions are automatically saved to `stats.json`.
  - View the Top 10 High Scores on a dedicated leaderboard screen.
- **⚙️ Advanced Settings**: 
  - Toggle **Walls** (Wrap-around mode vs. Collision mode).
  - Toggle **Obstacles** for increased difficulty.
  - Adjustable **Game Speed**.
- **🌈 Theming**: Instant personality with preset themes: **Neon**, **Matrix**, **Retro**, and **Classic**.

---

## 🎮 Controls

### In-Game
| Key | Action |
| :--- | :--- |
| **Arrow Keys / WASD** | Move Snake |
| **P** | Pause / Resume |
| **I** | View Session Stats (Overlay) |
| **L** | View Leaderboard (Overlay) |
| **Q** | Quit current game |

### Menus
| Key | Action |
| :--- | :--- |
| **Up/Down / WS** | Navigate Menu Items |
| **Enter / Space** | Select / Toggle Setting |
| **Q** | Back to previous screen / Exit |

---

## 🚀 Quick Start

### 🪟 Windows
Just double-click the launcher:
```cmd
run_snake.bat
```
*(This will automatically check for Python and install dependencies for you!)*

### 🐧 Linux / 🍎 macOS
1. Make it executable:
   ```bash
   chmod +x run_snake.sh
   ```
2. Run it:
   ```bash
   ./run_snake.sh
   ```

### 🐍 Manual Installation
1. Ensure **Python 3.10+** is installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch:
   ```bash
   python main.py
   ```

---

## 🛠️ Development

- **Architecture**: Modular Python modules separated into `game/`, `ui/`, and `data/`.
- **Rendering**: Pure `curses` / `windows-curses` (no heavy GUI frameworks).
- **Quality Assurance**: Unit tests for core mechanics.
  ```bash
  python -m pytest
  ```

### Directory Structure
```text
snake_cli/
├── main.py           # Entry point
├── data/             # Config, Stats, Leaderboard logic
├── game/             # Core Snake, Food, and Loop logic
├── ui/               # Curses renderer, Screens, and Themes
├── tests/            # Pytest suite
└── stats.json        # Persistent historical data
```

---

## 📜 License

This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file for details.
