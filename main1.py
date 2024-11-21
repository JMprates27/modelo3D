import pygame as pg
import moderngl as mgl
import sys

class GraphicsEngine:
    def __init__(self, win_size=(1600, 900)):

        #inicia modulos do pygame
        pg.init()
        #tamanho da janela
        self.WIN_SIZE = win_size
        #define atributos do opengl
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        #cria o contexto do opengl
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        #detecta e usa o contexto existente do opengl
        self.ctx = mgl.create_context()
        #cria um objeto para acompanhar o tempo
        self.clock = pg.time.Clock()

    def verifica_eventos(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def renderiza(self):
        #define a cor da tela
        self.ctx.clear(color=(0.07, 0.15, 0.17))
        #inverte os buffers
        pg.display.flip()

    def roda(self):
        while True:
            self.verifica_eventos()
            self.renderiza()
            self.clock.tick(60)

if __name__ == '__main__':
    app = GraphicsEngine()
    app.roda()

