from turtle import*
from random import*

hideturtle()
speed(0)
width(1)
tracer(200,0)



#screen = Screen()
#screen.tracer(0, 0)

def rhomby(x,y,l,a,r,c,lw,fc):
  "xpos,ypos,side_lenght,internal_angle,rotation,colour,line_width,fillcolour"
  up()
  goto(x,y)
  down()
  width(lw)
  setheading(r)
  pencolor(c)
  fillcolor(fc)
  right(a/2)
  begin_fill()
  fd(l)
  bigangle=180-((360-(a*2))/2)
  left (bigangle)
  fd(l)
  lt(180-a)
  fd(l)
  lt(bigangle)
  fd(l)
  end_fill()

def linny(x,y,l,w,c,sh):
  up()
  goto(x,y)
  down()
  setheading(sh)
  color(c)
  width(w)
  fd(l)

up()
goto(-50,-200)
setheading(270)
down()
fillcolor("#966F33")
begin_fill()
for z in range(2):  
  fd(200) 
  lt(90)
  fd(100) 
  lt(90)
end_fill()




for i in range(50):
  x1=randint(-40,40)
  y1=randint(-400,-200)
  sh1=randint(75,105)
  w1=randint(1,3)
  l1=randint(3,50)
  linny(x1,y1,l1,w1,"#C68E17",sh1)

colors=("#306754", "#6AA121","#B1FB17"," #4CC417")
#colors=("#15317E", "#1569C7", "#5CB3FF", "#151B54")

for j in range(-200,200,15):
 for i in range(-200,200,5):
    fam=choice(colors)
    r1=randint(1,180)
    sl1=randint(4,16)
    rhomby(i,j,sl1,150,r1,fam,5,fam)

update()