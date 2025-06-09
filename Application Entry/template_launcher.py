import sys
from Military_Grade_UI.Core_Interface.aerospace_main_window import AerospaceMainWindow
from Industrial_Export_System.DXF_R12_Exporter.iso_compliant_dxf_writer import IndustrialDXFWriter

class TemplateApplication:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_window = AerospaceMainWindow()
        self.dxf_writer = IndustrialDXFWriter()
    
    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    app = TemplateApplication()
    app.run()