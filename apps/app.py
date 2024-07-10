import tkinter as tk
import threading
import constants as const
import recognitioncv
import esp32serial


def rgb_to_hex(emotions):
    return '#{:02x}{:02x}{:02x}'.format(emotions['r'], emotions['g'], emotions['b'],)

MAX_PEOPLE = 1

colorMode = ""

def seguir():
    global colorMode
    colorMode = "Seguir"
    mode.config(text="Seguir")


def manual():
    global colorMode
    colorMode = "Manual"
    mode.config(text="Manual")


def add():
    global colorMode
    colorMode = "Add"
    mode.config(text="Add")


root = tk.Tk()
root.geometry(const.Janela.TAMANHO)
root.resizable(False, False)
root.configure(bg=const.Janela.BACKGROUND_COLOR)
root.title(const.Janela.TITULO)
icon = tk.PhotoImage(file=const.Janela.CAMINHO_ICON)
root.iconphoto(True, icon)

view_image = tk.PhotoImage(file=const.View.CAMINHO)
viewcolor = tk.Canvas( root, width = const.View.TAMANHO[const.X], 
                 height = const.View.TAMANHO[const.Y], 
                 background=const.Janela.BACKGROUND_COLOR, highlightthickness=0)

viewcolor.pack(side=tk.BOTTOM)
viewcolor.create_image(const.View.POSICAO[const.X], const.View.POSICAO[const.Y], 
                       image=view_image, anchor="nw")
color = viewcolor.create_oval(const.Circle.circle[const.X], const.Circle.circle[const.Y], 
                              const.Circle.circle[const.XF], const.Circle.circle[const.YF], 
                              fill=const.Circle.color)

select_image = tk.PhotoImage(file=r"C:\Users\enzoc\Documents\FRProject\apps\imagens\select.png")
select = tk.Canvas(root, width = 400, 
                 height = 200, background="#E6E2D6", highlightthickness=0)
select.create_image(200, 100, image=select_image)
select.pack(side=tk.BOTTOM)

follow_image = tk.PhotoImage(file=r"C:\Users\enzoc\Documents\FRProject\apps\imagens\follower.png")
follow = tk.Button(root, image=follow_image, highlightthickness=0, bd=0, background="#FFAA39", 
                   command=seguir)
follow.place(x=270, y=145)

manual_image = tk.PhotoImage(file=r"C:\Users\enzoc\Documents\FRProject\apps\imagens\manual.png")
manualButton = tk.Button(root, image=manual_image, highlightthickness=0, bd=0, background="#FFAA39",
                   command=manual)
manualButton.place(x=270, y=196)

add_image = tk.PhotoImage(file=r"C:\Users\enzoc\Documents\FRProject\apps\imagens\add.png")
addButton = tk.Button(root, image=add_image, highlightthickness=0, bd=0, background="#FFAA39",
                      command=add)
addButton.place(x=270, y=247)

mode = tk.Label(root, text="None", fg="#FFAA39", font=("Roboto", 20), bg="#E6E2D6")
mode.place(x=150, y=50)

def sendColorToESP():
    while True:
        emotions = recognitioncv.getcount_emotions()
        esp32serial.sendmessage(equation(emotions=emotions, mode=colorMode))


def equation(emotions, mode):
    if mode.lower() == "seguir" and MAX_PEOPLE == 1:
        if emotions['angry'] == 1:
            emotions['r'] = 255
            emotions['g'] = 0
            emotions['b'] = 0
        elif emotions['sad'] == 1:
            emotions['r'] = 255
            emotions['g'] = 255
            emotions['b'] = 0
        elif emotions['neutral'] == 1:
            emotions['r'] =  255
            emotions['g'] = 0
            emotions['b'] = 255
        elif emotions['happy'] == 1:
            emotions['r'] = 0
            emotions['g'] = 255
            emotions['b'] = 0
        elif emotions['fatigue'] == 1:
            emotions['r'] = 0
            emotions['g'] = 0
            emotions ['b'] = 255
    elif mode.lower() == "add":
        emotions['r'] = (int)(220 + ((emotions['angry'] + emotions['sad']) * (35/MAX_PEOPLE)))
        emotions['g'] = (int)(220 + ((emotions['neutral'] + emotions['happy']) * (35/MAX_PEOPLE)))
        emotions['b'] = (int)(220 + (emotions['fatigue'] * (35/MAX_PEOPLE)))
    global viewcolor
    viewcolor.itemconfig(color, fill=rgb_to_hex(emotions))
    return emotions

getExpressionThread = threading.Thread(target=recognitioncv.getRecog, daemon=True)
getExpressionThread.start()

sendColorToESPThread = threading.Thread(target=sendColorToESP, daemon=True)
sendColorToESPThread.start()

root.mainloop()