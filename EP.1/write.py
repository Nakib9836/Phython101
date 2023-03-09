Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
tao.shape('turtle')
tao.forward(180)
tao.forward(180)
tao.left(90)
tao.forward(45)
tao.left(90)
tao.forward(180)
>>> tao.forward(180)
>>> tao.clear()
>>> 
>>> 
>>> for i in range(4):
...     tao.forward(100)
...     tao.left(90)
... 
...     
>>> tao.penup()
>>> tao.goto(200,200)
>>> tao.pendown()
>>> for i in range(4):
...     tao.forward(100)
...     tao.left(90)
... 
...     
>>> tao.penup()
>>> tao.goto(-200,-200)
>>> tao.forward(100)
>>> tao.pendown()
>>> tao.forward(100)
>>> tao.left(135)
>>> tao.forward(100)
>>> tao.left(135)
>>> tao.forward(100)
