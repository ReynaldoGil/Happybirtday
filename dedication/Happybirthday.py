import turtle
import random
import pygame

# Inicializa pygame y carga la música
pygame.init()
pygame.mixer.music.load('happybirthdaysong.mp3')
pygame.mixer.music.play(-1)  # -1 significa que la canción se reproducirá en bucle

#establecer fondo de pantalla
bg = turtle.Screen()
bg.bgcolor("black")

#empezar a dibujar
turtle.penup()
turtle.goto(-170,-180)
turtle.color("tan")
turtle.pendown()
turtle.forward(330)

turtle.penup()
turtle.goto(-160,-150)
turtle.color("white")
turtle.pendown()
turtle.forward(305)

turtle.penup()
turtle.goto(-150,-120)
turtle.color("white")
turtle.pendown()
turtle.forward(280)

turtle.penup()
turtle.goto(-100,-100)
turtle.color("pink")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

turtle.penup()
turtle.goto(-90,0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-60,0)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-30,0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(0,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(30,0)
turtle.color("orange")
turtle.pendown()
turtle.forward(20)

# Dibuja los círculos de colores y rellénalos
colors = ["yellow", "yellow", "yellow", "yellow", "yellow", "yellow", "yellow"]
turtle.penup()
turtle.goto(-40, -50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.begin_fill()  # Comienza a llenar el círculo
    turtle.circle(10)
    turtle.end_fill()    # Termina de llenar el círculo
    turtle.right(angle)
    turtle.forward(10)

# Dibuja y rellena el círculo central
turtle.penup()
turtle.goto(-20, -55)  # Ajusta la posición al centro
turtle.color("white")  # Color de relleno para el círculo central
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)  # Dibuja el círculo central
turtle.end_fill()

turtle.penup()
turtle.goto(-170, 50)
turtle.color("cyan")
turtle.pendown()
turtle.write("¡Happy Birthday To You!", font=("Verdana", 25, "normal"))
turtle.color("black")
turtle.done()

pygame.quit()