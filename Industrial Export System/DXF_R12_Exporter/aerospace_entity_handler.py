class EntityHandler:
    def convert_to_dxf_entities(self, geometry):
        """Convert industrial geometry to DXF entities"""
        if geometry.geom_type == 'LineString':
            return {'type': 'LWPOLYLINE', 'points': list(geometry.coords)}
        elif geometry.geom_type == 'Polygon':
            return {
                'type': 'POLYGON',
                'exterior': list(geometry.exterior.coords),
                'interiors': [list(interior.coords) for interior in geometry.interiors]
            }