import ezdxf

class IndustrialDXFWriter:
    def __init__(self):
        self.doc = ezdxf.new('R12')
        self.doc.header['$INSUNITS'] = 4  # Millimeters
    
    def add_layer(self, name, color=7):
        if name not in self.doc.layers:
            self.doc.layers.new(name, dxfattribs={'color': color})
    
    def add_polyline(self, points, layer='OUTLINE'):
        msp = self.doc.modelspace()
        msp.add_lwpolyline(points, dxfattribs={'layer': layer})
    
    def save(self, filename):
        self.doc.saveas(filename)