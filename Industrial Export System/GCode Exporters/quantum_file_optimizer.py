class FileOptimizer:
    def optimize(self, gcode):
        """Industrial file size optimization"""
        # Remove comments and empty lines
        lines = [line for line in gcode.split('\n') 
                if line.strip() and not line.strip().startswith(';')]
        return '\n'.join(lines)