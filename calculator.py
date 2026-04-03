# calculator.py
# A simple + scientific calculator using tkinter (Python's built-in UI library)

import tkinter as tk   # tkinter comes with Python — no installation needed!
import math            # math gives us sqrt, power etc.

# ══════════════════════════════════════════
# THE BRAIN — all calculation logic here
# ══════════════════════════════════════════

current_input = ""     # what the user is currently typing
full_expression = ""   # the full equation shown above (like "23.5 + 10")

def update_display():
    """Refresh what's shown on screen"""
    display_result.config(text=current_input if current_input else "0")
    display_expression.config(text=full_expression)

def button_click(value):
    """Called every time a number or operator button is pressed"""
    global current_input
    current_input += str(value)   # add the button value to current input
    update_display()

def clear():
    """AC button — wipe everything"""
    global current_input, full_expression
    current_input = ""
    full_expression = ""
    update_display()

def calculate():
    """= button — evaluate the expression"""
    global current_input, full_expression
    try:
        full_expression = current_input          # show the equation on top
        result = eval(current_input)             # eval() solves the math string
        current_input = str(round(result, 10))   # round to avoid float weirdness
        update_display()
    except:
        current_input = "Error"                  # if something goes wrong
        update_display()

def toggle_sign():
    """+/- button — make positive number negative or vice versa"""
    global current_input
    if current_input and current_input != "0":
        if current_input.startswith("-"):
            current_input = current_input[1:]    # remove the minus sign
        else:
            current_input = "-" + current_input  # add a minus sign
        update_display()

# ══════════════════════════════════════════
# SCIENTIFIC FUNCTIONS
# ══════════════════════════════════════════

def square_root():
    global current_input, full_expression
    try:
        full_expression = f"√({current_input})"
        result = math.sqrt(float(current_input))
        current_input = str(round(result, 10))
        update_display()
    except:
        current_input = "Error"
        update_display()

def square():
    global current_input, full_expression
    try:
        full_expression = f"({current_input})²"
        result = float(current_input) ** 2       # ** means "to the power of"
        current_input = str(round(result, 10))
        update_display()
    except:
        current_input = "Error"
        update_display()

def reciprocal():
    global current_input, full_expression
    try:
        full_expression = f"1/({current_input})"
        result = 1 / float(current_input)
        current_input = str(round(result, 10))
        update_display()
    except:
        current_input = "Error"
        update_display()

def percentage():
    global current_input, full_expression
    try:
        full_expression = f"({current_input})%"
        result = float(current_input) / 100
        current_input = str(round(result, 10))
        update_display()
    except:
        current_input = "Error"
        update_display()

# ══════════════════════════════════════════
# THE FACE — building the UI with tkinter
# ══════════════════════════════════════════

window = tk.Tk()                          # create the main window
window.title("Calculator")                # window title bar text
window.resizable(False, False)            # user cannot resize the window
window.configure(bg="#1c1c1e")           # dark background color

# ── Display area ──────────────────────────
display_frame = tk.Frame(window, bg="#1c1c1e")
display_frame.pack(fill="both", padx=16, pady=(16, 8))

# Small expression text (shows "23.5 + 10" above result)
display_expression = tk.Label(
    display_frame, text="", font=("Arial", 13),
    bg="#1c1c1e", fg="#888888", anchor="e"
)
display_expression.pack(fill="x")

# Big result number
display_result = tk.Label(
    display_frame, text="0", font=("Arial", 40, "bold"),
    bg="#1c1c1e", fg="white", anchor="e"
)
display_result.pack(fill="x")

# ── Button layout ─────────────────────────
btn_frame = tk.Frame(window, bg="#1c1c1e")
btn_frame.pack(padx=16, pady=(0, 16))

def make_btn(parent, text, cmd, bg, fg, colspan=1):
    """Helper function — creates one button so we don't repeat styling"""
    btn = tk.Button(
        parent, text=text, command=cmd,
        font=("Arial", 16), bg=bg, fg=fg,
        activebackground=fg, activeforeground=bg,
        relief="flat", bd=0, cursor="hand2",
        width=4 * colspan, height=2
    )
    return btn

# Color scheme
C_NUM  = "#2c2c2e"   # number buttons (dark gray)
C_OP   = "#ff9f0a"   # operator buttons (orange)
C_ACT  = "#636366"   # action buttons (medium gray)
C_EQ   = "#30d158"   # equals button (green)
C_RED  = "#ff453a"   # clear button (red)

# Row 1 — AC, +/-, operators
r1 = tk.Frame(btn_frame, bg="#1c1c1e"); r1.pack(pady=3)
make_btn(r1, "AC",  clear,                    C_RED,  "white", 2).pack(side="left", padx=3)
make_btn(r1, "+/-", toggle_sign,              C_ACT,  "white").pack(side="left", padx=3)
make_btn(r1, "÷",   lambda: button_click("/"), C_OP,  "#1c1c1e").pack(side="left", padx=3)

# Row 2 — 7, 8, 9, ×
r2 = tk.Frame(btn_frame, bg="#1c1c1e"); r2.pack(pady=3)
for num in ["7", "8", "9"]:
    make_btn(r2, num, lambda n=num: button_click(n), C_NUM, "white").pack(side="left", padx=3)
make_btn(r2, "×", lambda: button_click("*"), C_OP, "#1c1c1e").pack(side="left", padx=3)

# Row 3 — 4, 5, 6, -
r3 = tk.Frame(btn_frame, bg="#1c1c1e"); r3.pack(pady=3)
for num in ["4", "5", "6"]:
    make_btn(r3, num, lambda n=num: button_click(n), C_NUM, "white").pack(side="left", padx=3)
make_btn(r3, "-", lambda: button_click("-"), C_OP, "#1c1c1e").pack(side="left", padx=3)

# Row 4 — 1, 2, 3, +
r4 = tk.Frame(btn_frame, bg="#1c1c1e"); r4.pack(pady=3)
for num in ["1", "2", "3"]:
    make_btn(r4, num, lambda n=num: button_click(n), C_NUM, "white").pack(side="left", padx=3)
make_btn(r4, "+", lambda: button_click("+"), C_OP, "#1c1c1e").pack(side="left", padx=3)

# Row 5 — 0, ., =
r5 = tk.Frame(btn_frame, bg="#1c1c1e"); r5.pack(pady=3)
make_btn(r5, "0", lambda: button_click("0"), C_NUM, "white", 2).pack(side="left", padx=3)
make_btn(r5, ".", lambda: button_click("."), C_NUM, "white").pack(side="left", padx=3)
make_btn(r5, "=", calculate,                 C_EQ,  "#1c1c1e").pack(side="left", padx=3)

# Row 6 — Scientific buttons
sep = tk.Frame(btn_frame, bg="#333333", height=1); sep.pack(fill="x", pady=8)
r6 = tk.Frame(btn_frame, bg="#1c1c1e"); r6.pack(pady=3)
make_btn(r6, "√",   square_root, C_ACT, "white").pack(side="left", padx=3)
make_btn(r6, "x²",  square,      C_ACT, "white").pack(side="left", padx=3)
make_btn(r6, "1/x", reciprocal,  C_ACT, "white").pack(side="left", padx=3)
make_btn(r6, "%",   percentage,  C_ACT, "white").pack(side="left", padx=3)

# ── Start the app ─────────────────────────
window.mainloop()   # this line keeps the window open and listening for clicks