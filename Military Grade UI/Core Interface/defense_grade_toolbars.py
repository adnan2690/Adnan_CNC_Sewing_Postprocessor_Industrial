from PyQt5.QtWidgets import QToolBar, QAction
from PyQt5.QtGui import QIcon

class IndustrialToolbar(QToolBar):
    def __init__(self, title):
        super().__init__(title)
        self.setMovable(False)
        self.setStyleSheet("""
            QToolBar {
                background-color: #34495e;
                border: none;
                padding: 5px;
            }
            QToolButton {
                background-color: #2c3e50;
                color: #ecf0f1;
                border-radius: 4px;
                padding: 5px;
                margin: 2px;
            }
            QToolButton:hover {
                background-color: #3498db;
            }
        """)
    
    def add_tool(self, icon_path, tooltip, callback):
        action = QAction(QIcon(icon_path), tooltip, self)
        action.triggered.connect(callback)
        self.addAction(action)
        return action