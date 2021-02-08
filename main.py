import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

##Vertices 0-7  (x,y,z)
vertices= ( 
    (3, -.4, -1.5),
    (3, .4, -1.5),
    (-3, .4, -1.5),
    (-3, -.4, -1.5),
    (3, -.4, 1.5),
    (3, .4, 1.5),
    (-3, .4, 1.5),
    (-3, -.4, 1.5)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,6),
    (5,1),
    (5,4),
    (5,6),
    (7,3),
    (7,4),
    (7,6)
)

surfaces = (   
    (0,1,2,3),
    (4,5,6,7),
    (1,5,4,0),
    (3,2,6,7),
    (1,2,6,5),
    (0,3,7,4)
)

colors = (
    ((1.0/255*41),(1.0/255*217),(1.0/255*152)),
    ((1.0/255*41),(1.0/255*217),(1.0/255*152)),
    ((1.0/255*242),(1.0/255*66),(1.0/255*128)),
    ((1.0/255*242),(1.0/255*66),(1.0/255*128)),
    ((1.0/255*19),(1.0/255*94),(1.0/255*242)),
    ((1.0/255*19),(1.0/255*94),(1.0/255*242)),      
)

def DrawBoard():
    
    glBegin(GL_QUADS)
    x = 0
    for surface in surfaces:
        
        for vertex in surface:  
            glColor3fv((colors[x]))          
            glVertex3fv(vertices[vertex])
        x += 1
    glEnd()
    
def main():
    pygame.init()
    display = (640,480)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    glClearColor((1.0/255*46),(1.0/255*45),(1.0/255*64),1)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    gluPerspective(100, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glRotatef(5, 0, 1, 0)
                if event.key == pygame.K_RIGHT:
                    glRotatef(-5, 0, 1, 0)

                if event.key == pygame.K_UP:
                    glRotatef(-5, 1, 0, 0)
                if event.key == pygame.K_DOWN:
                    glRotatef(5, 1, 0, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)

                if event.button == 5:
                    glTranslatef(0,0,-1.0)
        glRotatef(1, 3, 1, 1)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        DrawBoard()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__': main()