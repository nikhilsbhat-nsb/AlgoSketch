from tkinter import *
from tkinter import ttk
from bubblesort import bubble_sort, changeRun, bubble_sort_step
from quick_sort import quick_sort
import random

root = Tk()
root.title("AlgoSketch - An Algorithm Visualizer")
root.maxsize(900, 600)
root.config(bg='black')


# variables
selected_alg = StringVar()
data = []
pause = ''
play = ''
nextStep = ''
timeip = 0


def drawData(data, colorArrary):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 10
    spacing = 10
    normalization = [i/max(data) for i in data]
    for i, height in enumerate(normalization):
        # top left corner
        x0 = i * x_width + offset + spacing
        y0 = c_height - height*340
        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArrary[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()


def Generate():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []

    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data, ['red' for x in range(len(data))])


def startAlgorithm():
    global data, time
    time = speedScale.get()
    if not data:
        return
# choose the algorithm function to call based on drop down menu input
    if(algMenu.get() == 'Quick Sort'):
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
        drawData(data, ['red' for x in range(len(data))])

    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, time, speedScale.get())


def printNextStep():
    global nextStep
    bubble_sort_step(data, drawData)
    changeRun(True)


# frame/base layout
UI_frame = Frame(root, width=650, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=2, pady=2)

# bottom output screen
canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=2, pady=5)

# User interface

# first row
Label(UI_frame, text="Select \n Algorithm: ", bg='grey', font=8).grid(
    row=0, column=0, padx=1, pady=5, sticky=E)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=[
                       'Bubble Sort', 'Quick Sort', 'Merge Sort'], width=15)
algMenu.grid(row=0, column=1, padx=0, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=100, digits=2,
                   resolution=0.2, orient=HORIZONTAL, label="Select Delay(s)")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=startAlgorithm, bg="Red", width=10).grid(
    row=0, column=3, padx=5, pady=5, columnspan=2, sticky=N)


# Second Row
# Data size
sizeEntry = Scale(UI_frame, from_=3.0, to=25.0, resolution=1,
                  orient='horizontal', label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

# Min size
minEntry = Scale(UI_frame, from_=0.0, to=10.0, resolution=1,
                 orient='horizontal', label="Min Size")
minEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# Max size
maxEntry = Scale(UI_frame, from_=10.0, to=100.0, resolution=1,
                 orient='horizontal', label="Max Size")
maxEntry.grid(row=1, column=2, padx=5, pady=5, sticky=W)

Button(UI_frame, text="Generate", command=Generate, bg="steel blue",
       width=10, height=2).grid(row=1, column=3, padx=2, pady=2)
Button(UI_frame, text="Next Step", command=printNextStep, bg="green",
       width=10, height=2).grid(row=1, column=4, padx=2, pady=2)
root.mainloop()
