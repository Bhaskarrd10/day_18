# from turtle import Turtle, Screen
#
## import turtle as t
#
# timy = Turtle()
#
# timy.shape("turtle")
# timy.color("Red")
#
# for _ in range(4):
# timy.forward(100)
# timy.right(90)

# mport heroes

# rint(heroes.gen())


# import turtle as t
#
# tim = t.Turtle()
#
# for _ in range(25):
#    tim.forward(10)
#    tim.up()
#    tim.forward(10)
#    tim.pendown()

# def draw_shape(num_sides):
#    angle = 360 / num_sides
# for _ in range(num_sides):
#    tim.forward(100)
#    tim.right(angle)
#
# numbers = [1,2,3,4]
# name = "Reddy"
# new_lists = []
#
# for n in numbers:
#    add_1 = n+1
#    new_lists.append(add_1)
# print(new_lists)

# new_lists = [n+1 for n in numbers]
# new_name = [letter for letter in name]
# print (new_name)
#
# names= ["reddy", "ajay", "bha", "diya"]
#
# short_name = [name for name in names if len(name) < 5]
# name_uper = [name.upper() for name in names if len(name) > 4]
# print(name_uper)


student_dict = {
    "student": ["Bhaskar", "Angela", "Reddy"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# screen = Screen()
# screen.exitonclick()
