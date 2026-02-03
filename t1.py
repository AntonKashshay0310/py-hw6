import turtle

t = turtle.Turtle()

команда = input("Введіть команду (вліво, вправо, вперед, назад): ")

if команда == "вліво":
    t.left(90)
elif команда == "вправо":
    t.right(90)
elif команда == "вперед":
    t.forward(100)
elif команда == "назад":
    t.backward(100)
else:
    print("Невідома команда")

turtle.done()
