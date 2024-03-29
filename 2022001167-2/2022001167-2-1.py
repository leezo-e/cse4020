import numpy as np
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# 프로그램을 돌릴 때 초기 상태는 KEY4와 같음. 전역변수로 primitive type 선언
primitive_type = GL_LINE_LOOP 

def key_callback(window, key, scancode, action, mods):
    global primitive_type
    if action == glfw.PRESS:
        if key == glfw.KEY_1:
            primitive_type = GL_POINTS
        elif key == glfw.KEY_2:
            primitive_type = GL_LINES
        elif key == glfw.KEY_3:
            primitive_type = GL_LINE_STRIP
        elif key == glfw.KEY_4:
            primitive_type = GL_LINE_LOOP
        elif key == glfw.KEY_5:
            primitive_type = GL_TRIANGLES
        elif key == glfw.KEY_6:
            primitive_type = GL_TRIANGLE_STRIP
        elif key == glfw.KEY_7:
            primitive_type = GL_TRIANGLE_FAN
        elif key == glfw.KEY_8:
            primitive_type = GL_QUADS
        elif key == glfw.KEY_9:
            primitive_type = GL_QUAD_STRIP
        elif key == glfw.KEY_0:
            primitive_type = GL_POLYGON


def render():
    glClear(GL_COLOR_BUFFER_BIT)
    angle = np.linspace(0, 2*np.pi, 12, False)
    vertices = np.column_stack((np.cos(angle), np.sin(angle)))
    
    glBegin(primitive_type)
    for vertex in vertices:
        glVertex2fv(vertex)
    glEnd()


def main():
    window_title = "2022001167-2-1"

    if not glfw.init():
        return
    
    window = glfw.create_window(480, 480, window_title, None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    while not glfw.window_should_close(window):
        render()
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__" :
    main()