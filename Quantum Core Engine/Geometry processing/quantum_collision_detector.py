class CollisionDetector:
    def detect(self, geometry, tool_path):
        """Industrial collision detection"""
        buffer = tool_path.buffer(5.0)  # 5mm safety buffer
        return geometry.intersects(buffer)