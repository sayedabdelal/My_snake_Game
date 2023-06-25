import curses
import random

# Initialize the screen
stdscr = curses.initscr()
curses.curs_set(0)  # Hide the cursor
stdscr.nodelay(1)  # Make getch() non-blocking

# Get the dimensions of the screen
height, width = stdscr.getmaxyx()

# Create a new window for the game
win = curses.newwin(height, width, 0, 0)
win.keypad(1)
win.timeout(125)

# Initialize the snake's initial position and direction
snake_x = width // 4
snake_y = height // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

# Initialize the food's position
food = [height // 2, width // 2]
win.addch(food[0], food[1], 'O')

# Initialize the initial direction of the snake
key = curses.KEY_RIGHT

# Draw the boundaries
win.border(0)

# Game loop
while True:
    next_key = win.getch()
    key = key if next_key == -1 else next_key

    # Calculate the next position of the snake's head
    new_head = [snake[0][0], snake[0][1]]
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    elif key == curses.KEY_UP:
        new_head[0] -= 1
    elif key == curses.KEY_LEFT:
        new_head[1] -= 1
    elif key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Insert the new head at the beginning of the snake list
    snake.insert(0, new_head)

    # Check if the snake has hit the boundaries or itself
    if (
        new_head[0] in [0, height - 1] or
        new_head[1] in [0, width - 1] or
        new_head in snake[1:]
    ):
        break

    # Check if the snake has eaten the food
    if snake[0] == food:
        # Generate new food position
        while True:
            new_food = [
                random.randint(1, height - 2),
                random.randint(1, width - 2)
            ]
            if new_food not in snake:
                break
        food = new_food
        win.addch(food[0], food[1], 'O')
    else:
        # Remove the tail of the snake
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    # Draw the snake
    win.addch(snake[0][0], snake[0][1], 'X')

# End the game
curses.endwin()
