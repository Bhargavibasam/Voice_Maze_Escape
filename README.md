# VoiceMazeEscape 🎙️🧩

**VoiceMazeEscape** is an interactive voice-assisted maze escape game built with Python. Players use button controls to navigate a maze displayed using Pygame, while receiving real-time voice feedback powered by pyttsx3. The game guides users through voice prompts and offers helpful tips on quitting or replaying.

---

## 🎮 Game Features

- Visual maze interface using `Pygame`
- On-screen control buttons (Up, Down, Left, Right)
- Voice feedback for every action using `pyttsx3`
- Welcome voice at game start
- Voice prompt on winning: “Do you want to play again?”
- Voice tip if user quits before finishing
- Clean GUI layout with control buttons at the bottom

---

## 📜 Game Rules

- You must navigate the player from the start to the exit (marked as `E`).
- Walls (`#`) cannot be crossed.
- Move using on-screen buttons.
- Reach the exit to win and receive a voice congratulation.
- If you quit early, the game speaks a motivational maze tip.

---
## ▶️ How to Play

- Run the script using:

  ```bash
  python voice_maze_escape.py

## 📦 Prerequisites

-Make sure you have Python installed. You’ll also need these libraries:

```bash
pip install pygame pyttsx3
