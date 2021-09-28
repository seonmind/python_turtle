import turtle as t
import math

t.shape("turtle")
t.speed(0)
t.width(2.5)

face_r=100
ear_r=30
ear_small_r=15

# 귀 위치 
ear_pos_deg=math.pi/4
ear_position_x=face_r*math.sin(ear_pos_deg)
ear_position_y=face_r*(1+math.cos(ear_pos_deg))*(1.05)-ear_r

ear_small_position_x=ear_position_x-ear_small_r*(0.3)
ear_small_position_y=ear_position_y+ear_r-ear_small_r*(1.3)

for i in (-1,1):
    # 바깥귀
    t.penup()
    t.goto(i*ear_position_x,ear_position_y)
    t.setheading(0)
    t.pendown()

    t.fillcolor("#8f5c4b")
    t.begin_fill()
    t.circle(ear_r)
    t.end_fill()

    # 안쪽귀
    t.penup()
    t.goto(i*ear_small_position_x,ear_small_position_y)
    t.setheading(0)
    t.pendown()

    t.fillcolor("#68422f")
    t.begin_fill()
    t.circle(ear_small_r)
    t.end_fill()

# 얼굴
t.goto(0,0)
t.fillcolor("#8f5c4b")
t.begin_fill()
t.circle(face_r)
t.end_fill()

# 눈
eye_position_x=face_r*0.11
eye_position_y=face_r*1.14
eye_r=eye_position_x*0.5

for i in (-1,1):
    t.penup()
    t.goto(i*eye_position_x,eye_position_y)
    t.setheading(0)
    t.pendown()

    t.fillcolor("Black")
    t.begin_fill()
    t.circle(eye_r)
    t.end_fill()



# 입 테두리
mouth_x_postion=eye_position_x+eye_r*0.2
mouth_y_position=face_r*0.94
mouth_r=mouth_x_postion
mouth_length=mouth_r*1.7

t.penup()
t.goto(mouth_x_postion,mouth_y_position)
t.pendown()
t.fillcolor("#ffd1b8")
t.begin_fill()
for i in [-1,1]:
    t.setheading(i*90)
    t.fd(mouth_length)
    t.setheading(i*-90)
    t.circle(mouth_r,-180)
t.end_fill()

# 코
nose_y_position=mouth_y_position-mouth_length/3
t.penup()
t.goto(0,nose_y_position)
t.pendown()

nose_r=eye_r*2
t.setheading(60)
for i in range(3):
    t.fd(nose_r)
    t.left(120)

# 입
for i in (150,45,180,60):
    t.right(i)
    t.fd(nose_r/1.5)

t.penup()
t.goto(0,0)
t.exitonclick()