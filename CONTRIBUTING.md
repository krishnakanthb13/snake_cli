# Contributing to Snake CLI

First off, thank you for considering contributing to Snake CLI! It's people like you that make the open-source community such an amazing place.

## 🐛 Reporting Bugs

1.  **Check for existing issues**: Search the GitHub issue tracker before opening a new one.
2.  **Use a clear title**: Describe the problem succinctly.
3.  **Provide context**: Include your OS, terminal emulator (e.g., Windows Terminal, iTerm2, Kitty), and Python version.
4.  **Steps to reproduce**: How did you encounter the bug?
5.  **Screenshots**: If it's a visual glitch in the terminal, a screenshot is extremely helpful.

## ✨ Feature Suggestions

We love new ideas! When suggesting features:
-   Explain the **value** it adds to the game.
-   Consider if it fits within the "Terminal First" design philosophy.
-   Suggest a possible implementation if you have one in mind.

## 🛠️ Local Development Setup

1.  **Fork and Clone**:
    ```bash
    git clone https://github.com/krishnakanthb13/snake_cli.git
    cd snake_cli
    ```
2.  **Environment**: 
    - Create a virtual environment (optional but recommended):
      ```bash
      python -m venv venv
      source venv/bin/activate  # Unix
      .\venv\Scripts\activate   # Windows
      ```
3.  **Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Verify Setup**:
    ```bash
    python -m pytest
    ```

## 🤝 Contribution Workflow

1.  **Branch**: Create a new branch for your feature or fix (`git checkout -b feature/amazing-feature`).
2.  **Code**: Follow the existing modular structure. Keep UI and Game logic separate.
3.  **Test**: Ensure all unit tests pass and manually verify the UI screens.
4.  **Commit**: Use descriptive commit messages.
5.  **Push & PR**: Push to your fork and open a Pull Request to the `main` branch.

## ✅ Pre-submission Checklist

- [ ] Does the game still launch on both Windows and Unix?
- [ ] Did you update the `CODE_DOCUMENTATION.md` if you added new modules?
- [ ] Are all dependencies added to `requirements.txt`?
- [ ] Have you run the existing tests using `pytest`?

---

*By contributing, you agree that your contributions will be licensed under the project's MIT/GPL License.*
