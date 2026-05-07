# Maze Assignment - Ruth Tewodros
# Data Structure: northWall and eastWall arrays

R, C = 15, 15

# 1 = Wall exists, 0 = Wall is eaten
northWall = [[1 for _ in range(C)] for _ in range(R)]
eastWall = [[1 for _ in range(C)] for _ in range(R)]

# Track visited cells for the "Mouse"
visited = [[False for _ in range(C)] for _ in range(R)]

print("Grid initialized with all walls intact.")
