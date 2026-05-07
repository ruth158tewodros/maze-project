import turtle
import random


R, C = 15, 15
CELL_SIZE = 30
northWall = [[1 for _ in range(C)] for _ in range(R)]
eastWall = [[1 for _ in range(C)] for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]


screen = turtle.Screen()
screen.setup(C * CELL_SIZE + 100, R * CELL_SIZE + 100)
screen.tracer(0) # Makes drawing instant; remove if you want to watch it draw slowly
t = turtle.Turtle()
t.hideturtle()

def draw_maze():
    t.clear()
    # Center the maze on screen
    off_x, off_y = -(C * CELL_SIZE)/2, -(R * CELL_SIZE)/2
    
    for r in range(R):
        for c in range(C):
            x, y = off_x + c * CELL_SIZE, off_y + r * CELL_SIZE
            if northWall[r][c]:
                t.penup(); t.goto(x, y + CELL_SIZE); t.pendown(); t.goto(x + CELL_SIZE, y + CELL_SIZE)
            if eastWall[r][c]:
                t.penup(); t.goto(x + CELL_SIZE, y); t.pendown(); t.goto(x + CELL_SIZE, y + CELL_SIZE)
    screen.update()


def generate_maze(start_r, start_c):
    stack = [(start_r, start_c)]
    visited[start_r][start_c] = True

    while stack:
        r, c = stack[-1]
        neighbors = []
        if r + 1 < R and not visited[r+1][c]: neighbors.append((r + 1, c, 'N', r, c))
        if c + 1 < C and not visited[r][c+1]: neighbors.append((r, c + 1, 'E', r, c))
        if r - 1 >= 0 and not visited[r-1][c]: neighbors.append((r - 1, c, 'N', r - 1, c))
        if c - 1 >= 0 and not visited[r][c-1]: neighbors.append((r, c - 1, 'E', r, c - 1))

        if neighbors:
            next_r, next_c, wall_type, w_r, w_c = random.choice(neighbors)
            if wall_type == 'N': northWall[w_r][w_c] = 0
            else: eastWall[w_r][w_c] = 0
            visited[next_r][next_c] = True
            stack.append((next_r, next_c))
        else:
            stack.pop()


generate_maze(0, 0)
draw_maze()
print("Maze generation complete!")
turtle.done()