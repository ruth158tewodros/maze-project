Maze Generator and Solver. 
This project implements a dynamic maze generator and a backtracking solver using Python's Turtle graphics. It demonstrates the use of stack-based algorithms to navigate complex data structures and satisfy university-level Computer Graphics requirements.
🚀 Features: Dynamic Generation: Uses a "Mouse" (Randomized Depth-First Search) to eat through walls and create a perfect maze.
   Backtracking Solver: A visual solver that explores the maze with a red dot and backtracks using a blue dot when it hits a dead end.
   Mandatory Data Structures: Built using northWall and eastWall 2D arrays to manage grid boundaries.
   The "Challenge" Bonus: Includes a post-generation cycle where an extra wall is removed, creating a loop that tests the solver's ability to handle non-tree structures
   How it Works 1. The Generation Process. The maze starts as a solid grid where all walls are intact (1). A "mouse" starts at $(0, 0)$ and uses a stack to keep track of its path. It randomly selects unvisited neighbors, "eats" the wall between them (setting the wall value to 0), and moves forward until it must backtrack. 
   2. The Solver Logic The solver uses a second stack-based DFS to find a path from the start to the exit. Red Dots: Represent the current path being explored.Blue Dots: Represent "popped" cells from the stack, visually marking dead ends that the algorithm has discarded.💻 Tech Stack: Language: Python 3.12+, Library: Turtle (Standard Library)Version Control: Git/GitHub for process documentation
