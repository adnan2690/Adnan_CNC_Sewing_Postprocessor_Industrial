class LODManager:
    def adjust_detail(self, geometry, zoom_level):
        """Adjust level of detail based on zoom"""
        if zoom_level < 0.5:
            return geometry.simplify(1.0)
        elif zoom_level < 1.0:
            return geometry.simplify(0.5)
        else:
            return geometry