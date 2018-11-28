import turtle,time,sys

oyunEkrani = turtle.Screen()
oyunEkrani.bgcolor("turquoise")
oyunEkrani.setup(800,600)
oyunEkrani.title('PACMAN')

class Labirent(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")            # labirentteki cisimlerin turu
        self.color("blue")             # labirentin rengi
        self.penup()                    # labirent nesneleri iz birakmasin
        self.speed(0)                   # labirent olusum hizi

class BitisNoktasi(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

class Pacman(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("triangle")
        self.color("red")
        self.setheading(0)
        self.pensize(2)
        self.penup()
        self.speed(0)


    def pacmanDown(self):
        self.pendown()
        if (self.heading() == 270):                   # asagiya bakarken
            pacX = round(pacman.xcor(),0)
            pacY = round(pacman.ycor(),0)
            if (pacX, pacY) in son:
                print("Hedefe Ulasildi!")
                oyunuBitir()

            if (pacX+24, pacY) in duvarlar:          # saginda duvar varsa
                if(pacX, pacY-24) not in duvarlar:      # altinda duvar yoksa
                    self.forward(24)                        # oldugu gibi ilerle
                    yolCiz(self.xcor(), self.ycor(), 270)
                else:
                    self.right(90)                      # altinda duvar varsa sola don
            else:                                    # saginda duvar yoksa
                self.left(90)                          # saga don
                self.forward(24)                       # ve ilerle
                yolCiz(self.xcor(), self.ycor(), 0)

    def pacmanRight(self):
        self.pendown()
        if (self.heading() == 0):                 # saga bakarken
            pacX = round(pacman.xcor(),0)
            pacY = round(pacman.ycor(),0)
            if (pacX, pacY) in son:
                print("Hedefe Ulasildi!")
                oyunuBitir()
            if (pacX, pacY+24) in duvarlar:         # ustunde duvar varsa
                if(pacX+24, pacY) not in duvarlar:    # saginda duvar yoksa
                    self.forward(24)                    # oldugu gibi ilerle
                    yolCiz(self.xcor(), self.ycor(), 0)
                else:                                 # saginda duvar varsa
                    self.right(90)                      # sadece asagi don
            else:                                   # ustunde duvar yoksa
                self.left(90)                        # yukari don
                self.forward(24)                        # ve ilerle
                yolCiz(self.xcor(), self.ycor(), 90)

    def pacmanUp(self):
        self.pendown()
        if (self.heading() == 90):          # yukari bakarken
            pacX = round(pacman.xcor(),0)
            pacY = round(pacman.ycor(),0)
            if (pacX, pacY) in son:
                print("Hedefe Ulasildi!")
                oyunuBitir()
            if (pacX-24, pacY) in duvarlar:         # solunda duvar varsa
                if (pacX, pacY+24) not in duvarlar:   # ustunde duvar yoksa
                    self.forward(24)                   # oldugun gibi ilerle
                    yolCiz(self.xcor(), self.ycor(), 90)
                else:                                 # ustunde duvar varsa
                    self.right(90)                     # sadece saga don
            else:                                   # solunda duvar yoksa
                self.left(90)                        # sola don
                self.forward(24)                     # ve ilerle
                yolCiz(self.xcor(), self.ycor(), 180)

    def pacmanLeft(self):
        self.pendown()
        if (self.heading() == 180):                      # sola giderken

            pacX = round(pacman.xcor(),0)
            pacY = round(pacman.ycor(),0)
            if (pacX, pacY) in son:                       # oldugun yer bitis noktasi ise
                print("Hedefe Ulasildi!")
                oyunuBitir()

            if (pacX, pacY-24) in duvarlar:             # eger altinda duvar var ise
                if (pacX - 24, pacY) not in duvarlar:     # eger solunda duvar yoksa
                    self.forward(24)                        # sola dogru ilerle
                    yolCiz(self.xcor(), self.ycor(), 180)   # iz birak
                else:                                     # eger solunda duvar varsa
                    self.right(90)                          # sadece yukari don
            else:                                        # eger altinda duvar yok ise
                self.left(90)                             # asagi don
                self.forward(24)                          # ve ilerle
                yolCiz(self.xcor(), self.ycor(), 270)     # iz birak


def yolCiz(xCor,yCor,heading):
    kullanilanYol.append((xCor, yCor))
    yol = turtle.Turtle()
    yol.speed(0)
    yol.hideturtle()
    yol.shape("triangle")
    yol.color("red")
    #if (xCor, yCor) in kullanilanYol:
    #    yol.color("blue")
    yol.setheading(heading)
    yol.penup()
    yol.goto(xCor, yCor)
    yol.pendown()
    yol.showturtle()

def oyunuBitir():
    oyunEkrani.exitonclick()
    sys.exit()

harita = [
"+++++++++++++++++++++++++++",
"+p                       ++",
"+++++++++++++++++++++    ++",
"+b                       ++",
"+   +++++++++++++++++++++++",
"+                     +++++",
"++++++                    +",
"++++++    +++++++++++++++++",
"++++++        ++         ++",
"+         +++++++++  ++++++",
"++++                     ++",
"++++ ++++++++         +++++",
"+    ++    +++++     ++++++",
"+                    ++++++",
"+++++++++++++++++++++++++++",
]

def haritaOlustur(harita):
    for y in range(len(harita)):
        for x in range(len(harita[y])):
            karakter = harita[y][x]
            ekran_x = -320 + (x * 24)
            ekran_y = 240 - (y * 24)

            if karakter == "+":                    # + lari bulunca
                labirent.goto(ekran_x, ekran_y)    # duvar olarak or
                labirent.stamp()
                duvarlar.append((ekran_x, ekran_y))# ve diziye ata

            if karakter == "b":                     # bitisnoktasi varsa
                bitis.goto(ekran_x, ekran_y)         # bitisnoktasini ata
                bitis.stamp()
                son.append((ekran_x, ekran_y))  # bitis noktasini diziye at

            if karakter == "p":                     # eger pacman haritada varsa
                pacman.goto(ekran_x, ekran_y)      # pacmani haritadaki noktaya tasi

# Programin baslatildigi alan...
labirent = Labirent()
pacman = Pacman()
bitis = BitisNoktasi()
duvarlar =[]
son = []
kullanilanYol = []

haritaOlustur(harita)

while True:
    pacman.pacmanRight()
    pacman.pacmanLeft()
    pacman.pacmanDown()
    pacman.pacmanUp()

    time.sleep(0.02)
