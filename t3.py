import turtle

t = turtle.Turtle()
t.speed(3)


t.forward(100)

команда = input("Ухилення! (вліво або вправо): ")

if команда == "вліво":
    t.left(90)
elif команда == "вправо":
    t.right(90)
else:
    print("Ухилення не виконано")

turtle.done()
