from PyQt5.QtWidgets import (
    QMainWindow, QTabWidget, QDockWidget, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QLabel, QStatusBar, QSplitter,
    QSlider, QCheckBox, QTextEdit, QProgressBar, QListWidget,
    QStackedWidget  # Added missing widget imports
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon, QFont

class AerospaceMainWindow(QMainWindow):
    def __init__(self, cache=None, comm=None):
        super().__init__()
        self.cache = cache
        self.comm = comm
        
        # Industrial window settings
        self.setWindowTitle("Adnan CNC Industrial Sewing Suite")
        self.setWindowIcon(QIcon(":/icons/industrial_icon.png"))
        self.setGeometry(100, 100, 1600, 900)
        
        # Create aerospace layout
        self._create_main_layout()
        self._create_toolbars()
        self._create_status_bar()
        self._create_docking_panels()
        
        # Apply military-grade styling
        self._apply_industrial_style()
    
    def _create_main_layout(self):
        """Create aerospace-inspired main layout"""
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(5)
        
        # Create tab system for industrial modules
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.setMovable(True)
        
        # Add tab placeholders (will be populated by other modules)
        self.tabs.addTab(self._create_stitching_tab(), "Stitching")
        self.tabs.addTab(self._create_template_tab(), "Template/Cutter")
        self.tabs.addTab(self._create_machine_tab(), "Machine Control")
        
        main_layout.addWidget(self.tabs)
        self.setCentralWidget(main_widget)
    
    def _create_stitching_tab(self):
        """Stitching processor tab"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Toolbar section
        toolbar_layout = QHBoxLayout()
        self.stitch_tools = {
            "import": QPushButton(QIcon(":/icons/import.png"), "Import Design"),
            "straight": QPushButton(QIcon(":/icons/straight.png"), "Straight"),
            "zigzag": QPushButton(QIcon(":/icons/zigzag.png"), "Zigzag"),
            "triple": QPushButton(QIcon(":/icons/triple.png"), "Triple"),
            "lock": QPushButton(QIcon(":/icons/lock.png"), "Lock Stitch"),
            "generate": QPushButton(QIcon(":/icons/generate.png"), "Generate G-code")
        }
        
        for tool in self.stitch_tools.values():
            toolbar_layout.addWidget(tool)
            tool.setFixedSize(120, 40)
        
        layout.addLayout(toolbar_layout)
        
        # Visualization canvas area
        splitter = QSplitter(Qt.Horizontal)
        
        # Parameters panel (left)
        params_panel = QWidget()
        params_layout = QVBoxLayout(params_panel)
        
        # Industrial parameter controls
        params_layout.addWidget(QLabel("STITCH PARAMETERS"))
        self.stitch_params = {
            "density": self._create_slider("Density (stitches/mm)", 1, 10, 4),
            "length": self._create_slider("Stitch Length (mm)", 0.5, 5, 2.5),
            "width": self._create_slider("Width (mm)", 0.5, 10, 3),
            "tackle": self._create_slider("Tackle Length (mm)", 0, 10, 3)
        }
        
        for param in self.stitch_params.values():
            params_layout.addWidget(param)
        
        # Canvas area (right)
        # Commented out for now since we don't have the module
        # from ..Visualization_System.gpu_accelerated_canvas import IndustrialCanvas
        # self.canvas = IndustrialCanvas()
        self.canvas = QLabel("Canvas Area - GPU Accelerated Visualization")  # Placeholder
        
        splitter.addWidget(params_panel)
        splitter.addWidget(self.canvas)
        splitter.setSizes([300, 1200])
        
        layout.addWidget(splitter)
        return tab
    
    def _create_template_tab(self):
        """Template/cutter processor tab"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Industrial toolbar
        toolbar_layout = QHBoxLayout()
        self.template_tools = {
            "import": QPushButton(QIcon(":/icons/import.png"), "Import Design"),
            "select": QPushButton(QIcon(":/icons/select.png"), "Select"),
            "move": QPushButton(QIcon(":/icons/move.png"), "Move"),
            "rotate": QPushButton(QIcon(":/icons/rotate.png"), "Rotate"),
            "mirror": QPushButton(QIcon(":/icons/mirror.png"), "Mirror"),
            "offset": QPushButton(QIcon(":/icons/offset.png"), "Generate Offset"),
            "nest": QPushButton(QIcon(":/icons/nest.png"), "Auto-Nest"),
            "export": QPushButton(QIcon(":/icons/export.png"), "Export")
        }
        
        for tool in self.template_tools.values():
            toolbar_layout.addWidget(tool)
            tool.setFixedSize(120, 40)
        
        layout.addLayout(toolbar_layout)
        
        # Template workspace
        splitter = QSplitter(Qt.Horizontal)
        
        # Layer management panel
        layer_panel = QWidget()  # Changed from QDockWidget to QWidget
        layer_layout = QVBoxLayout(layer_panel)
        
        # Layer checkboxes
        self.layers = {
            "ORIGINAL": self._create_layer_checkbox("Original Geometry", True),
            "SEAM_ALLOWANCE": self._create_layer_checkbox("Seam Allowance", True),
            "STITCH_SLOT": self._create_layer_checkbox("Stitch Slot", True),
            "BOUNDARY": self._create_layer_checkbox("Boundary", False)
        }
        
        for layer in self.layers.values():
            layer_layout.addWidget(layer)
        
        # Material and sheet setup
        material_panel = QWidget()
        material_layout = QVBoxLayout(material_panel)
        material_layout.addWidget(QLabel("MATERIAL SETUP"))
        
        # Industrial material parameters
        self.material_params = {
            "width": self._create_slider("Material Width (mm)", 500, 2000, 1500),
            "height": self._create_slider("Material Height (mm)", 500, 3000, 2500),
            "seam": self._create_slider("Seam Allowance (mm)", 5, 20, 10),
            "foot": self._create_slider("Foot Extension (mm)", 2, 10, 5)
        }
        
        for param in self.material_params.values():
            material_layout.addWidget(param)
        
        # Canvas area
        # Commented out for now since we don't have the module
        # from ..Visualization_System.gpu_accelerated_canvas import IndustrialCanvas
        # self.template_canvas = IndustrialCanvas()
        self.template_canvas = QLabel("Template Canvas Area")  # Placeholder
        
        splitter.addWidget(layer_panel)
        splitter.addWidget(material_panel)
        splitter.addWidget(self.template_canvas)
        splitter.setSizes([200, 300, 1000])
        
        layout.addWidget(splitter)
        return tab
    
    def _create_machine_tab(self):
        """Machine control center"""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        
        # Machine control toolbar
        toolbar_layout = QHBoxLayout()
        self.machine_tools = {
            "connect": QPushButton(QIcon(":/icons/connect.png"), "Connect"),
            "home": QPushButton(QIcon(":/icons/home.png"), "Home"),
            "run": QPushButton(QIcon(":/icons/run.png"), "Run Job"),
            "pause": QPushButton(QIcon(":/icons/pause.png"), "Pause"),
            "resume": QPushButton(QIcon(":/icons/resume.png"), "Resume"),
            "stop": QPushButton(QIcon(":/icons/stop.png"), "Stop"),
            "estop": QPushButton(QIcon(":/icons/estop.png"), "E-Stop")
        }
        
        for tool in self.machine_tools.values():
            tool.setFixedSize(120, 40)
            tool.setStyleSheet("background-color: #2c3e50; color: white;")
            toolbar_layout.addWidget(tool)
        
        # Make E-Stop red
        self.machine_tools["estop"].setStyleSheet(
            "background-color: #e74c3c; color: white; font-weight: bold;"
        )
        
        layout.addLayout(toolbar_layout)
        
        # Machine status display
        status_layout = QHBoxLayout()
        
        # Machine vitals panel
        vitals_panel = QWidget()
        vitals_layout = QVBoxLayout(vitals_panel)
        vitals_layout.addWidget(QLabel("MACHINE VITALS"))
        
        self.vital_indicators = {
            "needle": self._create_status_indicator("Needle Position", "UP"),
            "clamp": self._create_status_indicator("Clamp Status", "OPEN"),
            "tension": self._create_status_indicator("Thread Tension", "NORMAL"),
            "temp": self._create_status_indicator("Motor Temp", "32°C")
        }
        
        for indicator in self.vital_indicators.values():
            vitals_layout.addWidget(indicator)
        
        # G-code terminal
        terminal_panel = QWidget()
        terminal_layout = QVBoxLayout(terminal_panel)
        terminal_layout.addWidget(QLabel("G-CODE TERMINAL"))
        
        # Industrial terminal display
        self.terminal = QTextEdit()
        self.terminal.setFont(QFont("Courier", 10))
        self.terminal.setReadOnly(True)
        self.terminal.setStyleSheet("background-color: #1a1a1a; color: #00ff00;")
        
        terminal_layout.addWidget(self.terminal)
        
        status_layout.addWidget(vitals_panel, 1)
        status_layout.addWidget(self.terminal, 3)
        
        layout.addLayout(status_layout)
        return tab
    
    def _create_docking_panels(self):
        """Create industrial docking panels"""
        # Left: Layer manager
        layer_dock = QDockWidget("Strategic Layer Control", self)
        layer_dock.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable)
        layer_widget = QWidget()
        layer_layout = QVBoxLayout(layer_widget)
        
        self.layer_list = QListWidget()
        self.layer_list.addItems(["ORIGINAL", "SEAM_ALLOWANCE", "STITCH_SLOT", "BOUNDARY"])
        
        layer_layout.addWidget(self.layer_list)
        layer_dock.setWidget(layer_widget)
        self.addDockWidget(Qt.LeftDockWidgetArea, layer_dock)
        
        # Right: Tool settings
        tools_dock = QDockWidget("Industrial Tool Settings", self)
        tools_widget = QWidget()
        tools_layout = QVBoxLayout(tools_widget)
        
        self.tool_settings = QStackedWidget()
        tools_layout.addWidget(self.tool_settings)
        tools_dock.setWidget(tools_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, tools_dock)
    
    def _create_status_bar(self):
        """Create military-grade status bar"""
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        
        # Industrial status indicators
        self.status_indicators = {
            "machine": QLabel("Machine: DISCONNECTED"),
            "material": QLabel("Material: NONE"),
            "progress": QProgressBar(),
            "fps": QLabel("FPS: 60")
        }
        
        # Style indicators
        self.status_indicators["machine"].setStyleSheet(
            "background-color: #e74c3c; color: white; padding: 2px;"
        )
        self.status_indicators["fps"].setStyleSheet(
            "background-color: #2c3e50; color: white; padding: 2px;"
        )
        self.status_indicators["progress"].setMaximumWidth(200)
        
        # Add to status bar
        status_bar.addPermanentWidget(self.status_indicators["machine"], 1)
        status_bar.addPermanentWidget(self.status_indicators["material"], 1)
        status_bar.addPermanentWidget(self.status_indicators["progress"], 2)
        status_bar.addPermanentWidget(self.status_indicators["fps"], 1)
        
        # Initial status
        self.update_status("System initialized", 5000)
    
    def _apply_industrial_style(self):
        """Apply aerospace-inspired styling"""
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
                font-weight: bold;
            }
            QTabBar::tab:selected {
                background: #3498db;
                color: #ffffff;
            }
            QDockWidget {
                background: #2c3e50;
                color: #ecf0f1;
                border: 1px solid #34495e;
            }
            QDockWidget::title {
                background: #3498db;
                padding: 6px;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 8px;
                font-weight: bold;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1c638e;
            }
            QLabel {
                color: #ecf0f1;
                font-weight: bold;
            }
            QSlider::groove:horizontal {
                height: 8px;
                background: #34495e;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #3498db;
                border: 1px solid #2980b9;
                width: 18px;
                margin: -6px 0;
                border-radius: 9px;
            }
            QSlider::add-page:horizontal {
                background: #2c3e50;
            }
            QSlider::sub-page:horizontal {
                background: #3498db;
            }
        """)
    
    # Helper methods
    def _create_slider(self, label, min_val, max_val, default):
        """Create industrial parameter slider"""
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(QLabel(label))
        
        slider = QSlider(Qt.Horizontal)
        slider.setRange(min_val * 10, max_val * 10)
        slider.setValue(default * 10)
        slider.setTickPosition(QSlider.TicksBelow)
        slider.setTickInterval(10)
        
        value_label = QLabel(f"{default} mm")
        slider.valueChanged.connect(
            lambda val: value_label.setText(f"{val/10:.1f} mm")
        )
        
        layout.addWidget(slider)
        layout.addWidget(value_label)
        return container
    
    def _create_layer_checkbox(self, text, checked):
        """Create layer visibility checkbox"""
        checkbox = QCheckBox(text)
        checkbox.setChecked(checked)
        checkbox.setStyleSheet("color: #ecf0f1;")
        return checkbox
    
    def _create_status_indicator(self, label, value):
        """Create machine status indicator"""
        container = QWidget()
        layout = QHBoxLayout(container)
        layout.addWidget(QLabel(label))
        
        value_label = QLabel(value)
        value_label.setAlignment(Qt.AlignRight)
        value_label.setStyleSheet("""
            background-color: #27ae60; 
            color: white; 
            padding: 4px;
            border-radius: 4px;
        """)
        
        layout.addWidget(value_label)
        return container
    
    def update_status(self, message, timeout=0):
        """Update status bar message"""
        self.statusBar().showMessage(f"INDUSTRIAL CNC: {message}", timeout)
    
    def safe_shutdown(self):
        """Industrial-grade shutdown procedure"""
        self.update_status("System shutting down...")
        # Save state, disconnect from machine, etc.
