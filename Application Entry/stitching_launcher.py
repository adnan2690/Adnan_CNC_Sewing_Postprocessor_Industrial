import sys
from Military_Grade_UI.Core_Interface.aerospace_main_window import AerospaceMainWindow
from Quantum_Core_Engine.Stitch_Processing.hyperspeed_gcode_engine import IndustrialGCodeGenerator

class StitchingApplication:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = AerospaceMainWindow()
        self.gcode_generator = IndustrialGCodeGenerator()
    
    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    app = StitchingApplication()
    app.run()