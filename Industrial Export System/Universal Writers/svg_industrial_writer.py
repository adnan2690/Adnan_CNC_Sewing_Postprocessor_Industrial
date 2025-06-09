class SVGWriter:
    def generate(self, geometry):
        svg = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000">']
        
        if geometry.geom_type == 'LineString':
            points = " ".join([f"{x},{y}" for x, y in geometry.coords])
            svg.append(f'<polyline points="{points}" fill="none" stroke="blue"/>')
        elif geometry.geom_type == 'Polygon':
            points = " ".join([f"{x},{y}" for x, y in geometry.exterior.coords])
            svg.append(f'<polygon points="{points}" fill="none" stroke="black"/>')
        
        svg.append('</svg>')
        return "\n".join(svg)