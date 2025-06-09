class PrecisionCalculator:
    TOLERANCE = 0.001  # 1μm
    
    def calculate_deviation(self, actual, target):
        """Calculate aerospace-grade precision deviation"""
        return abs(actual - target) < self.TOLERANCE