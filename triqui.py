import pygame

pygame.init()
screen = pygame.display.set_mode((450 , 450))
pygame.display.set_caption("Triqui Juan ")

fondo = pygame.image.load('static/tictactoe_background.png')
circle = pygame.image.load('static/circle.png')
equis = pygame.image.load('static/x.png')

fondo = pygame.transform.scale(fondo , (450 , 450))
circle = pygame.transform.scale(circle , (125 , 125))
equis = pygame.transform.scale(equis , (120 , 120))

coors = [
    [(40,50),(165,50),(290,50)],
    [(40,175),(165,175),(290,175)],
    [(40,300),(165,300),(290,300)],
]

tablero = [
    ['','',''],
    ['','',''],    
    ['','',''],
]

turno = 'x'
game_over = False
clock = pygame.time.Clock()

def graficar_board ():
    screen.blit(fondo, (0,0))
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == 'x':
                difujar_x(fila , col)
            elif  tablero[fila][col] == '0':
                difujar_o(fila , col)
def difujar_x(fila , col):
    screen.blit(equis, coors[fila][col])

def difujar_o(fila , col):
    screen.blit(circle, coors[fila][col])

def validarGanador () :
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != '':
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != '':
            return True
    if tablero[0][0] == tablero [1][1] == tablero[2][2] != '':
        return True
    if tablero[0][2] == tablero [1][1] == tablero[2][0] != '':
        return True
    return False

while not game_over :
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            game_over = True
            break
        elif event.type== pygame.MOUSEBUTTONDOWN:
            mouseX , mouseY = event.pos
            if(mouseX >=  40 and mouseX < 415) and (mouseY >= 50 and mouseY < 425):
                fila = (mouseY - 50 ) // 125
                col = (mouseX - 40 ) // 125
                if tablero[fila][col] == '':
                    tablero[fila][col] = turno
                    fin_juego  = validarGanador()
                    if fin_juego:
                        print(f"El jugador {turno} a ganado")
                        game_over = True
                    turno = '0' if turno == 'x' else 'x'
    graficar_board()
    pygame.display.update()
pygame.quit()