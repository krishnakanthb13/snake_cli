# Release Notes

## [v0.0.4] - 2026-02-08

The initial release of **Snake CLI**! A highly customizable, feature-rich Snake game designed for the terminal.

### 🚀 New Features
- **Customizable Appearance**: Choose from multiple snake shapes (`█`, `■`, `●`, `@`, `#`) and 7 vibrant colors.
- **Mixed Rendering Modes**: Play with static shapes/colors, or enable dynamic "Mixed" modes for a trippy visual experience.
- **Strategic Food System**:
  - **Small Food**: Steady growth.
  - **Big Food**: Rare (configurable chance) for high points and rapid growth.
  - **Food Customization**: Set food color or keep it random.
- **Persistent Stats & Leaderboards**:
  - Automatic session logging to `stats.json`.
  - **Leaderboard**: View top 10 scores, sortable by Score or Survival Time.
  - **History Browser**: Review every past game session with pagination.
- **Game Modes**:
  - **Walls**: Toggle on/off (wrap-around mode).
  - **Obstacles**: Toggle static obstacles for extra challenge.
  - **Speed**: Adjustable difficulty (5, 10, 15, 20).
- **Themes**: Instant visual makeovers with Classic, Neon, Matrix, and Retro presets.

### ⚡ Improvements
- **Horizontal Scaling**: Implemented 2x character width to ensure square-like pixels and balanced movement speed in all directions.
- **Cross-Platform**: Native support for Windows (via `windows-curses`) and Unix/macOS.
- **Zero-Config Launch**: Includes `.bat` and `.sh` scripts for instant play.

### 🏗️ Architecture
- **MVC Design**: Clean separation between Game Logic, UI Rendering, and Data Management.
- **State Management**: Robust tracking of session state, settings, and historical data.
