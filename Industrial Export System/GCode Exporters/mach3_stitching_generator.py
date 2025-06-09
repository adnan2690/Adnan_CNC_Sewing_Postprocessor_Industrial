class StitchGCodeGenerator:
    def generate(self, design):
        gcode = [
            "% Adnan CNC Stitching Program",
            "G21 G90 G94 ; Metric, absolute, feed/min",
            "M100 ; Start stitching routine"
        ]
        
        for i, path in enumerate(design.paths):
            gcode.append(f"\n; Path {i+1}")
            gcode.append(f"G0 X{path[0][0]} Y{path[0][1]} F8000")
            gcode.append("M106 ; Needle down")
            for point in path[1:]:
                gcode.append(f"G1 X{point[0]} Y{point[1]} F4000")
            gcode.append("M107 ; Needle up")
        
        gcode.append("M103 ; Stop stitching")
        return "\n".join(gcode)