#Pong

import turtle
import os #added for sound effects(owen)

screen = turtle.Screen()
screen.title("Single Player OG Pong") #title change(owen)
screen.bgcolor("black") #change background for OG look(owen)
screen.setup(width=800, height=600)
screen.tracer(0)

# Score
score_b = 0

# Paddle B (The paddle we are changing to the bottom of screen)
paddle_b = turtle.Turtle()
paddle_b.speed(2) #paddle speed change(owen)
paddle_b.shape("square")
paddle_b.color("blue") #changed paddle B to blue(greg)
paddle_b.shapesize(stretch_wid=1,stretch_len=5)
paddle_b.penup()
paddle_b.goto(0, -200) #location of paddle B

# Ball
ball = turtle.Turtle()
ball.speed(3) #speed increase(owen)
ball.shape("square")
ball.color("white") #changed base ball color to white(greg)
ball.penup()
ball.goto(0, 200)
ball.dx = 10 #speed increase(owen)
ball.dy = 5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white") #text color change(greg)
pen.penup()
pen.hideturtle()
pen.goto(0, 240) #changed to fit bigger text(owen)
pen.write("SCORE: {}".format(score_b), align="center", font=("Courier", 50, "normal")) #code for title and scoreboard #bigger text for easier read(greg)

def paddle_b_left():
    x = paddle_b.xcor()
    x += -50 #speed increase(owen)
    paddle_b.setx(x)

def paddle_b_right():
    x = paddle_b.xcor()
    x += 50 #speed increase(owen)
    paddle_b.setx(x)


# Keyboard binding
screen.listen()
screen.onkeypress(paddle_b_left, "Left")
screen.onkeypress(paddle_b_right, "Right")

# Added new bindings (greg)
screen.onkeypress(paddle_b_left, "a")
screen.onkeypress(paddle_b_right, "s")

# Main game loop
while True:
    screen.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
            
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dx *= -1
    
    #new code for ball to bounce off side walls
    elif ball.xcor() > 400:
        ball.setx(400)
        ball.dx *= -1

    elif ball.xcor() < -400:
        ball.setx(-400)
        ball.dx *= -1

    #Paddle and ball collisions 
    if  ball.ycor() < -190 and ball.xcor() < paddle_b.xcor() + 10 and ball.xcor() > paddle_b.xcor() - 10:
        ball.sety(-190)
        ball.dy *= -1
        paddle_b.color("purple") #color changes(owen)
        ball.color("red") #color changes(owen)
        score_b += 1
        pen.clear()
        pen.write("SCORE: {}".format(score_b), align="center", font=("Courier", 50, "normal"))
        
        #Paddle and ball collisions #more colors(owen)
    if  ball.ycor() < -190 and ball.xcor() < paddle_b.xcor() + 20 and ball.xcor() > paddle_b.xcor() - 20:
        ball.sety(-190)
        ball.dy *= -1
        paddle_b.color("red")
        ball.color("purple")
        score_b += 1
        pen.clear()
        pen.write("SCORE: {}".format(score_b), align="center", font=("Courier", 50, "normal"))

        #Paddle and ball collisions #more colors(owen)
    if  ball.ycor() < -190 and ball.xcor() < paddle_b.xcor() + 30 and ball.xcor() > paddle_b.xcor() - 30:
        ball.sety(-190)
        ball.dy *= -1
        paddle_b.color("green")
        ball.color("white")
        score_b += 1
        pen.clear()
        pen.write("SCORE: {}".format(score_b), align="center", font=("Courier", 50, "normal"))

        #Paddle and ball collisions #more colors(owen)
    if  ball.ycor() < -190 and ball.xcor() < paddle_b.xcor() + 40 and ball.xcor() > paddle_b.xcor() - 40:
        ball.sety(-190)
        ball.dy *= -1
        paddle_b.color("orange")
        ball.color("green")
        score_b += 1
        pen.clear()
        pen.write("SCORE: {}".format(score_b), align="center", font=("Courier", 50, "normal"))

        #Paddle and ball collisions #more colors(owen)
    if  ball.ycor() < -190 and ball.xcor() < paddle_b.xcor() + 50 and ball.xcor() > paddle_b.xcor() - 50:
        ball.sety(-190)
        ball.dy *= -1
        paddle_b.color("yellow")
        ball.color("orange")
        score_b += 1
        pen.clear()
        pen.write("SCORE: {}".format(score_b), align="center", font=("Courier", 50, "normal"))

    elif ball.ycor() < -205: #endgame
        pen.clear()
        pen.write("GAME OVER! Restart Terminal! Final Score: {}".format(score_b), align="center", font=("Courier", 24, "normal"))
