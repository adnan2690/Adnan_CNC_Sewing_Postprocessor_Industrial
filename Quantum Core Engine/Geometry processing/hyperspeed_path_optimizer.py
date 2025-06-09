import numpy as np
from scipy.spatial import KDTree

class PathOptimizer:
    def optimize(self, paths):
        """Industrial-grade path optimization using KDTree"""
        starts = [path.coords[0] for path in paths]
        kdtree = KDTree(starts)
        
        ordered_paths = []
        remaining = set(range(len(paths)))
        current = 0
        
        while remaining:
            ordered_paths.append(paths[current])
            remaining.remove(current)
            
            if not remaining:
                break
                
            # Find nearest neighbor
            current = min(remaining, 
                         key=lambda i: kdtree.query(paths[i].coords[0])[0])
        
        return ordered_paths