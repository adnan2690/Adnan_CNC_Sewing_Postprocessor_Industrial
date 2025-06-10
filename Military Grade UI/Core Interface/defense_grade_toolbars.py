from PyQt5.QtWidgets import QToolBar, QAction, QComboBox, QLabel
from PyQt5.QtGui import QIcon

class IndustrialToolbar(QToolBar):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setMovable(False)
        self.setIconSize(QSize(32, 32))
        self._setup_style()
    
    def _setup_style(self):
        """Apply defense-grade styling"""
        self.setStyleSheet("""
            QToolBar {
                background-color: #34495e;
                border: none;
                padding: 5px;
                spacing: 5px;
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
            QComboBox {
                background-color: #2c3e50;
                color: #ecf0f1;
                border: 1px solid #3498db;
                padding: 5px;
                min-width: 120px;
            }
        """)
    
    def add_tool(self, icon_path, tooltip, callback):
        """Add industrial tool"""
        action = QAction(QIcon(icon_path), tooltip, self)
        action.triggered.connect(callback)
        self.addAction(action)
        return action
    
    def add_combo(self, label, items, callback):
        """Add industrial combobox"""
        self.addWidget(QLabel(label))
        combo = QComboBox()
        combo.addItems(items)
        combo.currentIndexChanged.connect(callback)
        self.addWidget(combo)
        return combo
    
    def add_separator(self):
        """Add industrial separator"""
        self.addSeparator()
