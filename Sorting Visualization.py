import tkinter as tk
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Initialize Tkinter
root = tk.Tk()
root.title("Sorting Algorithms Visualizer")

# Initialize the mat graph
number_of_bars = 30
FPS = 60
arr = np.round(np.linspace(0, 1000, number_of_bars), 0)
np.random.shuffle(arr)

data_normalizer = mp.colors.Normalize()
cmap = plt.cm.viridis

fig, ax = plt.subplots()
bar_container = ax.bar(np.arange(0, len(arr), 1), arr, align="edge", width=0.8, color=cmap(data_normalizer(arr)))
text = ax.text(0.01, 0.95, "", transform=ax.transAxes, color="blue")
iteration = [0]

#init wave



# Function Defining

def reset_animation():
    if 'animation' in globals():
        animation.event_source.stop()
    np.random.shuffle(arr)
    for bar, h in zip(bar_container, arr):
        bar.set_height(h)
        
    iteration[0]=0
    canvas.draw()

def pause_animation():
    if 'animation' in globals():
        animation.event_source.stop()

###########################-Insertion sort-#####################################

def start_animation_insertion():
    global animation
    animation = FuncAnimation(fig, insertion_alg, frames=range(len(arr)), interval=50, repeat = False)
    canvas.draw()


def insertion_alg(i):
    global arr
    if i < len(arr):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
        for bar, h in zip(bar_container, arr):
            bar.set_height(h)
            bar.set_color(cmap(data_normalizer(h)))
        iteration[0] += 1
        text.set_text("iterations : {}".format(iteration[0]))
        canvas.draw()
    else:
        animation.event_source.stop()
        iteration[0]=0

##########################- Selection sort -###########################################

def start_animation_selection():
    global animation
    animation = FuncAnimation(fig, selection_alg, frames=range(len(arr)), interval=50, repeat = False)
    canvas.draw()

def selection_alg(frame):
    global arr
    i = frame
    n = len(arr)
    if i < n - 1:
        min_index = i
        min_val = arr[i]
        for j in range(i + 1, n):
            if arr[j] < min_val:
                min_val = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        for bar, h in zip(bar_container, arr):
            bar.set_height(h)
        iteration[0] += 1
        text.set_text("iterations : {}".format(iteration[0]))
        canvas.draw()
    else:
        animation.event_source.stop()
        iteration[0]=0

###################################- bubble sort -############################################
def start_animation_bubble():
    global animation
    animation = FuncAnimation(fig, bubble_alg, frames=range(len(arr)), interval=50, repeat = False)
    canvas.draw()

def bubble_alg(frame):
    global arr
    i = frame
    n = len(arr)
    if i < n - 1:
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        for bar, h in zip(bar_container, arr):
            bar.set_height(h)
        iteration[0] += 1
        text.set_text("iterations : {}".format(iteration[0]))
        canvas.draw()
    else:
        # Stop the animation when the sorting is complete
        animation.event_source.stop()
        iteration[0]=0

################################ - Quick Sort - ################################################


def quicksort(a, l, r):
    if l >= r:
        return
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[j], a[i] = a[i], a[j]
        yield a
    a[l], a[j]= a[j], a[l]
    yield a
    yield from quicksort(a, l, j-1)
    yield from quicksort(a, j + 1, r)

def quicksort_alg(A, bar, iteration):
        for bar, h in zip(bar, A):
            bar.set_height(h)
        iteration[0] += 1
        text.set_text("iterations : {}".format(iteration[0]))

def start_animation_quicksort():
    global animation
    animation = FuncAnimation(fig, quicksort_alg,fargs = (bar_container, iteration), frames=quicksort(arr, 0, number_of_bars - 1), interval=50, repeat = False, cache_frame_data=False)
    canvas.draw()

######################################## - Merge Sort -###############################################
    
def mergesort(A, start, end): 
    if end <= start: 
        return
    mid = start + ((end - start + 1) // 2) - 1  
    yield from mergesort(A, start, mid) 
    yield from mergesort(A, mid + 1, end) 
    yield from merge(A, start, mid, end) 
  
def merge(A, start, mid, end): 
    merged = [] 
    leftIdx = start 
    rightIdx = mid + 1
    while leftIdx <= mid and rightIdx <= end: 
        if A[leftIdx] < A[rightIdx]: 
            merged.append(A[leftIdx]) 
            leftIdx += 1
        else: 
            merged.append(A[rightIdx]) 
            rightIdx += 1
    while leftIdx <= mid: 
        merged.append(A[leftIdx]) 
        leftIdx += 1
    while rightIdx <= end: 
        merged.append(A[rightIdx]) 
        rightIdx += 1
    for i in range(len(merged)): 
        A[start + i] = merged[i] 
        yield A 

def merge_alg(A, bar, iteration): 
        for bar, h in zip(bar, A):  
            bar.set_height(h) 
        iteration[0] += 1
        text.set_text("iterations : {}".format(iteration[0])) 
      
def start_animation_merge():
    global animation
    animation = FuncAnimation(fig, func= merge_alg, fargs=(bar_container, iteration), frames=mergesort(arr, 0, len(arr)-1), interval=50, repeat=False)
    canvas.draw()
     

# Tkinter Application
canvas_frame = tk.Frame(root)
canvas_frame.grid(row=0, column=0, sticky="nsew")
root.columnconfigure(0, weight=3)
canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")
canvas_frame.rowconfigure(0, weight=1)
canvas_frame.columnconfigure(0, weight=3)

toolbar_frame = tk.Frame(root)
toolbar_frame.grid(row=0, column=1, sticky="ns")


tk.Label(toolbar_frame, text="Sorting Algorithms").grid(row=0, column=0, columnspan=2, pady=5)
tk.Button(toolbar_frame, text="Selection Sort", command=start_animation_selection).grid(row=1, column=0, columnspan=2, pady=5)
tk.Button(toolbar_frame, text="Bubble sort", command=start_animation_bubble).grid(row=2, column=0, columnspan=2, pady=5)
tk.Button(toolbar_frame, text="Insertion sort", command=start_animation_insertion).grid(row=3, column=0, columnspan=2, pady=5)
tk.Button(toolbar_frame, text="Quick sort", command=start_animation_quicksort ).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(toolbar_frame, text="Merge sort", command=start_animation_merge ).grid(row=5, column=0, columnspan=2, pady=5)
tk.Label(toolbar_frame, text="Animation Control").grid(row=6, column=0, columnspan=2, pady=5)
tk.Button(toolbar_frame, text="Pause", command=pause_animation).grid(row=7, column=0, pady=5)
tk.Button(toolbar_frame, text="Reset", command=reset_animation).grid(row=7, column=1, pady=5)




root.mainloop()


