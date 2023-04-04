from turtle import Turtle
import random
TAMANHO = 1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=TAMANHO, stretch_wid=TAMANHO)
        self.color("white")
        self.speed("fastest")
        self.x_move = 12
        self.y_move = 12
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def mudar_direcao_y(self):
        self.y_move *= -1

    def mudar_direcao_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.move_speed = 0.05
        self.mudar_direcao_x()
        self.goto(0, 0)

    def aumentar_velocidade(self):
        self.move_speed *= 0.9
