import tkinter as tk
import numpy as np

def solve_equations():
    first_eqn = text_eqn1.get().split()
    second_eqn = text_eqn2.get().split()

    # Extract the RHS values and convert to float
    try:
        val_1 = float(first_eqn[-1])
        val_2 = float(second_eqn[-1])
    except ValueError:
        print("Error: RHS values must be numeric.")
        return

    a, b = [], []

    # Improved digit check to handle negatives and decimals
    for val in first_eqn[:-1]:  # Skip RHS
        try:
            a.append(float(val))
        except ValueError:
            continue

    for val in second_eqn[:-1]:  # Skip RHS
        try:
            b.append(float(val))
        except ValueError:
            continue

    if len(a) < 2 or len(b) < 2:
        print("Error: Not enough coefficients found.")
        return

    A = np.array([[a[0], a[1]], [b[0], b[1]]])
    B = np.array([val_1, val_2])

    try:
        ans = np.linalg.solve(A, B)
        print("Solution:", ans)
    except np.linalg.LinAlgError:
        print("Error: Equations may be inconsistent or dependent.")
    
    anwers = tk.Label(frame1, text = "x = %.3f and y = %.3f"%(ans[0], ans[1]), height=4, width = 30)
    anwers.grid(row = 3, column=0)
    
window = tk.Tk()
window.title("Linear equation")
window.geometry("700x600")

frame1 = tk.Frame(bg = "yellow", padx = 12, pady = 10)
frame1.pack(anchor="n", fill=tk.X)

equation_1 = tk.Label(frame1, text="first equation : ")
equation_1.grid(row = 0, column= 0, pady = 2)

equation_2 = tk.Label(frame1, text="second equation : ")
equation_2.grid(row = 1, column= 0, pady = 2)

text_eqn1 = tk.StringVar()
text_eqn2 = tk.StringVar()

enter_equation_1 = tk.Entry(frame1, textvariable=text_eqn1)
enter_equation_1.grid(row = 0, column= 1, pady=2)

enter_equation_2 = tk.Entry(frame1, textvariable=text_eqn2)
enter_equation_2.grid(row = 1, column= 1, pady=2)

calculate_equations = tk.Button(frame1, text="Calculate", command=solve_equations)
calculate_equations.grid(row=2, column=1)

window.mainloop()