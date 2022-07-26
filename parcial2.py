#!/usr/bin/env python3
from tkinter import Tk, Label, Entry, Frame, Canvas, Button, CENTER, BOTH

BASE = 740
ALTURA = 500


def calcular_pendiente():
    valor_x1 = int(input_x1.get())
    valor_y1 = int(input_y1.get())
    valor_x2 = int(input_x2.get())
    valor_y2 = int(input_y2.get())
    pendiente = str((valor_y2 - valor_y1) / (valor_x2 - valor_x1))
    label_pendiente.config(text="Pendiente: " + pendiente)
    return pendiente


def graficar_recta():
    global recta
    canvas_principal.delete(recta)
    valor_x1 = int(input_x1.get())
    valor_y1 = int(input_y1.get())
    valor_x2 = int(input_x2.get())
    valor_y2 = int(input_y2.get())
    recta = canvas_principal.create_line(
        (BASE / 2) + valor_x1,
        (ALTURA / 2) + valor_y1 * -1,
        (BASE / 2) + valor_x2,
        (ALTURA / 2) + valor_y2 * -1,
        fill="red",
        width=5,
    )
    return recta


ventana_principal = Tk()
ventana_principal.geometry("1280x720")
ventana_principal.configure(background="blue")
ventana_principal.resizable(False, False)
ventana_principal.minsize(1280, 720)
ventana_principal.maxsize(1280, 720)

frame_principal = Frame(ventana_principal)
frame_principal.config(background="gray", width=1260, height=700)
frame_principal.place(x=10, y=10)

canvas_principal = Canvas(frame_principal)
canvas_principal.config(background="white", width=BASE, height=ALTURA)
canvas_principal.place(x=0, y=0, relx=0.5, rely=0.4, anchor=CENTER)

label_x1 = Label(text="X1")
label_x1.config(bg="#FAFAFA")
label_x1.place(x=300, y=580)
input_x1 = Entry(frame_principal)
input_x1.place(x=300, y=600)

label_y1 = Label(text="Y1")
label_y1.config(bg="#FAFAFA")
label_y1.place(x=480, y=580)
input_y1 = Entry(frame_principal)
input_y1.place(x=480, y=600)

label_x2 = Label(text="X2")
label_x2.config(bg="#FAFAFA")
label_x2.place(x=820, y=580)
input_x2 = Entry(frame_principal)
input_x2.place(x=820, y=600)

label_y2 = Label(text="Y2")
label_y2.config(bg="#FAFAFA")
label_y2.place(x=1000, y=580)
input_y2 = Entry(frame_principal)
input_y2.place(x=1000, y=600)

boton_graficar = Button(
    frame_principal,
    text="Graficar",
    background="white",
    highlightthickness=3,
    borderwidth=2,
    bd=2,
    command=graficar_recta,
)
boton_graficar.place(x=680, y=580)

boton_calcular = Button(
    frame_principal,
    text="Calcular pendiente",
    background="white",
    highlightthickness=3,
    borderwidth=2,
    bd=2,
    command=calcular_pendiente,
)
boton_calcular.place(x=660, y=630)

label_pendiente = Label(text="Pendiente: ")
label_pendiente.config(bg="#FAFAFA")
label_pendiente.place(x=350, y=680)

ejex = canvas_principal.create_line(
    0, ALTURA / 2, BASE, ALTURA / 2, fill="black", width=3, arrow=BOTH
)
ejey = canvas_principal.create_line(
    BASE / 2, 0, BASE / 2, ALTURA, fill="black", width=3, arrow=BOTH
)
recta = canvas_principal.create_line(0, 0, 0, 0)

ventana_principal.mainloop()
