import turtle
import time as tm
#Turtles#
r = turtle.Turtle()
r.speed(0)
#Time Setup
seconds = tm.time()
local_time = tm.ctime(seconds)
print("Local time:", local_time)

#Getting and Converting text to Instructions#
s = input()
NAME = input("Filename Please (make sure its short)")
tm.sleep(1)
print("The original string is : " + str(s))
tm.sleep(1)
print("PROCESSING")
tm.sleep(2.5)
res = ''.join(format(i, 'b') for i in bytearray(s, encoding ='utf-8'))
print("The string after binary conversion : " + str(res))
tm.sleep(1)

#Moving the Instructions to a TXT file#
print("Creating File")
tm.sleep(3)
f = open("INSTstart "+ str(NAME) + ".txt","w+")
for i in range(1):
     f.write(res)
     f.close()

#Reading the Instructions and Creating the Curve#
x = "INSTstart "+ str(NAME) + ".txt"
print("Reading File")
tm.sleep(1)
f = open("INSTstart "+ str(NAME) + ".txt","r")
if f.mode == 'r':
        contents = f.read()
        print(contents)
        print(x)
        tm.sleep(1)
        with open(x) as f:
             while True:
                  ch = f.read(1)
                  if ch == "0":
                       r.forward(10)
                       r.left(90)
                  elif ch == "1":
                       r.forward(10)
                       r.right(90)
                  if not ch:
                       tm.sleep(2)
                       print("FILE READ")
                       break

#IT WOOOOORKS!!!!#
                    
