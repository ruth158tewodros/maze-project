import turtle
import random
import time

# --- CONFIGURATION ---
R, C = 15, 15  # Grid size
CELL_SIZE = 30
WIDTH, HEIGHT = C * CELL_SIZE, R * CELL_SIZE

# Mandatory Data Structures
northWall = [[1 for _ in range(C)] for _ in range(R)]
eastWall = [[1 for _ in range(C)] for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

# Setup Turtle
screen = turtle.Screen()
screen.setup(WIDTH + 50, HEIGHT + 50)
screen.title("Maze Assignment - Ruth Tewodros")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen.tracer(0)

def get_coords(r, c):
    """Converts grid coordinates to screen pixels."""
    x = -WIDTH // 2 + c * CELL_SIZE
    y = -HEIGHT // 2 + r * CELL_SIZE
    return x, y

def draw_maze():
    """Renders the current state of the northWall and eastWall arrays."""
    t.clear()
    t.penup()
    for r in range(R):
        for c in range(C):
            x, y = get_coords(r, c)
            # Draw North Wall
            if northWall[r][c] == 1:
                t.goto(x, y + CELL_SIZE)
                t.setheading(0)
                t.pendown()
                t.forward(CELL_SIZE)
                t.penup()
            # Draw East Wall
            if eastWall[r][c] == 1:
                t.goto(x + CELL_SIZE, y)
                t.setheading(90)
                t.pendown()
                t.forward(CELL_SIZE)
                t.penup()
    
    # Draw static boundaries (South and West)
    t.goto(-WIDTH // 2, -HEIGHT // 2)
    t.setheading(0)
    t.pendown()
    t.forward(WIDTH)
    t.setheading(90)
    t.forward(HEIGHT)
    t.setheading(180)
    t.forward(WIDTH)
    t.setheading(270)
    t.forward(HEIGHT)
    t.penup()

def generate_maze(start_r, start_c):
    """Stack-based DFS 'Eating Mouse' logic."""
    stack = [(start_r, start_c)]
    visited[start_r][start_c] = True
    
    while stack:
        r, c = stack[-1]
        neighbors = []
        
        # Check Up, Down, Left, Right
        directions = [('N', r, c, r+1, c), ('S', r-1, c, r-1, c), 
                      ('E', r, c, r, c+1), ('W', r, c-1, r, c-1)]
        
        for d, wr, wc, nr, nc in directions:
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                neighbors.append((d, wr, wc, nr, nc))
        
        if neighbors:
            d, wr, wc, nr, nc = random.choice(neighbors)
            if d == 'N' or d == 'S': northWall[wr][wc] = 0
            if d == 'E' or d == 'W': eastWall[wr][wc] = 0
            
            visited[nr][nc] = True
            stack.append((nr, nc))
            
            # --- DYNAMIC ANIMATION ---
            draw_maze()
            screen.update()
            # time.sleep(0.01) # Uncomment this to slow it down more
        else:
            stack.pop()

def solve_maze(start_r, start_c, end_r, end_c):
    """Backtracking solver with Red/Blue dot visualization."""
    solve_stack = [(start_r, start_c)]
    solve_visited = set([(start_r, start_c)])
    
    # Mark the target exit with a black dot
    ex, ey = get_coords(end_r, end_c)
    t.goto(ex + CELL_SIZE/2, ey + CELL_SIZE/2)
    t.dot(15, "black")

    while solve_stack:
        r, c = solve_stack[-1]
        
        # Draw current path (Red Dot)
        x, y = get_coords(r, c)
        t.goto(x + CELL_SIZE/2, y + CELL_SIZE/2)
        t.dot(10, "red")
        screen.update()
        time.sleep(0.05)
        
        if (r, c) == (end_r, end_c):
            print("Target Reached!")
            break
            
        # Valid moves (no wall between)
        moved = False
        moves = [
            (r+1, c, r, c, 'N'), (r-1, c, r-1, c, 'S'),
            (r, c+1, r, c, 'E'), (r, c-1, r, c-1, 'W')
        ]
        
        for nr, nc, wr, wc, d in moves:
            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in solve_visited:
                if (d in ['N', 'S'] and northWall[wr][wc] == 0) or \
                   (d in ['E', 'W'] and eastWall[wr][wc] == 0):
                    solve_stack.append((nr, nc))
                    solve_visited.add((nr, nc))
                    moved = True
                    break
        
        if not moved:
            # Backtrack (Blue Dot)
            curr_r, curr_c = solve_stack.pop()
            bx, by = get_coords(curr_r, curr_c)
            t.goto(bx + CELL_SIZE/2, by + CELL_SIZE/2)
            t.dot(10, "blue")
            screen.update()

# --- EXECUTION ---
# 1. Generate dynamically
generate_maze(0, 0)

# 2. Bonus: Create a Cycle (Eat one extra random wall)
northWall[random.randint(1, R-2)][random.randint(1, C-2)] = 0
draw_maze()
screen.update()

# 3. Solve
solve_maze(0, 0, R-1, C-1)

turtle.done()