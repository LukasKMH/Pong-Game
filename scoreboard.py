from turtle import Turtle
import time
ALINHAMENTO = "center"
FONTE = ("Courier", 60, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pontuacao = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-150, 200)
        self.write(self.l_score, align=ALINHAMENTO, font=FONTE)
        self.goto(150, 200)
        self.write(self.r_score, align=ALINHAMENTO, font=FONTE)
        self.atualizar_placar()

    def atualizar_placar(self):
        self.goto(-150, 200)
        self.write(self.l_score, align=ALINHAMENTO, font=FONTE)
        self.goto(150, 200)
        self.write(self.r_score, align=ALINHAMENTO, font=FONTE)

    def finalizar_jogo(self):
        if self.l_score > 4:
            self.goto(-175, 0)
            self.write(f"VENCEDOR!", align=ALINHAMENTO,
                       font=("Courier", 40, "normal")),

        if self.r_score > 4:
            self.goto(175, 0)
            self.write(f"VENCEDOR!", align=ALINHAMENTO,
                       font=("Courier", 40, "normal"))

    def atualizar_pontuacao(self, lado):
        if lado == 'l':
            self.l_score += 1
        if lado == 'r':
            self.r_score += 1
        self.clear()
        self.atualizar_placar()
        time.sleep(1)


class Linhas(Turtle):
    def __init__(self):
        super().__init__()
        self.linhas = []
        self.y_pos = -280
        for _ in range(14):
            self.criar_linhas(self.y_pos)
            self.y_pos += 50

    def criar_linhas(self, y):
        self.linha = Turtle("square")
        self.linha.shapesize(stretch_wid=1.5, stretch_len=0.1)
        self.linha.color("white")
        self.linha.penup()
        self.linha.goto(0, y)
        self.linhas.append(self.linha)
