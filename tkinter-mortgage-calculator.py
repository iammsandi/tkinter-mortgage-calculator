from calendar import month
import tkinter as tk 
# define mortgage function  to run to run upon 
def submit():
    loan = int(entry_a.get())
    term = int(entry_b.get())
    rate = float(entry_c.get())
    down = int(entry_d.get())
    
    months = term *12
    rate_monthly = rate /100/12
    payment =(rate_monthly/(1-(1 + rate_monthly)**(- month)))* (loan - down)
    result = tk.Label(text = "R" + str(round(payment,2)))
    result.pack()
# Creating  a tkinter window (GUI)
window =tk.Tk()
# Create text and entry boxese
label_a = tk.Label(text= "please enter loan amount:")
label_a.pack()
entry_a = tk.Entry()
entry_a.pack()
label_b =tk.Label(text = "please enter loan term:")
label_b.pack()
entry_b = tk.Entry()
entry_b.pack()
label_a = tk.Label(text= "please enter loan amount:")
label_a.pack()
entry_a = tk.Entry()
entry_a.pack()
label_c = tk.Label(text = "please enter loan rate: ")
label_c.pack()
entry_c = tk.Entry()
entry_c.pack()
label_c = tk.Label(text = "please enter Down payment: ")
label_c.pack()
entry_c = tk.Entry()
entry_c.pack()
# create a sumit button 
Mybutton = tk.Button(window, text = "Submit ", width =10, command = submit )
Mybutton.pack()
# Run  the loop 
window.mainloop()
