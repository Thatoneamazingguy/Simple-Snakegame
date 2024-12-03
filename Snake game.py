import curses
import random
import time

# Initialize the screen
screen = curses.initscr()
curses.curs_set(0)  # Hide the cursor
sh, sw = screen.getmaxyx()  # Get the height and width of the window
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)  # Enable keypad mode
w.timeout(100)  # Refresh every 100 milliseconds

# Initial snake position and body
snake_x = sw // 4
snake_y = sh // 2
snake_body = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

# Direction of the snake
key = curses.KEY_RIGHT

# Initial food position
food = [sh // 2, sw // 2]
w.addch(food[0], food[1], curses.ACS_PI)

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key  # Change direction with arrow keys

    # Get the new head of the snake
    new_head = [snake_body[0][0], snake_body[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Insert the new head to the beginning of the snake body
    snake_body.insert(0, new_head)

    # Check for collisions with food or boundaries
    if (snake_body[0][0] in [0, sh]) or \
       (snake_body[0][1] in [0, sw]) or \
       (snake_body[0] in snake_body[1:]):
        curses.endwin()
        quit()

    # Check if the snake has eaten the food
    if snake_body[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh - 1),
                random.randint(1, sw - 1)
            ]
            food = nf if nf not in snake_body else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake_body.pop()
        w.addch(tail[0], tail[1], ' ')

    # Draw the new head of the snake
    w.addch(snake_body[0][0], snake_body[0][1], curses.ACS_CKBOARD)
