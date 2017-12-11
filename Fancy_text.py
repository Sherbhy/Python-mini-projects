

from turtle import *
from time import *

colours = { 
  'space': '#060608', 
  'moongrey': '#BCBDEF', 
  'verylime': '#A7E30E', 
  'deepsea': '#226363', 
  'reallyraspberry': '#FA057F', 
  'gloomygrey': '#363332', 
  'awesomeorange':  '#F37C06', 
  'coolcyan': '#4FEEF6',
  'perfectpurple': '#6820B0',
  'lovelylemon': '#FBF312',
}

screen = Screen()
screen.setup(400, 400)
screen.bgcolor(colours['space'])

penup()
goto(0, 100)
color(colours['reallyraspberry'])
style = ('Arial', 40, 'bold')
write('HELLO', font=style, align='center')
right(90)
forward(60)
color(colours['awesomeorange'])
write('WORLD', font=style, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(colours['moongrey'])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(colours['verylime'])
style=('Verdana', 20, 'bold')
write('Science', font=style, align='center')
forward(40)
color(colours['reallyraspberry'])
write('is', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['deepsea'])
write('the poetry', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(colours['awesomeorange'])
write('of', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['perfectpurple'])
write('reality', font=style, align='center')

