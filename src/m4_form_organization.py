import tkinter as tk
###############################################################################
# TODO: 1. (5 pts)
#
#   For this _todo_, copy your code from your fillable form from Session 18 and
#   paste it below.
#
#   Now, use the geometry managers we have learned about and reorganize/
#   reformat your fillable form. You must use more than just the pack() method,
#   but you can still use it if it is what you need in a certain spot.
#
#   You may need to add more frames and such to move things around effectively.
#
#   Feel free to be creative on how you want your form to look.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window=tk.Tk()
window.title("Costum Widgets")

f1 = tk.Frame(window, bg="red", padx=5, pady=5)
f2 = tk.Frame(window, bg="yellow", padx=5, pady=5)
f3 = tk.Frame(window, bg="blue", padx=5, pady=5)
f4 = tk.Frame(window, bg="purple", padx=5, pady=5)
f5 = tk.Frame(window, bg="green", padx=5, pady=5)

f1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
f2.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
f3.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
f4.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
f5.grid(row=4, column=4, padx=5, pady=5, sticky="nsew")

window.rowconfigure([0, 1, 2, 3, 4, 5], weight=1)
window.columnconfigure([0, 1, 2, 3, 4, 5], weight=1)

l1 = tk.Label(f1, text="Name", bg="red")
l2 = tk.Label(f2, text="Address Line 1", bg="yellow")
l3 = tk.Label(f3, text="Address Line 2", bg="blue")
l4 = tk.Label(f4, text="City", bg="purple")
l5 = tk.Label(f5, text="State", bg="green")

l1.pack()
l2.pack()
l3.pack()
l4.pack()
l5.pack()

entry1=tk.Entry(f1)
entry1.pack()
entry1=tk.Entry(f2)
entry1.pack()
entry1=tk.Entry(f3)
entry1.pack()
entry1=tk.Entry(f4)
entry1.pack()
entry1=tk.Entry(f5)
entry1.pack()

window.mainloop()

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