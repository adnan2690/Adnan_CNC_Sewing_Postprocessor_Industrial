class StitchFactory:
    def create_stitch(self, mode, path, params):
        if mode == "straight":
            return StraightStitch(path, params)
        elif mode == "zigzag":
            return ZigzagStitch(path, params)
        elif mode == "triple":
            return TripleStitch(path, params)
        elif mode == "lock":
            return LockStitch(path, params)
        else:
            raise ValueError(f"Unsupported stitch mode: {mode}")

class StraightStitch:
    def __init__(self, path, params):
        self.path = path
        self.density = params['density']
    
    def generate_points(self):
        # Generate points based on density
        return [point for point in self.path.coords]

class ZigzagStitch(StraightStitch):
    def generate_points(self):
        # Generate zigzag pattern
        points = []
        for i, point in enumerate(self.path.coords):
            if i % 2 == 0:
                points.append((point[0], point[1] + self.width/2))
            else:
                points.append((point[0], point[1] - self.width/2))
        return points