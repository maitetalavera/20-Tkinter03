import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (5 pts)
#
#   Now, create two frames in your window.
#
#   Use the grid() method to place them in the window side by side to each
#   other. Both frames should have 5px of padding in all directions.
#
#   Use the configure methods to make these columns and row responsive in all
#   directions. Choose minimum sizes that make sense (no text should be cut
#   off) but the two columns should both have equal weight (so they remain the
#   same relative size to each other).
#
#   Also, place a label in each frame labeling them as Frame A and Frame B and
#   give them different background colors.
#
#   Use the pack() method simply put the label in each frame.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
###############################################################################


window = tk.Tk()

f1 = tk.Frame(window, bg="red", padx=5, pady=5)
f2 = tk.Frame(window, bg="yellow", padx=5, pady=5)

f1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
f2.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

l1 = tk.Label(f1, text="Frame A", bg="red")
l2 = tk.Label(f2, text="Frame B", bg="yellow")

l1.pack()
l2.pack()

window.mainloop()
