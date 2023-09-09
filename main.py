import turtle as t
import time

t.color("red")

counter=0

while counter < 5 :
    t.forward(200)
    t.left(98)
    counter = counter+1
    t.end_fill()
    time.sleep(1)