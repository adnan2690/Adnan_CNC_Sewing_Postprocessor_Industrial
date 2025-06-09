from PyQt5.QtWidgets import QMainWindow, QTabWidget

class AerospaceMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Adnan CNC Industrial Sewing Suite")
        self.setGeometry(100, 100, 1200, 800)
        
        # Create tab interface
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        
        # Industrial styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2c3e50;
            }
            QTabWidget::pane {
                border: 1px solid #34495e;
                background: #34495e;
            }
            QTabBar::tab {
                background: #2c3e50;
                color: #ecf0f1;
                padding: 10px;
                border: 1px solid #34495e;
            }
            QTabBar::tab:selected {
                background: #3498db;
            }
        """)
    
    def add_tab(self, widget, title):
        """Add industrial-grade tab"""
        self.tabs.addTab(widget, title)