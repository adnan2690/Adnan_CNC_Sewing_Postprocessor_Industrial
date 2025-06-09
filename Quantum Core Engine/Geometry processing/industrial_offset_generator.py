import numpy as np
from shapely.geometry import LineString
from numba import jit

class IndustrialOffsetGenerator:
    PRECISION = 0.001  # 1μm precision
    MITER_LIMIT = 3.0
    
    @jit(nopython=True, parallel=True)
    def generate_offsets(self, geometry, seam_allowance, foot_extension):
        # Input validation
        assert 1.0 <= seam_allowance <= 20.0, "Invalid seam allowance"
        assert 0.5 <= foot_extension <= 15.0, "Invalid foot extension"
        
        # Generate seam allowance
        seam = geometry.buffer(
            seam_allowance,
            join_style=2,
            mitre_limit=self.MITER_LIMIT,
            resolution=32
        ).simplify(self.PRECISION)
        
        # Generate slot path
        slot = geometry.buffer(
            -foot_extension / 2,
            cap_style=2,
            join_style=2
        )
        
        # Apply industrial extensions
        return self.apply_extensions(slot, foot_extension * 1.5), seam
    
    @jit(nopython=True)
    def apply_extensions(self, geometry, extension):
        if extension <= 0: 
            return geometry
            
        coords = np.array(geometry.coords)
        start_dir = coords[1] - coords[0]
        end_dir = coords[-1] - coords[-2]
        
        start_ext = coords[0] - start_dir * extension / np.linalg.norm(start_dir)
        end_ext = coords[-1] + end_dir * extension / np.linalg.norm(end_dir)
        
        extended = np.vstack(([start_ext], coords, [end_ext]))
        return LineString(extended)