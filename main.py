from tkinter import Tk, Button, Label, DoubleVar, Entry

window = Tk()
window.title("Convertidor de pies a metros")
window.configure(background="light pink")
window.geometry("320x220")
window.resizable(width=True, height=True)

ft_lbl = Label(window,text="Pies", bg="light blue", fg="white", width=14)
ft_lbl.grid(column=0, row=0, padx=15, pady=15)

ft_value = DoubleVar()
ft_entry = Entry(window, textvariable=ft_value, width=14)
ft_entry.grid(column=1, row=0)
ft_entry.delete(0, 'end')

window.mainloop()