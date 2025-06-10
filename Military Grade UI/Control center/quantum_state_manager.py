from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QHeaderView

class LayerManager(QTreeWidget):
    def __init__(self):
        super().__init__()
        self.setHeaderLabels(["Layer", "Visible", "Locked"])
        self.header().setSectionResizeMode(QHeaderView.ResizeToContents)
        self._setup_layers()
        self._setup_style()
    
    def _setup_layers(self):
        """Initialize industrial layers"""
        layers = [
            ("ORIGINAL", "Original Geometry", True, False),
            ("SEAM_ALLOWANCE", "Seam Allowance", True, False),
            ("STITCH_SLOT", "Stitch Slot", True, True),
            ("BOUNDARY", "Material Boundary", False, False),
            ("ANNOTATIONS", "Annotations", True, False)
        ]
        
        for id, name, visible, locked in layers:
            item = QTreeWidgetItem(self)
            item.setText(0, name)
            item.setCheckState(1, Qt.Checked if visible else Qt.Unchecked)
            item.setCheckState(2, Qt.Checked if locked else Qt.Unchecked)
            item.setData(0, Qt.UserRole, id)
    
    def _setup_style(self):
        """Apply aerospace styling"""
        self.setStyleSheet("""
            QTreeWidget {
                background-color: #2c3e50;
                color: #ecf0f1;
                border: none;
            }
            QHeaderView::section {
                background-color: #3498db;
                color: white;
                padding: 4px;
                border: none;
            }
        """)
    
    def get_visible_layers(self):
        """Get list of visible layers"""
        visible = []
        for i in range(self.topLevelItemCount()):
            item = self.topLevelItem(i)
            if item.checkState(1) == Qt.Checked:
                visible.append(item.data(0, Qt.UserRole))
        return visible
