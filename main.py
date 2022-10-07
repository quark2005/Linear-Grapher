import tkinter as tk

root = tk.Tk()
root.geometry("900x500")
root.resizable(False, False)

lineFunc = []
lineInfo = []

def ClearGraph():
    canvas.delete("graph")

def GetLine():
    lineFunc.clear()
    try:
        grad = int(gradientInp.get())
        yInt = int(yICInp.get())
    except ValueError:
        tk.Label(text="Must Be Integers!").grid(column=1, row=2)

    DrawLine(grad, yInt)

def DrawLine(grad, yInt):

    if grad > 0:
        x1 = 100 - (100/grad)
        y1 = 200 - (yInt * 10)

        x2 = 100 + (100/grad)
        y2 = -1 * (yInt * 10)

        while y1 < 200 and x1 > 0:
            y1 += grad
            x1 -= 1
        while y2 > 0 and x2 < 200:
            y2 -= grad
            x2 += 1
        while y1 > 200:
            y1 -= grad
            x1 += 1

    elif grad == 0:
        x1 = 0
        x2 = 200
        y1 = 100 - (yInt * 10)
        y2 = 100 - (yInt * 10)

    elif grad < 0:
        _grad = grad * -1
        x1 = 100 - (100 / _grad)
        y1 =  -1 * (yInt * 10)

        x2 = 100 + (100 / _grad)
        y2 = 200 - (yInt * 10)

        while y1 < 200 and x1 > 0:
            y1 += grad
            x1 -= 1
        while y2 > 0 and x2 < 200:
            y2 -= grad
            x2 += 1
        while y2 > 200:
            y2 += grad
            x2 -= 1


    canvas.create_line(x1, y1, x2, y2, dash=(2, 2), tags="graph")
    canvas.grid(column=4)


tk.Label(text="Enter Gradient").grid(row=0, column=0)
gradientInp = tk.Entry(root)
gradientInp.grid(row=0, column=1)

tk.Label(text="Enter Y Intercept").grid(row=1, column=0)
yICInp = tk.Entry(root)
yICInp.grid(row=1, column=1)

printButton = tk.Button(root, text = "ENTER", command = GetLine)
printButton.grid(row=3)

clearButton = tk.Button(root, text = "CLEAR", command = ClearGraph)
clearButton.grid(row=3, column=1)

tk.Label(text="Axis from 10 to -10").grid(row=3, column = 2)


"""
    GRID AXIS 
            TOP LEFT -> 0, 0         X AXIS at Y = 100
           TOP RIGHT -> 200, 0       Y AXIS at X = 100
         BOTTOM LEFT -> 0, 200
        BOTTOM RIGHT -> 200, 200
"""

canvas = tk.Canvas(root)
canvas.create_line(100, 0, 100, 200)
canvas.create_line(0, 100, 200, 100)

canvas.grid(column=4)

root.mainloop()
