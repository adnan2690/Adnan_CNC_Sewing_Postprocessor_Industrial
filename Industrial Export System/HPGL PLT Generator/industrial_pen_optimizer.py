class PenOptimizer:
    def optimize_moves(self, paths):
        """Optimize pen movements for industrial cutting"""
        # Sort paths to minimize travel
        return sorted(paths, key=lambda path: path[0][0])