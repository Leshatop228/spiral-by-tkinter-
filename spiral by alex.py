import tkinter as tk
import math

window = tk.Tk()
window.title("Спираль алексея")

canvas = tk.Canvas(window, width=600, height=600, background="black")
canvas.pack()

turn_angle = 0
number_points = 0

def draw_circe_and_animation():
    global turn_angle, number_points
    canvas.delete("all")


    x = 300
    y = 300
    size_circle = 3

    list_color = ["red", "orange", "yellow", "lime", "purple"]

    for number in range(number_points):
        radius = 5 * math.sqrt(number)
        angle_point = number * 0.5 + math.radians(turn_angle)
        dx =  x + radius * math.cos(angle_point)
        dy =  y + radius * math.sin(angle_point)


        ring = int(radius // 10)
        color = list_color[ring % len(list_color)]

        left = dx - size_circle
        top = dy - size_circle
        right = dx + size_circle
        bottom = dy + size_circle

        canvas.create_oval(left, top, right, bottom, fill=color, outline="")

    turn_angle += 3
    number_points += 10

    if number_points > 500:
        number_points = 30

    window.after(50, draw_circe_and_animation)

draw_circe_and_animation()
window.mainloop()
