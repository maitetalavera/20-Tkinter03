import tkinter as tk
###############################################################################
# DONE: 1. (5 pts)
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
f3 = tk.Frame(window, bg="yellow", padx=5, pady=5)
f4 = tk.Frame(window, bg="purple", padx=5, pady=5)
f5 = tk.Frame(window, bg="green", padx=5, pady=5)
f6 = tk.Frame(window, bg="blue", padx=5, pady=5)
f7 = tk.Frame(window, bg="red", padx=5, pady=5)
f8 = tk.Frame(window, bg="red", padx=5, pady=5)

f1.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
f2.grid(row=1, column=0, padx=5, pady=5)
f3.grid(row=2, column=0, padx=5, pady=5)
f4.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
f5.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
f6.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
f7.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")
f8.grid(row=7, column=0, padx=5, pady=5, sticky="nsew")

window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8], weight=1)
window.columnconfigure(0, weight=1)

l1 = tk.Label(f1, text="Name", bg="red")
l2 = tk.Label(f2, text="Address Line 1", bg="yellow")
l3 = tk.Label(f3, text="Address Line 2", bg="yellow")
l4 = tk.Label(f4, text="City", bg="purple")
l5 = tk.Label(f5, text="State", bg="green")
l6 = tk.Label(f6, text="Zip Code", bg="blue")
l7 = tk.Label(f7, text="Phone Number", bg="red")
l8 = tk.Label(f8, text="Email Address", bg="red")

l1.pack()
l2.pack()
l3.pack()
l4.pack()
l5.pack()
l6.pack()
l7.pack()
l8.pack()


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
entry1=tk.Entry(f6)
entry1.pack()
entry1=tk.Entry(f7)
entry1.pack()
entry1=tk.Entry(f8)
entry1.pack()

window.mainloop()
