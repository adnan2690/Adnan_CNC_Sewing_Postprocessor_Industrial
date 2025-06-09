from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtGui import QOpenGLShaderProgram, QOpenGLShader, QOpenGLBuffer
from OpenGL.GL import *
import numpy as np

class IndustrialCanvas(QOpenGLWidget):
    def initializeGL(self):
        # Initialize shader pipeline
        self.shader_program = QOpenGLShaderProgram()
        self.shader_program.addShaderFromSourceCode(QOpenGLShader.Vertex, """
            #version 330 core
            in vec3 position;
            in vec3 color;
            out vec3 fragColor;
            void main() {
                gl_Position = vec4(position, 1.0);
                fragColor = color;
            }
        """)
        self.shader_program.addShaderFromSourceCode(QOpenGLShader.Fragment, """
            #version 330 core
            in vec3 fragColor;
            out vec4 outColor;
            void main() {
                outColor = vec4(fragColor, 1.0);
            }
        """)
        self.shader_program.link()
        
        # Create GPU buffers
        self.path_vbo = QOpenGLBuffer()
        self.path_vbo.create()
        
        # Configure OpenGL
        glClearColor(0.95, 0.95, 0.95, 1.0)
        glEnable(GL_LINE_SMOOTH)
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
        glLineWidth(1.5)
    
    def load_paths(self, paths):
        data = []
        for path in paths:
            for x, y in path.coords:
                data.extend([x, y, 0])  # Position
                data.extend([0.1, 0.3, 0.8])  # Blue color
        self.path_data = np.array(data, dtype=np.float32)
        
        self.path_vbo.bind()
        self.path_vbo.allocate(self.path_data.tobytes(), self.path_data.nbytes)
        self.path_vbo.release()
    
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.shader_program.bind()
        
        if hasattr(self, 'path_data'):
            self.path_vbo.bind()
            loc = self.shader_program.attributeLocation("position")
            self.shader_program.enableAttributeArray(loc)
            self.shader_program.setAttributeBuffer(loc, GL_FLOAT, 0, 3, 24)
            
            loc = self.shader_program.attributeLocation("color")
            self.shader_program.enableAttributeArray(loc)
            self.shader_program.setAttributeBuffer(loc, GL_FLOAT, 12, 3, 24)
            
            glDrawArrays(GL_LINE_STRIP, 0, len(self.path_data)//6)
            self.path_vbo.release()
        
        self.shader_program.release()