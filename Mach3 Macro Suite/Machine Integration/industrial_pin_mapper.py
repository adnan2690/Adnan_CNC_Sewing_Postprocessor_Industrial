class PinMapper:
    PIN_MAPPING = {
        "clamp": 1,
        "needle_sensor": 2,
        "cutter": 3,
        "emergency_stop": 4
    }
    
    def get_pin(self, function):
        return self.PIN_MAPPING.get(function, None)