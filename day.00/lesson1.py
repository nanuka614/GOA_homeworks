from turtle import *

#building a house
speed(20)
width(7)
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of square 

#drawing a door
forward(70) 
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door 
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()  #starting to build a roof 
goto(200,200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200) #end of the roof
end_fill()
penup()
color("blue")
end_fill()
penup()
goto(20,125)
pendown()
left(210)
forward(50)
right(90)
forward(50)
left(270)
forward(50)
right(90)
forward(50)
#drawing another window
penup()
goto(125,125)
pendown()
left(180)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

exitonclick()


