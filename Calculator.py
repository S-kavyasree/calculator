import tkinter as tk
import math
import re

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("360x500")
root.configure(bg="white")
root.resizable(False, False)

expr = tk.StringVar()


screen = tk.Entry(
    root,
    textvariable=expr,
    font=("Segoe UI", 18),
    bd=4,
    relief="sunken",
    justify="right"
)
screen.grid(row=0, column=0, columnspan=4, padx=8, pady=10, ipady=10, sticky="nsew")



def press(x):
    expr.set(expr.get() + x)

def clear_all():
    expr.set("")

def delete_one():
    expr.set(expr.get()[:-1])

def factorial(n):
    return math.factorial(int(n))

def nCr(n, r):
    return math.comb(int(n), int(r))

def nPr(n, r):
    return math.perm(int(n), int(r))


def calculate():
    try:
        e = expr.get()

        e = e.replace("^", "**")

        e = re.sub(r'sin(\d+\.?\d*)', r'math.sin(\1)', e)
        e = re.sub(r'cos(\d+\.?\d*)', r'math.cos(\1)', e)
        e = re.sub(r'tan(\d+\.?\d*)', r'math.tan(\1)', e)

        e = e.replace("sin(", "math.sin(")
        e = e.replace("cos(", "math.cos(")
        e = e.replace("tan(", "math.tan(")
        e = e.replace("log(", "math.log10(")
        e = e.replace("ln(", "math.log(")
        e = e.replace("√(", "math.sqrt(")

        e = e.replace("π", "math.pi")
        e = e.replace("e", "math.e")

        e = re.sub(r'(\d+)!', r'factorial(\1)', e)

        e = re.sub(r'(\d+)\s*nCr\s*(\d+)', r'nCr(\1,\2)', e)
        e = re.sub(r'(\d+)\s*nPr\s*(\d+)', r'nPr(\1,\2)', e)

        result = eval(e, {
            "math": math,
            "factorial": factorial,
            "nCr": nCr,
            "nPr": nPr
        })

        expr.set(str(result))
    except:
        expr.set("Error")




btn = {
    "bg": "#f4fefe",
    "fg": "black",
    "font": ("Segoe UI", 10),
    "width": 5,
    "height": 2,
    "relief": "raised"
}


layout = [
    ["sin", "cos", "tan", "AC"],
    ["log(", "ln(", "√(", "DEL"],
    ["x!", "x²", "π", "e"],

    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]



for r in range(len(layout)):
    for c in range(4):
        t = layout[r][c]

        def make_cmd(x=t):
            if x == "AC":
                return clear_all
            elif x == "DEL":
                return delete_one
            elif x == "=":
                return calculate
            elif x == "x!":
                return lambda: press("!")
            elif x == "x²":
                return lambda: press("^2")
            elif x in ["sin", "cos", "tan"]:
                return lambda: press(x)
            else:
                return lambda: press(x)

        b = tk.Button(root, text=t, command=make_cmd(), **btn)
        b.grid(row=r+1, column=c, padx=4, pady=4, sticky="nsew")

root.mainloop()





