class TackleGenerator:
    def generate(self, position, length=3.0, count=4):
        """Generate industrial tackle stitching"""
        points = []
        for i in range(count):
            offset = length if i % 2 == 0 else -length
            points.append((position[0], position[1] + offset))
        return points