
import sys
from PyQt5.QtWidgets import QApplication
from Adnan_cnc_postprocessor_industrial.Military_Grade_UI.Core_Interface.aerospace_main_window import AerospaceMainWindow
from Quantum_Core_Engine.Performance_Acceleration.quantum_cache_system import QuantumCache
from Enterprise_Support_System.Global_Integration.quantum_entanglement_comm import QuantumCommSystem

class IndustrialApplication:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.cache = QuantumCache()
        self.cache.load()
        # Only pass the key if QuantumCommSystem expects it in its __init__
        self.comm = QuantumCommSystem()  # or QuantumCommSystem(b"adnan_industrial_secret_key")
        self.main_window = AerospaceMainWindow(self.cache, self.comm)
        
    def run(self):
        self.main_window.showMaximized()
        sys.exit(self.app.exec_())
    
    def shutdown(self):
        self.cache.save()
        self.comm.close()
        print("Industrial system shutdown complete")

if __name__ == "__main__":
    cnc_app = None
    try:
        cnc_app = IndustrialApplication()
        cnc_app.run()
    except Exception as e:
        print(f"Critical error: {str(e)}")
    finally:
        if cnc_app is not None:
            cnc_app.shutdown()
