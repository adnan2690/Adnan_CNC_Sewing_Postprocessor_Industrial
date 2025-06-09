class ErrorCodes:
    CODES = {
        1001: "Geometry self-intersection detected",
        1002: "Stitch density too high for path curvature",
        1003: "Unsupported file format structure",
        2001: "Needle position sensor timeout",
        2002: "Clamp engagement failure",
        3001: "Material feed jam detected",
        4001: "Emergency stop activated",
        9999: "Critical system failure"
    }
    
    def get_message(self, code):
        return self.CODES.get(code, "Unknown error")