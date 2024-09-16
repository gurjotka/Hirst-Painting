import colorgram as cg
import turtle as t
import random

t.colormode(255)
# rgb_colors = []
# colors = cg.extract('image.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.r
#     b = color.rgb.r
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

color_list = [ (125, 125, 125), (187, 187, 187), (170, 170, 170), (5, 5, 5), (201, 
201, 201), (109, 109, 109), (39, 39, 39), (223, 223, 223), (84, 84, 84),
 (20, 20, 20), (111, 111, 111), (75, 75, 75), (8, 8, 8), (65, 65, 65),
   (132, 132, 132), (184, 184, 184), (183, 183, 183), (210, 210, 210),
     (178, 178, 178), (150, 150, 150), (90, 90, 90), (28, 28, 28), (193, 193, 193)
     , (17, 17, 17), (215, 215, 215), (190, 190, 190), (78, 78, 78)]

num = 9
t.penup()
t.hideturtle()
for _ in range(0, num+1):
  for _ in range(10):
      t.dot(20, random.choice(color_list))
      t.forward(30)
  t.home()
  t.left(90)
  t.forward(30*num)
  t.right(90)
  num-=1



my_screen = t.Screen()
my_screen.exitonclick()