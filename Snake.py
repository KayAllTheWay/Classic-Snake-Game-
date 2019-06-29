#Classic Snake Game by Kenita

import turtle
import time
import random 

delay = 0.1 

#Screen
win = turtle.Screen()
win.title("Snake Game by Kenita")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

#Snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"
 
#Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("green")
food.penup()
food.goto(0,100)

segments = []


#Functions

def go_up ():
	if head.direction != "down":
		head.direction = "up"

def go_down():
	if head.direction != "up":
		head.direction = "down"

def go_left():
	if head.direction != "right":
		head.direction = "left"

def go_right(): 
	if head.direction != "left":
		head.direction = "right"			

def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + 20)

	if head.direction == "down":
		y = head.ycor()
		head.sety(y - 20)

	if head.direction == "left":
		x = head.xcor()
		head.setx(x - 20)

	if head.direction == "right":
		x = head.xcor()
		head.setx(x + 20)

#Keyboard bindings
win.listen()
win.onkeypress(go_up,"Up")		
win.onkeypress(go_down,"Down")
win.onkeypress(go_left,"Left")
win.onkeypress(go_right,"Right")

#Main game loop
while True:
	win.update()

	#Check for collision with border
	if head.xcor()>290 or head.xcor()<-290 or head .ycor()>290 or head.ycor()<-290:
		time.sleep(1)
		head.goto(0,0)
		head.direction = "stop"

		#Hide the segments
		for segment in segments: 
			segment.goto(1000, 1000)

		#Clear the segments list
		segments.clear()

 	#Check for collision with food 
	if head.distance(food) < 20: 
		#move the food to a random spot
		x = random.randint(-290, 290)
		y = random.randint( -290, 290)
		food.goto(x,y)

		#Add a segment
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("grey")
		new_segment.penup()     
		segments.append(new_segment)

		
	#Move the end segments first in reverse order
	for index in range(len(segments)-1, 0, -1):
 		x = segments[index-1].xcor()
 		y = segments[index-1].ycor()
 		segments[index].goto(x, y)

 	#Move segment 0 to where the head is
	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x,y)


	move()

	#Check for a collision with the border									
	if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
		time.sleep(1)
		head.goto(0,0)
		head.direction = "stop"

		#Hide the segments
		for segment in segments:
			segment.goto(1000, 1000)

		#Clear the segments list
		segments.clear()

	time.sleep(delay)

win.mainloop()