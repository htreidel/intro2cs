# Hadar Treidel, hadar_t787, 20325554
import turtle


# repeating variables
petal_moves_forward = 30
petal_rotation_small_angle = 45
petal_rotation_big_angle = 135
flower_petals_angles = 90
flower_advanced_angles = 90
flower_advanced_forward = 150
flower_bed_angles = 180


def draw_petal():
    """this function draws one petal"""
    turtle.forward(petal_moves_forward)
    turtle.left(petal_rotation_small_angle)
    turtle.forward(petal_moves_forward)
    turtle.left(petal_rotation_big_angle)
    turtle.forward(petal_moves_forward)
    turtle.left(petal_rotation_small_angle)
    turtle.forward(petal_moves_forward)
    turtle.left(petal_rotation_big_angle)


def draw_flower():
    """this function uses first function to draw flower"""
    turtle.right(45)
    draw_petal()
    turtle.right(flower_petals_angles)
    draw_petal()
    turtle.right(flower_petals_angles)
    draw_petal()
    turtle.right(flower_petals_angles)
    draw_petal()
    turtle.right(135)
    turtle.forward(150)


def draw_flower_advanced():
    """draws flower and moves the starting point away for the next flower"""
    draw_flower()
    turtle.left(flower_advanced_angles)
    turtle.up()
    turtle.forward(flower_advanced_forward)
    turtle.left(flower_advanced_angles)
    turtle.forward(flower_advanced_forward)
    turtle.right(flower_advanced_angles)
    turtle.down()


def draw_flower_bed():
    """this function makes three flowers side by side"""
    turtle.up()
    turtle.left(flower_bed_angles)
    turtle.forward(200)
    turtle.right(flower_bed_angles)
    turtle.down()
    draw_flower_advanced()
    draw_flower_advanced()
    draw_flower_advanced()
