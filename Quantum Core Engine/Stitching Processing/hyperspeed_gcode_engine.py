class IndustrialGCodeGenerator:
    def generate(self, design, machine_profile="industrial"):
        profiles = {
            "industrial": {"rapid": 10000, "stitch": 5000, "tackle": 2500},
            "precision": {"rapid": 6000, "stitch": 3000, "tackle": 1500}
        }
        config = profiles[machine_profile]
        
        gcode = [
            "% Adnan CNC Sewing Program",
            "G90 G94 G21 ; Absolute, feed/min, metric",
            f"M100 ; Initialize stitching"
        ]
        
        for i, path in enumerate(design.paths):
            gcode.append(f"\n; Path {i+1}")
            gcode.extend(self._generate_path_commands(path, config))
        
        gcode.append("M103 ; Stop stitching")
        return "\n".join(gcode)
    
    def _generate_path_commands(self, path, config):
        commands = []
        start = path.coords[0]
        
        # Rapid move to start
        commands.append(f"G0 X{start[0]:.3f} Y{start[1]:.3f} F{config['rapid']}")
        
        # Tackle stitching
        if path.properties.get('tackle', True):
            commands.extend(self._generate_tackle(start, config))
        
        # Needle down + main path
        commands.append("M106 ; Needle down")
        for point in path.coords[1:]:
            commands.append(f"G1 X{point[0]:.3f} Y{point[1]:.3f} F{config['stitch']}")
        commands.append("M107 ; Needle up")
        
        return commands
    
    def _generate_tackle(self, position, config):
        x, y = position
        return [
            f"G1 X{x:.3f} Y{y+3:.3f} F{config['tackle']}",
            f"G1 X{x:.3f} Y{y-3:.3f} F{config['tackle']}",
            f"G1 X{x:.3f} Y{y+3:.3f} F{config['tackle']}",
            f"G1 X{x:.3f} Y{y:.3f} F{config['tackle']}"
        ]