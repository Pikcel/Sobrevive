#Sebastian Macias Ibarra - A01376492
#Juego de obstáculos hecho con Pygame

#LIBRERÍAS UTILIZADAS
#import paho.mqtt.client as mqtt    #Librería para establecer conexión con un broker.
import pygame   #Librería para poder utilizar Pygame.
import random   #Librería para recibir valores aleatorios (útil al momento de posicionar obstáculos).

#DATOS CONSTANTES
ancho = 800   #Ancho de la pantalla.
alto = 600   #
blanco = (255, 255, 255)   #Color blanco en RGB: 0 es la máxima ausencia de color y 255 es la máxima presencia de color.
negro = (0, 0, 0)   #Color blanco en RGB: 0 es la máxima ausencia de color y 255 es la máxima presencia de color.
jugadores = []
posiciones = ["primer", "segundo", "tercer", "cuarto", "quinto"]

#DISEÑO Y PROGRAMACIÓN DE JUEGO
def juego():    #Función principal: dentro de ella se encuentran todos los objetos y funciones utilizadas para la creación del juego.
    #client = mqtt.Client("Sobrevive")   #Se establece un cliente con el nombre del juego. ################################################ Comentar en caso de no contar con wifi, para evitar errores.
    #client.connect("broker.hivemq.com")    #Se conecta a un broker. ###################################################################### Comentar en caso de no contar con wifi, para evitar errores.
    pygame.mixer.pre_init(44100, -16, 2, 2048)   #Se pre-inicia el mixer para evitar fallas o retrasos en la carga de archivos de música.
    pygame.init()   #Se inicia Pygame.
    pygame.mixer.init()   #Se inicia el mixer para poder reproducir música y sonidos.
    pantalla = pygame.display.set_mode((ancho, alto))   #Se inicia la pantalla del juego con las dimensiones anteriores, la cual será la misma ventana siempre.
    pygame.display.set_caption("Sobrevive")    #Se nombra la ventana con el nombre del juego ("Sobrevive").
    icono = pygame.image.load('globo.png')  #Se prepara el icono de la ventana del juego.
    pygame.display.set_icon(icono)  #Se establece el icono.
    #IMÁGENES Y OBJETOS UTILIZADOS
    bg_menu = pygame.image.load('fondom.png')   #Imagen del fondo de la pantalla Menú.
    bg_controles = pygame.image.load('controles.png')   #Imagen del fondo de la pantalla Controles.
    bg_juego = pygame.image.load('fondoj.png')    #Imagen del fondo de la pantalla Juego.
    bg_puntaje = pygame.image.load('fondop.png')    #Imagen del fondo de la pantalla Puntaje.
    ad = pygame.image.load('texto.png')   #Imagen del texto desplegado arriba en la pantalle de Controles.
    bot_controles = pygame.image.load('button_controles.png')   #Imagen del botón "Controles".
    botG_jugar = pygame.image.load('button_jugar.png')   #Imagen del botón grande "Jugar".
    bot_menu = pygame.image.load('button_menu.png')    #Imagen del botón "Menú".
    botS_jugar = pygame.image.load('button_jugar2.png')   #Imagen del botón pequeño "Jugar".
    bot_puntaje = pygame.image.load('button_puntaje.png')   #Imagen del botón "Puntaje".
    bot_regresar = pygame.image.load('button_regresar.png')    #Imagen del botón "Regresar".
    bot_retry = pygame.image.load('button_jugar-de-nuevo.png')    #Imagen del botón "Jugar de nuevo".
    explode = pygame.image.load('explosion.png')    #Imagen del personaje cuando pierde (explosión).
    globo = pygame.image.load('globo.png')    #Imagen del personaje (globo).
    bala1 = pygame.image.load('bala1.png')    #Imagen del enemigo/obstáculo (bala).
    bala2 = pygame.image.load('bala2.png')    #Imagen del enemigo/obstáculo (bala).
    bala3 = pygame.image.load('bala3.png')    #Imagen del enemigo/obstáculo (bala).
    bala4 = pygame.image.load('bala4.png')    #Imagen del enemigo/obstáculo (bala).
    bala5 = pygame.image.load('bala5.png')    #Imagen del enemigo/obstáculo (bala).
    reloj = pygame.time.Clock()   #Se inicia un reloj de Pygame para interactuar con el framerate y el cronómetro.
    pygame.mixer.music.load('musicai.mp3')   #Se reproduce la música inicial.
    pygame.mixer.music.play(-1)    #Se reproduce -1 veces para hacer un ciclo y que se reproduzca de forma infinita.
    archivo = open("Score.txt", "a")
    archivo.close()

    #FUNCIÓN PARA EL DISEÑO E INTERACCIÓN DE LA PANTALLA DEL MENÚ
    def menu():    #Nombre de la función de menú.
        pantalla.fill(blanco)   #Se "borra" la pantalla anterior y se deja literalmente en blanco.
        pantalla.blit(bg_menu, (0, 0))   #Se muestra la imagen de fondo del menú.
        pantalla.blit(botG_jugar, (100, 200))   #Se muestra la imagen del botón "Jugar".
        pantalla.blit(bot_controles, (100, 380))   #Se muestra la imagen del botón "Controles".
        pantalla.blit(bot_puntaje, (550, 50))   #Se muestra la imagen del botón "Puntaje".
        xb = [100, 503, 550, 696]   #Aquí están las medidas del inicio y final de los botones en x.
        yb = [200, 330, 380, 510, 50, 110]   #Aquí están las medidas del inicio y final de los botones en y.
        while True:    #Aquí hay un ciclo para evitar que continúe el programa antes de que se exista alguna instrucción. Hasta entonces, se correrá el menú de forma infinita.
            for event in pygame.event.get():    #Recibe los eventos en Pygame.
                if event.type == pygame.QUIT:    #Condicional si se oprime el botón para cerrar ventana.
                    pygame.quit()   #Orden para cerrar la ventana de pygame.
                if event.type == pygame.MOUSEBUTTONDOWN:    #Condicional si se oprime el botón del mouse.
                    xm, ym = pygame.mouse.get_pos()   #En xm se recibirá el valor de la posición x del cursor cuando se apretó el botón del mouse, y ym recibirá el valor de la posición y del cursor.
                    if xm >= xb[0] and xb[1] >= xm and ym >= yb[0] and yb[1] >= ym:    #Condicional para evaluar la posición del cursor dentro del rango del botón "Jugar".
                        juego()    #Si el botón "Jugar" fue oprimido, se realizará la función del juego.
                    if xm >= xb[0] and xb[1] >= xm and ym >= yb[2] and yb[3] >= ym:    #Condicional para evaluar la posición del cursor dentro del rango del botón "Controles".
                        controles()    #Si el botón "Controles" fue oprimido, se realizará la función de los controles.
                    if xm >= xb[2] and xb[3] >= xm and ym >= yb[4] and yb[5] >= ym:    #Condicional para evaluar la posición del cursor dentro del rango del botón "Puntaje".
                        puntajes()    #Si el botón "Puntaje" fue oprimido, se realizará la función de los puntajes.
            pygame.display.update()    #Mientras se siga dentro del while, esta función actualizará la pantalla.

    # FUNCIÓN PARA EL DISEÑO E INTERACCIÓN DE LA PANTALLA DE LOS PUNTAJES
    def puntajes():    #Nombre de la función de los puntajes*.
        pantalla.fill(blanco)   #Se "borra" la pantalla anterior y se deja literalmente en blanco.
        pantalla.blit(bg_puntaje, (0, 0))   #Se muestra la imagen de fondo de los puntajes.
        pantalla.blit(bot_regresar, (100, 400))   #Se muestra la imagen del botón "Regresar".
        xb = [100, 500]   #Aquí están las medidas del inicio y final de los botones en x.
        yb = [400, 530]   #Aquí están las medidas del inicio y final de los botones en y.
        while True:    #Aquí hay un ciclo para evitar que continúe el programa antes de que se exista alguna instrucción. Hasta entonces, se correrá la pantalla de los puntajes de forma infinita.
            for event in pygame.event.get():    #Recibe los eventos en Pygame.
                if event.type == pygame.QUIT:    #Condicional si se oprime el botón para cerrar ventana.
                    pygame.quit()   #Orden para cerrar la ventana de pygame.
                if event.type == pygame.MOUSEBUTTONDOWN:    #Condicional si se oprime el botón del mouse.
                    xm, ym = pygame.mouse.get_pos()   #En xm se recibirá el valor de la posición x del cursor cuando se apretó el botón del mouse, y ym recibirá el valor de la posición y del cursor.
                    if xm >= xb[0] and xb[1] >= xm and ym >= yb[0] and yb[1] >= ym:    #Condicional para evaluar la posición del cursor dentro del rango del botón "Regresar".
                        menu()    #Si el botón "Regresar" fue oprimido, se realizará la función del menú.
            puntaje()   #Se mostrará en pantalla de forma constante los datos de la función puntaje mientras se siga dentro del while.
            pygame.display.update()    #Mientras se siga dentro del while, esta función actualizará la pantalla.

    #FUNCIÓN PARA EL DISEÑO E INTERACCIÓN DE LA PANTALLA DE LOS CONTROLES
    def controles():    #Nombre de la función de los controles.
        pantalla.fill(blanco)   #Se "borra" la pantalla anterior y se deja literalmente en blanco.
        pantalla.blit(bg_controles, (0, 0))   #Se muestra la imagen de fondo de los controles.
        pantalla.blit(bot_menu, (100, 100))   #Se muestra la imagen del botón "Menú".
        pantalla.blit(botS_jugar, (100, 200))   #Se muestra la imagen del botón "Jugar".
        pantalla.blit(ad, (50, 50))   #Se muestra la imagen del aviso sobre la velocidad del personaje.
        xb = [100, 255]   #Aquí están las medidas del inicio y final de los botones en x.
        yb = [100, 160, 200, 260]   #Aquí están las medidas del inicio y final de los botones en y.
        while True:    #Aquí hay un ciclo para evitar que continúe el programa antes de que se exista alguna instrucción. Hasta entonces, se correrá la pantalla de los controles de forma infinita.
            for event in pygame.event.get():    #Recibe los eventos en Pygame.
                if event.type == pygame.QUIT:    #Condicional si se oprime el botón para cerrar ventana.
                    pygame.quit()   #Orden para cerrar la ventana de pygame.
                if event.type == pygame.MOUSEBUTTONDOWN:    #Condicional si se oprime el botón del mouse.
                    xm, ym = pygame.mouse.get_pos()   #En xm se recibirá el valor de la posición x del cursor cuando se apretó el botón del mouse, y ym recibirá el valor de la posición y del cursor.
                    if xm >= xb[0] and xb[1] >= xm and ym >= yb[0] and yb[1] >= ym:    #Condicional para evaluar la posición del cursor dentro del rango del botón "Menú".
                        menu()    #Si el botón "Menú" fue oprimido, se realizará la función del menú.
                    if xm >= xb[0] and xb[1] >= xm and ym >= yb[2] and yb[3] >= ym:    #Condicional para evaluar la posición del cursor dentro del rango del botón "Jugar".
                        juego()    #Si el botón "Jugar" fue oprimido, se realizará la función del juego.
            pygame.display.update()    #Mientras se siga dentro del while, esta función actualizará la pantalla.

    #FUNCIÓN PARA LA IMPRESIÓN DE LOS PUNTAJES EN LA PANTALLA DE PUNTAJE
    def puntaje():    #Nombre de la función de los puntajes**.
        fuente = pygame.font.Font('CaviarDreams.ttf', 22)   #Se inicia una fuente para poder agregar texto. Dentro del paréntesis, el primer valor es el nombre de la fuente y el segundo es el tamaño de letra.
        registro = open("Score.txt", "r")
        jugadores = registro.read()
        jugadores = jugadores.split(",")
        jugadores.remove('')
        for x in range(5):
            jugadores.append(0.0)
        for x in range(len(jugadores)):
            jugadores[x] = float(jugadores[x])
        jugadores.sort(reverse=True)
        for x in range(5):
            y = 40 * x  # Esta variable es para la posición en 'y' de cada puntaje. Dentro de for, usamos "'x' en el rango de jugadores", así que pos cada jugador, 'y' será igual a 30 por el número de jugador, por lo cual cada vez será mayor el valor de 'y', pero constante.
            texto = fuente.render("Puntos del " + posiciones[x] + " lugar: " + str(round(jugadores[x])), True, (255, 255, 255))  # Se hace una variable para poder usar nuestro texto como una superficie y poder mostrarlo en pantalla. Dentro del paréntesis está nuestro texto y el color del mismo (blanco). Texto = Puntos del jugador [número de jugador (toma la posición 'x' del for, le suma uno y se agrega como string al texto)]: [puntaje del jugador (agrega el valor de la jugadores[] en la posición 'x' como un string)].
            pantalla.blit(texto, (45, y + 150))  # Muestra el texto de cada jugador en la pantalla, con 45 como 'x' y 'y + 130' como 'y'.

    #FUNCIÓN PARA LA IMPRESIÓN DE LOS PUNTAJES EN LA PANTALLA DE JUEGO
    def puntaje_juego(points):    #Nombre de la función de los puntajes***. Dentro de la función, se recibirán los "puntos", dados por la función juego().
        fuente = pygame.font.Font('Amatic-Bold.ttf', 30)   #Se inicia una fuente para poder agregar texto. Dentro del paréntesis, el primer valor es el nombre de la fuente y el segundo es el tamaño de letra.
        texto = fuente.render("Puntos: {0}".format(round(points)), True, (0, 0, 0))   #Se hace una variable para poder usar nuestro texto como una superficie y poder mostrarlo en pantalla. Dentro del paréntesis está nuestro texto y el color del mismo (negro). Texto = Puntos: [puntos (valor que se reciba como "points", convertido a string)].
        pantalla.blit(texto, (560, 17))    #Muestra el texto de los puntos en la pantalla, con 560 como 'x' y 17 como 'y'.

    #FUNCIÓN PARA LA IMPRESIÓN DEL CRONÓMETRO EN LA PANTALLA DE JUEGO
    def tiempo(segundos):    #Nombre de la función del cronómetro. Dentro de la función, se recibirán los "segundos", dados por la función juego().
        fuente = pygame.font.Font('Amatic-Bold.ttf', 30)   #Se inicia una fuente para poder agregar texto. Dentro del paréntesis, el primer valor es el nombre de la fuente y el segundo es el tamaño de letra.
        texto = fuente.render("Tiempo: {0:.0f}".format(segundos), True, (0, 0, 0))   #Se hace una variable para poder usar nuestro texto como una superficie y poder mostrarlo en pantalla. Dentro del paréntesis está nuestro texto y el color del mismo (negro). Texto = Tiempo: [puntos (valor que se reciba como "segundos", convertido a string)].
        pantalla.blit(texto, (15, 17))    #Muestra el texto del tiempo en la pantalla, con 15 como 'x' y 17 como 'y'.

    #FUNCIÓN PARA LA CREACIÓN DE UNA SUPERFICIE DE CON TEXTO
    def textos(texto, fuente):    #Nombre de la función. Dentro de la función, se recibirá el texto y la fuente del mismo, dados por la función mensaje().
        textSurface = fuente.render(texto, True, (0, 0, 0))     #Se hace una variable para poder usar nuestro texto como una superficie y poder mostrarlo en pantalla. Dentro del paréntesis se encuentra el texto que se recibirá al llamar la función y el color del mismo (negro).
        return textSurface, textSurface.get_rect()     #Regresa a la función de la cual fue llamada y devuelve el texto final como superficie y las medidas del mismo.

    #FUNCIÓN PARA AGREGAR TEXTO CENTRADO A LA PANTALLA
    def mensaje(texto):    #Nombre de la función. Dentro de la función, se recibirá el texto, dado por la función boom().
        fuente = pygame.font.Font('Amatic-Bold.ttf', 115)   #Se inicia una fuente para poder agregar texto. Dentro del paréntesis, el primer valor es el nombre de la fuente y el segundo es el tamaño de letra.
        TextSurf, TextRect = textos(texto, fuente)   #Se crear variables en las que se recibe la información de textos().
        TextRect.center = ((ancho / 2), (alto / 2) - 100)    #Se alínea el texto con el centro de la pantalla.
        pantalla.blit(TextSurf, TextRect)    #Muestra el texto del tiempo en la pantalla.

    #FUNCIÓN PARA MOSTRAR EL PERSONAJE
    def personaje(x, y):    #Nombre de la función del personaje. Dentro de la función, se recibirá 'x' y 'y', dadas por la función juego().
        pantalla.blit(globo, (x, y))    #Se muestra la imagen de globo en la pantalla en la posición (x,y).

    #FUNCIÓN PARA MOSTRAR LAS BALAS
    def balas(x1, x2, x3, x4, x5, y):    #Nombre de la función de las balas. Dentro de la función, se recibirá una 'x' por cada bala y 'y', dadas por la función juego().
        pantalla.blit(bala1, (x1, y))    #Se muestra la imagen de una bala en la pantalla en la posición (x1,y).
        pantalla.blit(bala2, (x2, y))    #Se muestra la imagen de una bala en la pantalla en la posición (x2,y).
        pantalla.blit(bala3, (x3, y))    #Se muestra la imagen de una bala en la pantalla en la posición (x3,y).
        pantalla.blit(bala4, (x4, y))    #Se muestra la imagen de una bala en la pantalla en la posición (x4,y).
        pantalla.blit(bala5, (x5, y))    #Se muestra la imagen de una bala en la pantalla en la posición (x5,y).

    # FUNCIÓN PARA PERDER
    def boom(x, y, x1, x2, x3, x4, x5, yb, s, p):    #Nombre de la función perder. Dentro de la función, se recibirán las posiciones en 'x' y 'y' de cada bala y del globo, también los segundos y los puntos, dados por la función juego().
        #client.publish("sobrevive/puntaje/", p, 0)    #Se publica en el broker el puntaje final, con el tópico establecido entre los paréntesis.############################################################################3
        #client.disconnect()   #Se desconecta del broker.############################################################################3
        pantalla.fill(blanco)   #Se "borra" la pantalla anterior y se deja literalmente en blanco.
        pantalla.blit(bg_juego, (0, 0))   #Se muestra la imagen de fondo del juego.
        balas(x1, x2, x3, x4, x5, yb)   #Se llama a la función balas() con las últimas posiciones en que éstas estaban antes de que el jugador perdiera.
        mensaje("Perdiste")   #Se llama a la función mensaje() para mostrar el texto "Perdiste" en pantalla.
        personaje(-100, -100)   #Se llama a la personaje() con las últimas posiciones (-100,-100) para que el globo no se muestre en pantalla.
        pantalla.blit(explode, (x, y))       #Se muestra la imagen del personaje cuando pierde en pantalla en las últimas posiciones en las que estaba el globo antes de perder.
        tiempo(s)   #Se llama a la función tiempo() para mostrar el cronómetro final antes de perder.
        puntaje_juego(p)   #Se llama a la función puntaje_juego() para mostrar el puntaje final antes de perder.
        jugadores.append(p) #Se agrega el último puntaje (p) a la lista jugadores[] cada que se pierde.
        pantalla.blit(bot_retry, (100, 420))   #Se muestra la imagen del botón "Volver a jugar".
        pantalla.blit(bot_menu, (500, 400))   #Se muestra la imagen del botón "Menú".
        xb = [100, 256, 500, 650]   #Aquí están las medidas del inicio y final de los botones en x.
        yb = [420, 458, 400, 460]   #Aquí están las medidas del inicio y final de los botones en y.
        registro = open("Score.txt", "a")
        registro.write(str(p) + ",")
        registro.close()
        while True:    #Aquí hay un ciclo para evitar que continúe el programa antes de que se exista alguna instrucción. Hasta entonces, se correrá la pantalla de game over de forma infinita.
            for event in pygame.event.get():    #Recibe los eventos en Pygame.
                if event.type == pygame.QUIT:    #Condicional si se oprime el botón para cerrar ventana.
                    pygame.quit()   #Orden para cerrar la ventana de pygame.
                if event.type == pygame.MOUSEBUTTONDOWN:    #Condicional si se oprime el botón del mouse.
                    xm, ym = pygame.mouse.get_pos()   #En xm se recibirá el valor de la posición x del cursor cuando se apretó el botón del mouse, y ym recibirá el valor de la posición y del cursor.
                    if xm >= xb[0] and xb[1] >= xm and ym >= yb[0] and yb[1] >= ym:    #Condicional para evaluar la posición del cursor dentro del rango del botón "Jugar de nuevo".
                        juego()    #Si el botón "Jugar de nuevo" fue oprimido, se realizará la función del juego.
                    if xm >= xb[2] and xb[3] >= xm and ym >= yb[2] and yb[3] >= ym:    #Condicional para evaluar la posición del cursor dentro del rango del botón "Menú".
                        pygame.mixer.music.load('musicai.mp3')   #Se reproduce la música inicial de nuevo.
                        pygame.mixer.music.play(-1)    #Se reproduce -1 veces para hacer un ciclo y que se reproduzca de forma infinita.
                        menu()    #Si el botón "Menú" fue oprimido, se realizará la función del menú.
            pygame.display.update()    #Mientras se siga dentro del while, esta función actualizará la pantalla.

    #FUNCIÓN DEL JUEGO
    def juego():   #Nombre de la función que llevará a cabo el juego.
        pygame.mixer.music.load('musicaj.mp3')   #Se reproduce la música del juego.
        pygame.mixer.music.play(-1)    #Se reproduce -1 veces para hacer un ciclo y que se reproduzca de forma infinita.
        pantalla.fill(blanco)   #Se "borra" la pantalla anterior y se deja literalmente en blanco.
        pantalla.blit(bg_juego, (0, 0))   #Se muestra la imagen de fondo del juego.
        ancho_bala = pygame.Surface.get_width(bala1)    #Variable igual al ancho de las balas. Nota: todas las balas miden lo mismo.
        alto_bala = pygame.Surface.get_height(bala1)    #Variable igual al alto de las balas. Nota: todas las balas miden lo mismo.
        puntos = 0    #Variable inicialmente igual a 0. Aquí se irán sumando los puntos.
        x = []     #Lista en la que se irán asignando posiciones aleatorias en 'x' para las balas.
        y = -alto_bala      #Posición 'y' de las balas.
        mov_gx = 10    #Velocidad de movimiento horizontal constante del globo.
        mov_gy = 8    #Velocidad de movimiento vertical constante del globo.
        pos_gx = 378    #Posición en 'x' del globo. Inicialmente comienza en 378.
        pos_gy = 500    #Posición en 'y' del globo. Inicialmente comienza en 500.
        personaje(pos_gx, pos_gy)    #Se llama a la función personaje() para mostrar por primera vez al globo en su posición inicial.
        tiempo_inicial = pygame.time.get_ticks()/1000    #Variable que almacena el tiempo que ha pasado desde que se ejecutó el programa.
        velocidad = 1   #Velocidad de caída de las balas.
        movimiento = 0   #Dirección de movimiento del globo.
        yg = pygame.Surface.get_height(globo)    #Variable igual a la altura del globo.
        siguiente = False   #Booleano para continuar o terminar un while.
        for i in range(5):      #Un ciclo for que usaremos para asignar las posiciones iniciales en 'x' de las balas, por lo cual tenemos un rango de 5.
            x.append(random.randrange(0,800-ancho_bala))    #Aquí se agregar un valor aleatorio entre el ancho de la pantalla a la lista x[]. Cada valor en x[] será el valor de 'x' en la posición de una bala.
        while not siguiente:    #Aquí hay un ciclo para evitar que continúe el programa antes de que se siguiente sea igual a True. Hasta entonces, se correrá la pantalla del juego de forma infinita.
            for event in pygame.event.get():    #Recibe los eventos en Pygame.
                if event.type == pygame.QUIT:    #Condicional si se oprime el botón para cerrar ventana.
                    pygame.quit()   #Orden para cerrar la ventana de pygame.
                if event.type == pygame.KEYDOWN:    #Condicional si se oprime alguna tecla del teclado.
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:    #Condicional si se oprime "A".
                        movimiento = 1     #Si la tecla A fue oprimida, el movimiento del globo será hacia la izquierda (1).
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:    #Condicional si se oprime "D".
                        movimiento = 2     #Si la tecla D fue oprimida, el movimiento del globo será hacia la derecha (2).
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:    #Condicional si se oprime "S".
                        movimiento = 3     #Si la tecla S fue oprimida, el movimiento del globo será hacia abajo (3).
                    if event.key == pygame.K_w or event.key == pygame.K_UP:    #Condicional si se oprime "W".
                        movimiento = 4     #Si la tecla W fue oprimida, el movimiento del globo será hacia arriba (4).
                    if event.key == pygame.K_ESCAPE:    #Condicional si se oprime "Esc".
                        pygame.mixer.music.load('musicai.mp3')   #Se reproduce la música inicial de nuevo.
                        pygame.mixer.music.play(-1)    #Se reproduce -1 veces para hacer un ciclo y que se reproduzca de forma infinita.
                        menu()    #Si la tecla "Esc" fue oprimida, se realizará la función del menú.
            if movimiento == 1:    #Condicional para definir la dirección actual del movimiento (izquierda).
                pos_gx -= mov_gx     #Si el movimiento es hacia la izquierda, entonces se restará el movimiento en 'x' del globo a su posición de forma constante.
            if movimiento == 2:    #Condicional para definir la dirección actual del movimiento (derecha).
                pos_gx += mov_gx     #Si el movimiento es hacia la derecha, entonces se sumará el movimiento en 'x' del globo a su posición de forma constante.
            if movimiento == 3:    #Condicional para definir la dirección actual del movimiento (abajo).
                pos_gy += mov_gy     #Si el movimiento es hacia la abajo, entonces se sumará el movimiento en 'y' del globo a su posición de forma constante.
            if movimiento == 4:    #Condicional para definir la dirección actual del movimiento (arriba).
                pos_gy -= mov_gy     #Si el movimiento es hacia la arriba, entonces se restará el movimiento en 'y' del globo a su posición de forma constante.
            pantalla.fill(blanco)   #Se "borra" la pantalla anterior y se deja literalmente en blanco.
            pantalla.blit(bg_juego, (0, 0))   #Se muestra la imagen de fondo del juego.
            personaje(pos_gx, pos_gy)    #Se llama a la función personaje() para mostrar al globo en su nueva posición.
            balas(x[0], x[1], x[2], x[3], x[4], y)    #Se llama a la función balas() para mostrar las balas en sus nuevas posiciones.
            y += velocidad   #Se sumará constantemente la velocidad a 'y' (posición 'y' de las balas) para que vayan descenciendo desde la parte superior de la ventana.
            segundos = (pygame.time.get_ticks() / 1000) - tiempo_inicial   #La variable será igual al tiempo menos el tiempo inicial para que el cronómetro comience en cero ya que, al comenzar a contarse el tiempo desde que se ejecutó el programa, sería un dato falso si es que no se restara el tiempo antes de iniciar la función juego().
            tiempo(segundos)   #Se llama a la función tiempo() para mostrar el cronómetro en pantalla mientras se está jugando.
            puntos += segundos * .005   #Se establece una relación entre puntos y segundos, y esto se suma a la variable puntos. Si uno dura más tiempo sin perder, gana más puntos.
            puntaje_juego(puntos)   #Se llama a la función puntaje_juego() para mostrar el puntaje en pantalla mientras se está jugando.
            if pos_gx - 15 < 0 or pos_gx + 33 > 785 or pos_gy - 20 < 0 or pos_gy + yg > 600:       #Condicional para limitar el globo dentro de la pantalla. Si el globo cumple la condición y se sale del marco, el jugador habrá perdido.
                pygame.mixer.music.load('cuak.mp3')   #Se reproduce el sonido para cuando pierde el jugador.
                pygame.mixer.music.play(1)     #El sonido se reproduce una sola vez.
                boom(pos_gx-22, pos_gy-10, x[0], x[1], x[2], x[3], x[4], y, segundos, puntos)   #Se llama a la función boom() para cambiar terminar el juego y mostrar la pantalla de cuando el jugador ha perdido.
                siguiente = True   #Si siguiente es igual a True, se rompe el while.

            if (((pos_gx + 25 > x[0] and pos_gx + 25 < x[0] + ancho_bala) or (pos_gx < x[0] + ancho_bala and pos_gx > x[0])) or ((pos_gx + 25 > x[1] and pos_gx + 25 < x[1] + ancho_bala) or (pos_gx < x[1] + ancho_bala and pos_gx > x[1])) or ((pos_gx + 25 > x[2] and pos_gx + 25 < x[2] + ancho_bala) or (pos_gx < x[2] + ancho_bala and pos_gx > x[2])) or ((pos_gx + 25 > x[3] and pos_gx + 25 < x[3] + ancho_bala) or (pos_gx < x[3] + ancho_bala and pos_gx > x[3])) or ((pos_gx + 25 > x[4] and pos_gx + 25 < x[4] + ancho_bala) or (pos_gx < x[4] + ancho_bala and pos_gx > x[4]))) and ((pos_gy <= y + alto_bala and pos_gy + yg > y + alto_bala) or (pos_gy < y and pos_gy + yg - 23 > y) or (pos_gy > y and pos_gy + yg < y + alto_bala)):       #Condicional para evaluar la posición del globo con respecto a las balas. Si el globo toca alguna bala, el jugador habrá perdido.
                pygame.mixer.music.load('cuak.mp3')   #Se reproduce el sonido para cuando pierde el jugador.
                pygame.mixer.music.play(1)     #El sonido se reproduce una sola vez.
                boom(pos_gx - 22, pos_gy - 10, x[0], x[1], x[2], x[3], x[4], y, segundos, puntos)   #Se llama a la función boom() para cambiar terminar el juego y mostrar la pantalla de cuando el jugador ha perdido.
                siguiente = True   #Si siguiente es igual a True, se rompe el while.
            if y > 600:  #Condicional para cuando las balas terminan de caer.
                for i in range(5):  #Un for para conseguir definir las nuevas posiciones en 'x' de las balas.
                    x[i] = random.randrange(0, 800 - ancho_bala)   #Cada posición en 'x' de las balas vuelve a cambiar a un valor aleatorio entre el ancho de la pantalla.
                y = -alto_bala   #Se reinicia la posición en 'y' de las balas para que caigan de nuevo.
                velocidad += 1    #Por cada vez que caigan las balas, la velocidad incrementará.
            pygame.display.update()    #Mientras se siga dentro del while, esta función actualizará la pantalla.
            reloj.tick(60)    #Candidad de frames por segundo.

    while True:   #Mientras la ventana siga abierta, el juego seguirá corriendo.
        menu()   #El juego comenzará en el menú.

juego()   #Se continúa con el juego todo el tiempo, hasta que se cierre la ventana.
