"""planets.py: Description of what planetary obitals.

__author__ = "Wanggan"
__pkuid__  = "1700011722"
__email__  = "1700011722@pku.edu.cn"
"""

import turtle
import math
win=turtle.Screen()
win.bgcolor("black")
sun=turtle.Turtle()
sun.color('white')
sun.shape('circle')
mer=turtle.Turtle()
ven=turtle.Turtle()
ear=turtle.Turtle()
mar=turtle.Turtle()
jup=turtle.Turtle()
sat=turtle.Turtle()

def orb(s1,s2,s3,s4,s5,s6,shape,w1,color1,e1,p1,w2,color2,e2,p2,w3,color3,e3,p3,w4,color4,e4,p4,w5,color5,e5,p5,w6,color6,e6,p6):
    s1.shape(shape)
    s1.color(color1)
    s1.pu()
    s1.ht()
    s1.goto(p1*e1/(1-e1),0)
    s1.st()
    s1.pd()
    s2.shape(shape)
    s2.color(color2)
    s2.pu()
    s2.ht()
    s2.goto(p2*e2/(1-e2),0)
    s2.pd()
    s2.st()
    s3.shape(shape)
    s3.color(color3)
    s3.pu()
    s3.ht()
    s3.goto(p3*e3/(1-e3),0)
    s3.pd()
    s3.st()
    s4.shape(shape)
    s4.color(color4)
    s4.pu()
    s4.ht()
    s4.goto(p4*e4/(1-e4),0)
    s4.pd()
    s4.st()
    s5.shape(shape)
    s5.color(color5)
    s5.pu()
    s5.ht()
    s5.goto(p5*e5/(1-e5),0)
    s5.pd()
    s5.st()
    s6.shape(shape)
    s6.color(color6)
    s6.pu()
    s6.ht()
    s6.goto(p6*e6/(1-e6),0)
    s6.pd()
    s6.st()
    for i in range(10000):
        c1=i/w1*360
        x1=e1*p1*math.cos(c1)/(1-e1*math.cos(c1))
        y1=e1*p1*math.sin(c1)/(1-e1*math.cos(c1))
        c2=i/w2*360
        x2=e2*p2*math.cos(c2)/(1-e2*math.cos(c2))
        y2=e2*p2*math.sin(c2)/(1-e2*math.cos(c2))
        c3=i/w3*360
        x3=e3*p3*math.cos(c3)/(1-e3*math.cos(c3))
        y3=e3*p3*math.sin(c3)/(1-e3*math.cos(c3))
        c4=i/w4*360
        x4=e4*p4*math.cos(c4)/(1-e4*math.cos(c4))
        y4=e4*p4*math.sin(c4)/(1-e4*math.cos(c4))
        c5=i/w5*360
        x5=e5*p5*math.cos(c5)/(1-e5*math.cos(c5))
        y5=e5*p5*math.sin(c5)/(1-e5*math.cos(c5))
        c6=i/w6*360
        x6=e6*p6*math.cos(c6)/(1-e6*math.cos(c6))
        y6=e6*p6*math.sin(c6)/(1-e6*math.cos(c6))
        s1.goto(x1,y1)
        s2.goto(x2,y2)
        s3.goto(x3,y3)
        s4.goto(x4,y4)
        s5.goto(x5,y5)
        s6.goto(x6,y6)
        
def main():
    """main module
    """
    orb(mer,ven,ear,mar,jup,sat,'circle',3500,'blue',0.2,300,5000,'yellow',0.21,500,6400,'green',0.24,800,7800,'red',0.23,1200,8800,'violet',0.22,1600,9200,'pink',0.27,1620)



if __name__ == '__main__':
    main()
