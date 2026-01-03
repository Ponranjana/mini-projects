import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Houra - Smart Digital Clock")
root.geometry("500x300")
root.resizable(False, False)

is_24_hour = True

def toggle_format():
    global is_24_hour
    is_24_hour = not is_24_hour

def get_greeting(hour):
    if 5 <= hour < 12:
        return "Good Morning 🌅"
    elif 12 <= hour < 17:
        return "Good Afternoon ☀️"
    elif 17 <= hour < 21:
        return "Good Evening 🌆"
    else:
        return "Good Night 🌙"

def get_theme(hour):
    if 5 <= hour < 12:
        return "#B3E5FC", "#000000"   # Morning
    elif 12 <= hour < 17:
        return "#FFF9C4", "#000000"   # Afternoon
    elif 17 <= hour < 21:
        return "#FFE0B2", "#000000"   # Evening
    else:
        return "#0D1B2A", "#FFFFFF"   # Night


def get_time_mirror(now):
    seconds_passed = now.hour * 3600 + now.minute * 60 + now.second
    total_seconds = 24 * 3600

    percentage = (seconds_passed / total_seconds) * 100
    remaining_seconds = total_seconds - seconds_passed

    rem_hours = remaining_seconds // 3600
    rem_minutes = (remaining_seconds % 3600) // 60

    return int(percentage), rem_hours, rem_minutes

def update_clock():
    now = datetime.now()
    hour = now.hour

    if is_24_hour:
        time_text = now.strftime("%H:%M:%S")
    else:
        time_text = now.strftime("%I:%M:%S %p")
    date_text = now.strftime("%A, %d %B %Y")

    greeting = get_greeting(hour)
    bg_color, fg_color = get_theme(hour)
    percent, rh, rm = get_time_mirror(now)

    root.config(bg=bg_color)
    time_label.config(text=time_text, bg=bg_color, fg=fg_color)
    greeting_label.config(text=greeting, bg=bg_color, fg=fg_color)
    mirror_label.config(
        text=f"You've used {percent}% of today\nRemaining: {rh}h {rm}m",
        bg=bg_color,
        fg=fg_color)
    date_label.config(text=date_text, bg=bg_color, fg=fg_color)


    root.after(1000, update_clock)

time_label = tk.Label(
    root,
    font=("Segoe UI", 40, "bold")
)
time_label.pack(pady=15)

date_label = tk.Label(
    root,
    font=("Segoe UI", 14)
)
date_label.pack()


greeting_label = tk.Label(
    root,
    font=("Segoe UI", 16)
)
greeting_label.pack()

mirror_label = tk.Label(
    root,
    font=("Segoe UI", 14)
)
mirror_label.pack(pady=10)

toggle_button = tk.Button(
    root,
    text="Switch 12H / 24H",
    font=("Segoe UI", 11),
    command=toggle_format
)
toggle_button.pack(pady=10)

update_clock()
root.mainloop()

