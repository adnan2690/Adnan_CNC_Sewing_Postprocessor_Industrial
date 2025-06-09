class CuttingGCodeGenerator:
    def generate(self, template):
        gcode = [
            "% Adnan CNC Template Cutting",
            "G21 G90 G94 ; Metric, absolute, feed/min",
            "M110 ; Activate cutter"
        ]
        
        for path in template.cut_paths:
            gcode.append(f"\n; Cutting path")
            gcode.append(f"G0 X{path[0][0]} Y{path[0][1]} F10000")
            gcode.append("M111 ; Cutter down")
            for point in path[1:]:
                gcode.append(f"G1 X{point[0]} Y{point[1]} F5000")
            gcode.append("M112 ; Cutter up")
        
        gcode.append("M113 ; Stop cutter")
        return "\n".join(gcode)