import turtle

екран = turtle.Screen()

час = input("Введіть час доби (день або ніч): ")

if час == "день":
    екран.bgcolor("lightblue")
elif час == "ніч":
    екран.bgcolor("darkblue")
else:
    print("Невідомий час доби")

turtle.done()
