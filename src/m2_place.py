import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# TODO: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# TODO: 2. (4 pts)
#
#   Now, create one frame dimensions 200 by 200.
#
#   Use the default pack() method to place it in the window.
#
#   Also, place 3 labels in the frame labeling them as Label A, Label B, and
#   Label C and give them different background colors.
#
#   Use the place() method to place each of these labels at different
#   coordinates such that they do not overlap.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
###############################################################################

#window=tk.Tk()

#frame1=tk.Frame(master=window, width=100, height=100, bg="red")
#frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

#frame2=tk.Frame(master=window, width=50, height=50, bg="yellow")
#frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

#frame3=tk.Frame(master=window, width=25, height=25, bg="blue")
#frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

#frame=tk.Frame(master=window, width=150, height=150)
#frame.pack()

#label1=tk.Label(master=frame, text="I'm at (0,0)", bg="red")
#label1.place(x=0, y=0)

#label2=tk.Label(master=frame, text="I'm at (65,75)", bg="yellow")
#label2.place(x=65, y=75)

#for i in range(3):
#    window.columnconfigure(i, weight=1, minsize=75)
#    window.rowconfigure(i, weight=1, minsize=50)

#    for j in range(3):
#        frame=tk.Frame(
#            master=window,
#            relief=tk.RAISED,
#            borderwidth=1
#        )
#        frame.grid(row=i, column=j, padx=5, pady=5)
#        label=tk.Label(master=frame, text=f"Row {i}\nColumn{j}")
#        label.pack()

#window.rowconfigure(0,weight=1, minsize=50)
#window.columnconfigure([0, 1, 2, 3], weight=1, minsize=50)

#label1=tk.Label(text="1", bg="black", fg="white")
#label2=tk.Label(text="2", bg="black", fg="white")
#label3=tk.Label(text="3", bg="black", fg="white")
#label4=tk.Label(text="4", bg="black", fg="white")

#label1.grid(row=0, column=0)
#label2.grid(row=0, column=1, sticky="ew")
#label3.grid(row=0, column=2, sticky="ns")
#label4.grid(row=0, column=3, sticky="nsew")

#window.mainloop()