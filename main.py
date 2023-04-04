from turtle import Turtle, Screen
import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, Linhas
import time

LARGURA = 800
ALTURA = 600
X1 = -360
X2 = 360

screen = Screen()
screen.setup(LARGURA, ALTURA)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle(X1)
r_paddle = Paddle(X2)
ball = Ball()
scoreboard = Scoreboard()
linhas = Linhas()


# Faz com que a cobra possa mudar de direção
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
# screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detectando se a bola encostou na parede
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.mudar_direcao_y()

    # Pondo da esquerda
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.atualizar_pontuacao('l')

    # Ponto da direita
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.atualizar_pontuacao('r')

    # Detectando colisão com as raquetes
    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 or ball.distance(l_paddle) < 50 and ball.xcor() < -335:
        ball.mudar_direcao_x()
        ball.aumentar_velocidade()

    if scoreboard.l_score > 4 or scoreboard.r_score > 4:
        game_is_on = False
        scoreboard.finalizar_jogo()


screen.exitonclick()
