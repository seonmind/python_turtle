import turtle as t

t.colormode(255)
t.pencolor((163,153,141))
t.shape("turtle")
t.width(1)
t.speed(0)

# 붓 이동함수
def move(a,b):
    t.penup()
    t.goto(a,b)
    t.pendown()

# 몸체
start=(0,-100)
move(*start)

body_trace=[(-3,1),(-60,1),(-2,6),(50,6),(80,5),(0,1),(70,2),(90,2),(110,5.3),(116,12),(135,1.5), 
        (88,3),(105,2.5),(130,1.1),(210,1.1),(245,2.5),(272,2.5),(-185,2.6)]
t.fillcolor((163,153,141))
t.begin_fill()
for a,b in body_trace:
    t.setheading(a)
    t.fd(10*b)

move(*start)
   
for a,b in body_trace:
    t.setheading(180-a)
    t.fd(10*b)
t.end_fill()

# 팔 윤곽
t.pencolor("White")
move(122.2,-16.07)
t.setheading(100)
t.fd(50)
t.setheading(110)
t.fd(50)

move(-122.2,-16.07)
t.setheading(80)
t.fd(50)
t.setheading(70)
t.fd(50)

# 배
t.pencolor((163,153,141))
move(0,-90)

belly_trace=[(0,150,20),(20,80,30),(70,180,40),(110,100,30),(155,100,20)]
t.fillcolor((239,222,202))
t.begin_fill()
for a,b,c in belly_trace:
    t.setheading(a)
    t.circle(b,c)
t.goto(0,118)
move(0,-90)
for a,b,c in belly_trace:
    t.setheading(180-a)
    t.circle(-1*b,c)
t.goto(0,117)
t.end_fill()
t.penup()
t.goto(0,0)

# 눈
for i in [1,-1]:
    move(i*40,145)
    t.fillcolor("white")
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    move(i*40,149)
    t.fillcolor((103,94,87))
    t.begin_fill()
    t.circle(7)
    t.end_fill()

# 코
move(0,155)
nose_trace=[(0,75*0.8,15*0.8),(15,3*0.8,150*0.8),(165,75*0.8,15*0.9)]
t.fillcolor((103,94,87))
t.begin_fill()
for a,b,c in nose_trace:
    t.setheading(a)
    t.circle(b,c)
move(0,155)
for a,b,c in nose_trace:
    t.setheading(180-a)
    t.circle(-1*b,c)
t.end_fill()

# 입
t.width(2)
t.pencolor("Black")
move(0,140)
t.setheading(-30)
t.fd(7)
move(0,140)
t.setheading(210)
t.fd(7)

# 수염
t.width(1)

move(50,140)
t.setheading(0)
t.circle(100,30)
move(52,137)
t.setheading(-10)
t.circle(100,35)
move(54,133)
t.setheading(-20)
t.circle(100,40)

move(-50,140)
t.setheading(180)
t.circle(-100,30)
move(-52,137)
t.setheading(190)
t.circle(-100,35)
move(-54,133)
t.setheading(200)
t.circle(-100,40)

# 디테일
t.pencolor((103,94,87))
t.width(3)
move(-60,90)
t.setheading(60)
t.circle(-16,100)
move(-20,95)
t.setheading(60)
t.circle(-16,100)
move(20,95)
t.setheading(45)
t.circle(-16,100)

move(-70,50)
t.setheading(60)
t.circle(-16,100)
move(-30,60)
t.setheading(60)
t.circle(-16,100)
move(10,65)
t.setheading(45)
t.circle(-16,100)
move(50,60)
t.setheading(30)
t.circle(-16,100)

move(0,-500)

t.exitonclick()

