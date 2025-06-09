class MaterialProfiler:
    PROFILES = {
        "denim": {"feed": 2500, "tension": 0.8, "needle": "DEN-110"},
        "silk": {"feed": 1800, "tension": 0.3, "needle": "SIL-70"},
        "leather": {"feed": 1200, "tension": 0.9, "needle": "LEA-125"},
        "canvas": {"feed": 3000, "tension": 1.0, "needle": "CAN-100"}
    }
    
    def get_profile(self, material):
        return self.PROFILES.get(material.lower(), {"feed": 2000, "tension": 0.5})