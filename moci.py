import turtle

def draw_heart():
    turtle.bgcolor("black")
    turtle.pensize(2)
    turtle.color("red")
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()
    turtle.hideturtle()

def write_text():
    turtle.penup()
    turtle.goto(0, -150)  # Posisikan teks di bawah hati
    turtle.pendown()
    turtle.color("white")  # Warna teks putih
    turtle.write("I LOVE YOU SOO MUCH MOCII!!", align="center", font=("Arial", 20, "bold"))

draw_heart()
write_text()
turtle.done()