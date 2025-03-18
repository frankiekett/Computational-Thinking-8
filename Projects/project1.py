###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("winter")

q1 = codesters.Square(100, 100, 200, 'navy')
q2 = codesters.Square(-100, 100, 200, 'blue')
q3 = codesters.Square(-100, -100, 200, 'light blue')
q4 = codesters.Square(100, -100, 200, 'white')

s1 = codesters.Sprite("ski", 100, 100)
s1.set_size(0.15)
s2 = codesters.Sprite("volleyball", -100,-100)
s2.set_size(0.1)
s3 = codesters.Sprite("hotdog2", 100, -100)
s3.set_size(0.2)
s4 = codesters.Sprite("cardinal", -100, 100)
s4.set_size(0.5)

message1 = codesters.Text("Frankie Kettrick",0,220,"Black")
message2 = codesters. Text("I love Caroline",0,-220,"Black")