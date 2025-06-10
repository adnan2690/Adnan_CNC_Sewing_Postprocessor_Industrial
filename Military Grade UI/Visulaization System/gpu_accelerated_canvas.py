from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtGui import QOpenGLShaderProgram, QOpenGLShader
from OpenGL.GL import *
import numpy as np

class IndustrialCanvas(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.path_data = None
        self.jump_data = None
        self.zoom = 1.0
        self.pan = [0.0, 0.0]
        
    def initializeGL(self):
        # Initialize shader pipeline
        self.shader_program = QOpenGLShaderProgram()
        self.shader_program.addShaderFromSourceCode(
            QOpenGLShader.Vertex,
            """
            #version 330 core
            layout(location = 0) in vec3 position;
            layout(location = 1) in vec3 color;
            uniform mat4 matrix;
            out vec3 fragColor;
            void main() {
                gl_Position = matrix * vec4(position, 1.0);
                fragColor = color;
            }
            """
        )
        self.shader_program.addShaderFromSourceCode(
            QOpenGLShader.Fragment,
            """
            #version 330 core
            in vec3 fragColor;
            out vec4 outColor;
            void main() {
                outColor = vec4(fragColor, 1.0);
            }
            """
        )
        self.shader_program.link()
        
        # Create GPU buffers
        self.path_vbo = glGenBuffers(1)
        self.jump_vbo = glGenBuffers(1)
        
        # Configure OpenGL
        glClearColor(0.95, 0.95, 0.95, 1.0)
        glEnable(GL_LINE_SMOOTH)
        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
        glLineWidth(2.0)
    
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.shader_program.bind()
        
        # Set transformation matrix
        matrix = QMatrix4x4()
        matrix.ortho(-self.zoom + self.pan[0], self.zoom + self.pan[0], 
                     -self.zoom + self.pan[1], self.zoom + self.pan[1], 
                     -1, 1)
        self.shader_program.setUniformValue("matrix", matrix)
        
        # Render paths
        if self.path_data is not None:
            glBindBuffer(GL_ARRAY_BUFFER, self.path_vbo)
            glEnableVertexAttribArray(0)
            glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
            glEnableVertexAttribArray(1)
            glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
            glDrawArrays(GL_LINE_STRIP, 0, len(self.path_data) // 6)
        
        # Render jumps
        if self.jump_data is not None:
            glBindBuffer(GL_ARRAY_BUFFER, self.jump_vbo)
            glEnableVertexAttribArray(0)
            glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
            glEnableVertexAttribArray(1)
            glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
            glLineStipple(1, 0x00FF)
            glEnable(GL_LINE_STIPPLE)
            glDrawArrays(GL_LINES, 0, len(self.jump_data) // 6)
            glDisable(GL_LINE_STIPPLE)
        
        glBindBuffer(GL_ARRAY_BUFFER, 0)
        self.shader_program.release()
    
    def load_paths(self, paths, color=(0.1, 0.3, 0.8)):
        """Load industrial path data to GPU"""
        data = []
        for path in paths:
            for point in path:
                data.extend([point[0], point[1], 0])  # Position
                data.extend(color)                    # Color
        
        self.path_data = np.array(data, dtype=np.float32)
        
        glBindBuffer(GL_ARRAY_BUFFER, self.path_vbo)
        glBufferData(GL_ARRAY_BUFFER, self.path_data.nbytes, self.path_data, GL_STATIC_DRAW)
        self.update()
    
    def load_jumps(self, jumps, color=(0.8, 0.1, 0.1)):
        """Load industrial jump data to GPU"""
        data = []
        for start, end in jumps:
            data.extend([start[0], start[1], 0])  # Start position
            data.extend(color)                     # Color
            data.extend([end[0], end[1], 0])       # End position
            data.extend(color)                     # Color
        
        self.jump_data = np.array(data, dtype=np.float32)
        
        glBindBuffer(GL_ARRAY_BUFFER, self.jump_vbo)
        glBufferData(GL_ARRAY_BUFFER, self.jump_data.nbytes, self.jump_data, GL_STATIC_DRAW)
        self.update()
    
    def wheelEvent(self, event):
        """Industrial zoom control"""
        zoom_factor = 1.1
        if event.angleDelta().y() > 0:
            self.zoom /= zoom_factor
        else:
            self.zoom *= zoom_factor
        self.zoom = max(0.1, min(self.zoom, 100.0))
        self.update()
    
    def mouseMoveEvent(self, event):
        """Industrial pan control"""
        if event.buttons() == Qt.LeftButton:
            delta = event.pos() - self.last_mouse_pos
            self.pan[0] += delta.x() * 0.002 * self.zoom
            self.pan[1] -= delta.y() * 0.002 * self.zoom
            self.last_mouse_pos = event.pos()
            self.update()
    
    def mousePressEvent(self, event):
        """Start pan operation"""
        if event.button() == Qt.LeftButton:
            self.last_mouse_pos = event.pos()
