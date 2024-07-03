import tkinter as tk
    

colorMode = ""

def seguir():
    colorMode = "Seguir"


def auto():
    colorMode = "Auto"

root = tk.Tk()
root.geometry("450x450")

seguir = tk.Button(root, text="Seguir", command=seguir)
seguir.place(x=20, y=50)

auto = tk.Button(root, text="Auto", command=auto)
auto.place(x=20, y=100)

manual = tk.Button(root, text="Manual")
manual.place(x=20, y=150)
root.mainloop()