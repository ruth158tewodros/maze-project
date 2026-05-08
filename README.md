Ruth Tewodros sec1 UGR/7383/16
 loom video link https://www.loom.com/share/d72f98979c0d4a868951770f32560b32

Maze Generator and Solver

This project implements a dynamic maze generator and a backtracking solver using Python's **Turtle** graphics. It demonstrates the use of stack-based algorithms to navigate complex data structures and satisfy the core requirements for the Computer Graphics assignment.

 🚀 Features

Dynamic Generation**: Uses a "Mouse" logic (Randomized Depth-First Search) to eat through walls and create a perfect maze in real-time.
Backtracking Solver**: A visual solver that explores the maze with a **red dot** and marks dead ends with a **blue dot** when popping the stack.
Mandatory Data Structures**: Built using `northWall` and `eastWall` 2D arrays to manage grid boundaries as required.
The "Challenge" Bonus**: Includes a post-generation cycle where an extra wall is randomly removed to break the "shoulder-to-the-wall" rule, proving the solver uses true backtracking.

 🛠️ How it Works

 1. The "Eating Mouse" (Generation)

The maze starts as a solid grid where all walls are intact (`1`). A "mouse" starts at $(0, 0)$ and uses a **stack** to keep track of its path. It randomly selects unvisited neighbors, "eats" the wall between them by setting the wall value to `0`, and moves forward until it must backtrack.

2. The Backtracking Solver

The solver uses a second stack-based DFS to find a path from the start to the exit.
Red Dots: Represent the current path being actively explored.
Blue Dots: Represent "popped" cells from the stack, visually marking dead ends that the algorithm has discarded.

💻 Tech Stack & Requirements

Language: Python 3.12+.
Library: Turtle (Standard Library).
Data Structures: 2D Lists/Arrays (`northWall`, `eastWall`, `visited`).

 📝 Evolution of Work (Commit History)

1.Initial grid setup**: Defining the mandatory data structures.
2.Added Turtle drawing: Implementing the visual "eating" mouse and generation logic.
3.Implemented backtracking solver: Finalizing the red/blue dot visualization and the bonus cycle challenge.

