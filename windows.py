import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import time


CUBE_POS_1 = (-2, 2, -10)
CUBE_POS_2 = (2, -2, -10)
CUBE_POS_3 = (0, 0, -8)

VERTICES = (
    (1, 0, 0),
    (0, 1, 0),
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
    (1, 1, 1),
    (-1, 1, 1),
    (-1, -1, 1),
    (1, -1, 1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, -1),
)

COLORS = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 1),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 0),
    (0, 0, 0),
    (0.5, 0.5, 0.5),
)

FACES = (
    (0, 1, 6), (0, 6, 9), (0, 9, 4),
    (1, 2, 7), (1, 7, 6), (2, 3, 8),
    (2, 13, 12), (2, 12, 7), (3, 10, 8),
    (3, 11, 10), (3, 4, 11), (4, 5, 13),
    (5, 9, 13), (5, 4, 9), (7, 12, 6),
    (11, 12, 10), (11, 6, 12), (10, 6, 8),
)

def Cube1():
    glPushMatrix()
    glTranslate(CUBE_POS_1[0], CUBE_POS_1[1], CUBE_POS_1[2])
    glRotatef(pygame.time.get_ticks() / 10, 1, 0, 0)
    glRotatef(pygame.time.get_ticks() / 10, 0, 1, 0)
    glRotatef(pygame.time.get_ticks() / 10, 0, 0, 1)
    glBegin(GL_TRIANGLES)
    glColor3fv((1, 1, 1))
    for face in FACES:
        for vertex in face:
            glVertex3fv(VERTICES[vertex])
    glEnd()
    glPopMatrix()

def Cube2():
    glPushMatrix()
    glTranslate(CUBE_POS_2[0], CUBE_POS_2[1], CUBE_POS_2[2])
    glRotatef(pygame.time.get_ticks() / 8, 1, 0, 0)
    glRotatef(pygame.time.get_ticks() / 8, 0, 1, 0)
    glRotatef(pygame.time.get_ticks() / 8, 0, 0, 1)
    glBegin(GL_TRIANGLES)
    glColor3fv((1, 1, 0))
    for face in FACES:
        for vertex in face:
            glVertex3fv(VERTICES[vertex])
    glEnd()
    glPopMatrix()

def Cube3():
    glPushMatrix()
    glTranslate(CUBE_POS_3[0], CUBE_POS_3[1], CUBE_POS_3[2])
    glRotatef(pygame.time.get_ticks() / 8, 1, 0, 0)
    glRotatef(pygame.time.get_ticks() / 8, 0, 1, 0)
    glRotatef(pygame.time.get_ticks() / 8, 0, 0, 1)
    glBegin(GL_TRIANGLES)
    for i, face in enumerate(FACES):
        if i >= len(COLORS):
            break
        glColor3fv(COLORS[i])
        for vertex in face:
            glVertex3fv(VERTICES[vertex])
    glEnd()
    glPopMatrix()

def main():
    pygame.init()
    display = (800, 600)

    # 创建两个窗口
    window1 = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    window2 = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    clock = pygame.time.Clock()

    pygame.display.set_caption("GPU Benchmark")
    icon = pygame.image.load("icon.ico")
    pygame.display.set_icon(icon)

    frame_timestamps = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(0.1, 0, 0, 1)

        # 渲染第一个窗口
        window1_id = pygame.display.get_wm_info()['window']
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL, window1_id)
        Cube1()
        Cube2()
        Cube3()
        pygame.display.flip()

        # 渲染第二个窗口
        window2_id = pygame.display.get_wm_info()['window']
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL, window2_id)
        Cube1()
        Cube2()
        Cube3()
        pygame.display.flip()

        # 每秒记录帧率并写入文件
        current_time = pygame.time.get_ticks() / 1000
        frame_timestamps.append(current_time)
        if current_time - frame_timestamps[0] >= 1:
            fps = len(frame_timestamps) / (current_time - frame_timestamps[0])
            with open("fps.txt", "a") as f:
                f.write(str(fps) + "\n")
            frame_timestamps.pop(0)

        clock.tick(10000)

if __name__ == '__main__':
    main()