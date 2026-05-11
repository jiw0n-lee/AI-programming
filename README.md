# Monster Ball Finder Game

A simple reaction-based clicking game made with Python and Tkinter.

## Game Description

Press the `Enter` key to start the game.

When the game starts, multiple balls will randomly move around the screen.  
Once the message **"Click the Monster Ball!"** appears at the top of the screen,  
you must find and click the Monster Ball within 1 second.

- Clicking the Monster Ball = Success
- Clicking the wrong ball or running out of time = Failure

## Controls

- `Enter` : Start / Restart game
- `Esc` : Exit game
- Mouse Click : Select a ball
- `A` or `Q` : Cheat key (automatic success)

## Features

- Random ball placement
- Monster Ball click detection
- 1-second time limit
- Success / Failure result screen
- Cheat key system
- Restart functionality

## Demo

![demo](demo.gif)

## How to Run

```bash
python main.py
```

## Project Structure

```txt
monsterball-game/
├── main.py
├── gui_core.py
├── assets/
│   ├── boom_ball.png
│   ├── basketball.png
│   ├── tennis_ball.png
│   ├── golf_ball.png
│   ├── soccer_ball.png
│   ├── baseball.png
│   └── monster_ball.png
├── demo.gif
├── README.md
└── .gitignore
```

## Technologies Used

- Python
- Tkinter

## What I Learned

- Basic game loop structure
- Event handling with keyboard and mouse input
- Object collision and click detection
- Managing game states
- Organizing a small game project
