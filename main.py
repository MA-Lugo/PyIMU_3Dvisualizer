import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from figure import *
from tkinter import *
from tkinter import ttk

ApplicationGL = False

class PortSettings:
    Name = "COM1"
    Speed = "9600"
    Timeout = 2

myport = PortSettings()


def RunAppliction():
    global ApplicationGL
    myport.Name = Port_entry.get()
    myport.Speed = Baud_entry.get()
    ApplicationGL = True
    ConfWindw.destroy()

ConfWindw = Tk()
ConfWindw.title("Configure Serial Port")
ConfWindw.configure(bg = "#2E2D40") 
ConfWindw.geometry('300x150')
ConfWindw.resizable(width=False, height=False)
positionRight = int(ConfWindw.winfo_screenwidth()/2 - 300/2)
positionDown = int(ConfWindw.winfo_screenheight()/2 - 150/2)
ConfWindw.geometry("+{}+{}".format(positionRight, positionDown))

Port_label = Label(text = "Port:",font =("",12),justify= "right",bg = "#2E2D40",fg = "#FFFFFF")
Port_label.place(x = 50, y =30,anchor = "center")
Port_entry = Entry(width = 20,bg = "#37364D", fg = "#FFFFFF", justify = "center")
Port_entry.insert(INSERT,myport.Name)
Port_entry.place(x = 180, y = 30,anchor = "center")

Baud_label = Label(text = "Speed:",font =("",12),justify= "right",bg = "#2E2D40",fg = "#FFFFFF")
Baud_label.place(x = 50, y =80,anchor = "center")
Baud_entry = Entry(width = 20,bg = "#37364D", fg = "#FFFFFF", justify = "center")
Baud_entry.insert(INSERT,myport.Speed)
Baud_entry.place(x = 180, y = 80,anchor = "center")

ok_button = Button(text = "Ok",width = 8,command = RunAppliction,bg="#135EF2",fg ="#FFFFFF")
ok_button.place(x = 150, y = 120,anchor="center")

def InitPygame():
    global display
    pygame.init()
    display = (640,480)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption('IMU visualizer')


def InitGL():
    glClearColor((1.0/255*46),(1.0/255*45),(1.0/255*64),1)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

    gluPerspective(100, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)

def DrawText(textString):     
    font = pygame.font.SysFont ("Courier New",25, True)
    textSurface = font.render(textString, True, (255,255,0), (46,45,64,255))     
    textData = pygame.image.tostring(textSurface, "RGBA", True)         
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)    

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
    ConfWindw.mainloop()
    if ApplicationGL == True:
        InitPygame()
        InitGL()

        while True:

            glRotatef(1, 3, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            DrawText("My text")
            DrawBoard()
            pygame.display.flip()
            pygame.time.wait(10)


if __name__ == '__main__': main()