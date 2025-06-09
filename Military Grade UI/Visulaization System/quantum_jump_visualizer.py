class JumpVisualizer:
    def visualize(self, jumps):
        """Visualize jump moves between paths"""
        return [
            {
                "start": jump[0],
                "end": jump[1],
                "style": "dashed",
                "color": (0.8, 0.1, 0.1)
            }
            for jump in jumps
        ]