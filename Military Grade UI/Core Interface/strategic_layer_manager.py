class LayerManager:
    LAYERS = ["ORIGINAL", "SEAM_ALLOWANCE", "STITCH_SLOT", "BOUNDARY"]
    
    def __init__(self):
        self.layers = {name: [] for name in self.LAYERS}
        self.visible = {name: True for name in self.LAYERS}
    
    def add_to_layer(self, layer, geometry):
        if layer in self.layers:
            self.layers[layer].append(geometry)
    
    def set_visibility(self, layer, visible):
        if layer in self.visible:
            self.visible[layer] = visible