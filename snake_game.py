import tkinter as tk
import random

WIDTH = 520
HEIGHT = 520
SPACE = 20
SPEED = 110

BG_COLOR = "#0f172a"
HEAD_COLOR = "#22c55e"
BODY_COLOR = "#16a34a"
FOOD_COLOR = "#f43f5e"
TEXT_COLOR = "#e5e7eb"
GAMEOVER_COLOR = "#fb7185"
BUTTON_COLOR = "#334155"
BUTTON_HOVER = "#475569"

FONT_MAIN = ("Segoe UI", 14)
FONT_BIG = ("Segoe UI", 32, "bold")

window = tk.Tk()
window.title("Snake — Python Tkinter")
window.resizable(False, False)
window.configure(bg=BG_COLOR)

score = 0
direction = "right"
game_running = True

score_label = tk.Label(
    window, text="Score  0",
    fg=TEXT_COLOR, bg=BG_COLOR,
    font=FONT_MAIN
)
score_label.pack(pady=8)

canvas = tk.Canvas(
    window, width=WIDTH, height=HEIGHT,
    bg=BG_COLOR, highlightthickness=0
)
canvas.pack()

class Snake:
    def __init__(self):
        self.coordinates = [[100, 100], [80, 100], [60, 100]]
        self.squares = []
        for i, (x, y) in enumerate(self.coordinates):
            color = HEAD_COLOR if i == 0 else BODY_COLOR
            square = canvas.create_rectangle(
                x, y, x + SPACE, y + SPACE,
                fill=color, outline=""
            )
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(1, (WIDTH // SPACE) - 2) * SPACE
        y = random.randint(1, (HEIGHT // SPACE) - 2) * SPACE
        self.coordinates = [x, y]
        canvas.create_oval(
            x, y, x + SPACE, y + SPACE,
            fill=FOOD_COLOR, outline=""
        )

def draw_border():
    canvas.create_rectangle(
        SPACE, SPACE, WIDTH - SPACE, HEIGHT - SPACE,
        outline="#334155", width=2
    )

def next_turn():
    global game_running

    if not game_running:
        return

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE
    elif direction == "down":
        y += SPACE
    elif direction == "left":
        x -= SPACE
    elif direction == "right":
        x += SPACE

    snake.coordinates.insert(0, [x, y])
    square = canvas.create_rectangle(
        x, y, x + SPACE, y + SPACE,
        fill=HEAD_COLOR, outline=""
    )
    snake.squares.insert(0, square)
    canvas.itemconfig(snake.squares[1], fill=BODY_COLOR)

    if [x, y] == food.coordinates:
        global score
        score += 1
        score_label.config(text=f"Score  {score}")
        canvas.delete("all")
        draw_border()
        create_food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision():
        game_over()
    else:
        window.after(SPEED, next_turn)

def change_direction(new_dir):
    global direction
    opposite = {"up": "down", "down": "up", "left": "right", "right": "left"}
    if new_dir != opposite.get(direction):
        direction = new_dir

def check_collision():
    x, y = snake.coordinates[0]
    if x <= SPACE or x >= WIDTH - SPACE or y <= SPACE or y >= HEIGHT - SPACE:
        return True
    for body in snake.coordinates[1:]:
        if [x, y] == body:
            return True
    return False

def game_over():
    global game_running
    game_running = False
    canvas.delete("all")

    canvas.create_text(
        WIDTH / 2, HEIGHT / 2 - 30,
        text="GAME OVER",
        fill=GAMEOVER_COLOR,
        font=FONT_BIG
    )
    canvas.create_text(
        WIDTH / 2, HEIGHT / 2 + 10,
        text=f"Final Score  {score}",
        fill=TEXT_COLOR,
        font=FONT_MAIN
    )

    play_btn = tk.Button(
        window, text="Play Again",
        font=("Segoe UI", 12),
        bg=BUTTON_COLOR, fg=TEXT_COLOR,
        activebackground=BUTTON_HOVER,
        relief="flat", padx=16, pady=6,
        command=restart_game
    )
    canvas.create_window(WIDTH / 2, HEIGHT / 2 + 60, window=play_btn)

def restart_game():
    global snake, food, score, direction, game_running

    canvas.delete("all")
    score = 0
    direction = "right"
    game_running = True
    score_label.config(text="Score  0")

    draw_border()
    snake = Snake()
    create_food()
    next_turn()

def create_food():
    global food
    food = Food()


window.bind("<Up>", lambda e: change_direction("up"))
window.bind("<Down>", lambda e: change_direction("down"))
window.bind("<Left>", lambda e: change_direction("left"))
window.bind("<Right>", lambda e: change_direction("right"))


draw_border()
snake = Snake()
create_food()
next_turn()

window.mainloop()


  
