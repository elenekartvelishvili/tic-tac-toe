#  Tic-Tac-Toe AI (Minimax Algorithm)

##  Project Overview

This project implements a console-based Tic-Tac-Toe game in Python where the AI always plays first as "X". The AI is designed to be unbeatable using the Minimax algorithm, ensuring optimal decision-making at every move. The player plays as "O" against the AI.

---

##  How It Works

The game is built on a 3×3 board represented as a 1D list of size 9. Each index corresponds to a cell on the board.

Winning conditions are predefined using index combinations for rows, columns, and diagonals.

The AI uses the **Minimax algorithm**, which simulates all possible future moves and selects the optimal one assuming the opponent also plays perfectly.

---

##  Algorithm Explanation

- AI = Maximizing player (X)
- Human = Minimizing player (O)

Each game state is assigned a score:
- +10 → AI wins  
- -10 → Human wins  
- 0 → Draw  

The AI evaluates all possible moves recursively and chooses the move that gives the best guaranteed outcome. Moves are simulated and then undone using backtracking to explore all possibilities.

---

##  Why Minimax?

Minimax is used because:
- It explores the full game tree
- It assumes optimal play from both players
- It guarantees the best possible outcome for the AI

Since Tic-Tac-Toe has a small state space, full search is possible, making the AI unbeatable.

---

##  Game Rules

- AI always plays first as "X"
- Player plays as "O"
- Players take turns marking empty cells
- First to get 3 in a row wins
- If board fills with no winner → draw

---

##  Features

- Console-based gameplay
- AI always plays first
- Unbeatable AI using Minimax
- Win, lose, and draw detection
- Simple and lightweight implementation

---

##  Technologies Used

- Python 3
- Recursion (Minimax)
- List-based board representation

---

##  Key Concepts Learned

- Game theory basics
- Minimax algorithm
- Backtracking
- State-space search
- Decision trees
