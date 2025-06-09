class CutterDriver:
    HPGL_COMMANDS = {
        "INIT": "IN;",
        "PEN_UP": "PU;",
        "PEN_DOWN": "PD;",
        "SELECT_PEN": "SP{pen};",
        "MOVE": "PA{x},{y};"
    }
    
    def generate_hpgl(self, paths):
        commands = [self.HPGL_COMMANDS["INIT"], "SP1;"]
        for path in paths:
            commands.append(self.HPGL_COMMANDS["PEN_UP"])
            commands.append(f"PA{path[0][0]},{path[0][1]};")
            commands.append(self.HPGL_COMMANDS["PEN_DOWN"])
            for point in path[1:]:
                commands.append(f"PA{point[0]},{point[1]};")
        commands.append(self.HPGL_COMMANDS["PEN_UP"])
        return "\n".join(commands)