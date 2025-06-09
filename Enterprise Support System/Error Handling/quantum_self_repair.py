class SelfRepair:
    def recover(self, error_code):
        """Industrial self-repair mechanism"""
        if error_code == 1001:
            return "Attempting geometry repair"
        elif error_code == 2001:
            return "Resetting needle position sensor"
        else:
            return "Initiating system reboot"