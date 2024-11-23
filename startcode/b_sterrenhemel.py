import turtle
import random
from sterren_module import *

kleuren = ("red", "orange", "yellow", "lime green", "orchid", "magenta", "dodger blue", "crimson", "chocolate", "navy", "salmon", "green yellow", "teal", "cyan", "aquamarine", "hot pink", "firebrick", "royal blue", "wheat")
for i in range(30):
    a = random.randint(-350,350)
    b = random.randint(-300,300)
    kleur = random.choice(kleuren)
    teken_ster(a, b, kleur)



turtle.exitonclick()