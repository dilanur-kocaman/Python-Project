from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)

#Is_equal_to_label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

#Miles_label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

#Km_label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

#Km_result_label
km_result_label = Label(text=0)
km_result_label.grid(column=1, row=1)

#Miles_input
miles_input= Entry(width=10)
miles_input.grid(column=1, row=0)

#Button
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()