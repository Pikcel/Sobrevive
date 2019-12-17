
import pygame   # Librería de pygame
import random
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
NEGRO =(0, 0, 0)
# Estados
MENU = 1
JUGANDO = 2
CONTROLES = 3
OVER = 4
# Estados en Movimiento
QUIETO = 1
ARRIBA = 2
ABAJO = 3
DERECHA = 4
IZQUIERDA = 5
#def escribirMensaje (ventana, font, mensaje, color):
 #   texto = font.render(mensaje, True, color)
  #  ventana.blit(texto, [ANCHO // 3, ALTO // 3])
def dibujarPersonaje(ventana, spriteGlobo):
    ventana.blit(spriteGlobo.image, spriteGlobo.rect)
def dibujarObstaculos(ventana, listaObstaculos):
    for enemigos in listaObstaculos:
        ventana.blit(enemigos.image, enemigos)
def actualizarEnemigos(listaEnemigos):
    for enemigo in listaEnemigos: # VISITA a cada enemigo
        enemigo.rect.bottom += 1
        '''
        if enemigo.rect.bottom<=10:
            pass
        else:
            break
        '''
def verificacionColiciones(sonido, explosion, spriteGlobo, listaObstaculos):
    for o in range(len(listaObstaculos) - 1, -1, -1):
        obstaculos = listaObstaculos[o]
        # bala vs enemigo
        xg, yg, anchog, altog = spriteGlobo.rect
        xo, yo, anchoo, altoo = obstaculos.rect
        if xg >= xo and xg <= xo + anchoo and yg >= yo and yg <= yo - altoo:
            spriteGlobo = explosion
            sonido.play()
# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Inicializa el motor de pygame
    pygame.mixer.pre_init(44100,-16,2,2048)
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no
    # Imágenes para el juego
    imgFondo = pygame.image.load("fondom.png")
    xFondo = 0
    imgControles = pygame.image.load("controles.png")
    imgFondoJ = pygame.image.load("fondoj.png")
    #Estado inicial
    estado = MENU
    # Imágenes para el menú
    imgBtnJugar = pygame.image.load("button_jugar.png")
    imgBtnControles = pygame.image.load("button_controles.png")
    # Imágenes para controles
    imgBtnJugar2 = pygame.image.load("button_jugar2.png")
    imgBtnMenu = pygame.image.load("button_menu.png")
    imgTexto = pygame.image.load("texto.png")
    #Audio
    pygame.mixer.init()
    pygame.mixer.music.load("musicai.mp3")
    pygame.mixer.music.play(-1)
    # Personaje principal
    imgGlobo = pygame.image.load("globo.png")
    spriteGlobo = pygame.sprite.Sprite()
    spriteGlobo.image = imgGlobo
    spriteGlobo.rect = imgGlobo.get_rect()
    spriteGlobo.rect.left = ANCHO // 2 + spriteGlobo.rect.width // 2
    spriteGlobo.rect.bottom = ALTO - 25
    movimiento = QUIETO
    imgExplosion = pygame.image.load("explosion.png")
    spriteExp = pygame.sprite.Sprite()
    spriteExp.image = imgExplosion
    spriteExp.rect = imgExplosion.get_rect()
    #Imagen de los obtáculos
    listaObstaculos = []  # Lista vacía de enemigos
    imgObstaculos = pygame.image.load("bala1.png")
    for k in range(random.randint(1, 15)):
        spriteBala = pygame.sprite.Sprite
        spriteBala.image = imgObstaculos
        spriteBala.rect = imgObstaculos.get_rect()
        spriteBala.rect.left = random.randint(25, ANCHO - 25)
        spriteBala.rect.bottom = 25   #random.randint(0, ALTO)
        listaObstaculos.append(spriteBala)
    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w:
                    movimiento = ARRIBA
                    # spriteGlobo.rect.bottom -= 10
                elif evento.key == pygame.K_s:
                    movimiento = ABAJO
                    # spriteGlobo.rect.bottom += 10
                elif evento.key == pygame.K_d:
                    movimiento = DERECHA
                elif evento.key == pygame.K_a:
                    movimiento = IZQUIERDA
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm1, ym1 = pygame.mouse.get_pos()
                xm2, ym2 = pygame.mouse.get_pos()
                xm3, ym3 = pygame.mouse.get_pos()
                xm4, ym4 = pygame.mouse.get_pos()
                #Datos de los botones
                xb2 = 100
                xb1 = 100
                xb3 = 100
                xb4 = 100
                yb1 = 200
                yb2 = 380
                yb3 = 100
                yb4 = 200
                anchoB1 = 403
                anchoB2 = 400
                anchoB3 = 150
                anchoB4 = 155
                altoB1 = 130
                altoB2 = 130
                altoB3 = 60
                altoB4 = 60
                if xm1 >= xb1 and xm1 <= xb1 + anchoB1 and ym1 >= yb1 and ym1 <= yb1 + altoB1:
                    estado = JUGANDO
                if xm2 >= xb2 and xm2 <= xb2 + anchoB2 and ym2 >= yb2 and ym2 <= yb2 + altoB2:
                    estado = CONTROLES
                if estado == CONTROLES and xm3 >= xb3 and xm3 <= xb3 + anchoB3 and ym3 >= yb3 and ym3 <= yb3 + altoB3:
                    estado = MENU
                if estado == CONTROLES and xm4 >= xb4 and xm4 <= xb4 + anchoB4 and ym4 >= yb4 and ym4 <= yb4 + altoB4:
                    estado = JUGANDO
        reloj.tick(30)  # 40 fps
        # Pregunta en qué estado está el juego
        if estado == MENU:
            # Borrar pantalla
            ventana.fill(BLANCO)
            ventana.blit(imgFondo, (xFondo, 0))
            ventana.blit(imgBtnJugar, (100, 200))
            ventana.blit(imgBtnControles, (100, 380))
        elif estado == CONTROLES:
            ventana.fill(BLANCO)
            ventana.blit(imgControles, (xFondo, 0))
            ventana.blit(imgBtnMenu, (100, 100))
            ventana.blit(imgBtnJugar2, (100, 200))
            ventana.blit(imgTexto, (50, 50))
        elif estado == JUGANDO:
            #Audio0
            pygame.mixer.music.load("musicaj.mp3")
            pygame.mixer.music.play(-1)
            # Actualizar objetos
            ventana.fill(BLANCO)
            ventana.blit(imgFondoJ, (xFondo, 0))
            actualizarEnemigos(listaObstaculos)
            # Dibujar, aquí haces todos los trazos que requieras
            dibujarPersonaje(ventana, spriteGlobo)
            dibujarObstaculos(ventana, listaObstaculos)
            # Mover Personaje
            if movimiento == ARRIBA:
                spriteGlobo.rect.bottom -= 10
            elif movimiento == ABAJO:
                spriteGlobo.rect.bottom += 10
            elif movimiento == DERECHA:
                spriteGlobo.rect.right += 10
            elif movimiento == IZQUIERDA:
                spriteGlobo.rect.left -= 10
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()