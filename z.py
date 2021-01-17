import turtle
import os
import math
import random
#import platform

'''if (platform().system== "windows"):
    try:
        import winsound
    except:
        print("winsound module not available ")'''

#screen
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("SPACE WARS")
wn.bgpic("background.gif")
wn.tracer(0)

turtle.register_shape("violaters.gif")
turtle.register_shape("player.gif")



#border
border_pen=turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(5)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#score
score=0
#draw score
score_pen = turtle.Turtle()
score_pen.speed=(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring="Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial",14,"normal"))
score_pen.hideturtle()


#player
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
playerspeed = 15


#choose no of enemies
number_of_enemies = 30
enemies=[]

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

enemy_start_x= -225
enemy_start_y = 250
enemy_number = 0

for enemy in enemies:
    enemy.color("red")
    enemy.shape("violaters.gif")
    enemy.penup()
    enemy.speed(0)
    
    x=enemy_start_x + (50 * enemy_number)
    y=enemy_start_y  
    
    enemy.setposition(x,y)
    enemy_number += 1
    if(enemy_number == 10):
        enemy_start_y -= 50
        enemy_number = 0
        
enemyspeed = 0.1

    
#BULLET
bullet = turtle.Turtle()
bullet.color("white")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletspeed = 3

#states of bullet
bulletstate="ready"

#functions 
def move_left():
	x = player.xcor()
	x -= playerspeed
	if(x < -280):x=-280
	player.setx(x)
	player.speed = -3

def move_right():
	x = player.xcor()
	x += playerspeed
	if (x > 280):x = 280
	player.setx(x)
	player.speed = 3

def fire_bullet():
    global bulletstate
    if(bulletstate == "ready"):
        #os.system("aflaser.wav&")
        bulletstate= "fire"   
        x=player.xcor()
        y=player.ycor() +10
        bullet.setposition(x,y)
        bullet.showturtle()
def is_collision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if(distance<15):
        return True
    else:
        return False
        
#
'''def play_sound("laser.wav",time=0):
    if platformsystem == "windows":
        winsound.Playsound("explosion.wav",winsound.SND_ASYNC)'''


#keyboard binding
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")

#main
while True:
    #move the enemy
    wn.update()
    for enemy in enemies:
        
        
        x=enemy.xcor()
        x+=enemyspeed
        enemy.setx(x)
        
        #move back and down
        if enemy.xcor()>280:
            #move all enemies down
            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            #change enemy direction
            enemyspeed*=-1
            
        if enemy.xcor()<-280:

            for e in enemies:
                y=e.ycor()
                y-=40
                e.sety(y)
            enemyspeed*=-1
        #checkfor collision
        if is_collision(bullet,enemy):
            #os.system("af play explosion.wav&")
            #reset bullet
            bullet.hideturtle()
            bulletstate="ready"
            bullet.setposition(0,-400)
            #reset enemy
            enemy.setposition(0,10000)
            #score update
            score+=10
            scorestring="Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial",14,"normal"))
            
        if is_collision(player,enemy):
            #play_sound("explosion.wav")
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER")
            break
    #move the bullet
    if(bulletstate=="fire"):
        
        y=bullet.ycor()
        y+=bulletspeed
        bullet.sety(y)
    #check if bullet passed margin
    if bullet.ycor()>275:
        bullet.hideturtle()
        bulletstate="ready"
    #
    if is_collision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("TRY AGAIN-->")
            break
    #
    if(score==300):
            player.hideturtle()
            enemy.hideturtle()
            print("YOU WON")
            break
            
        

   

   
    
    
