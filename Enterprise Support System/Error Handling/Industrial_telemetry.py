import time
import json

class TelemetrySystem:
    def log(self, event, details):
        """Industrial telemetry logging"""
        entry = {
            "timestamp": time.time(),
            "event": event,
            "details": details
        }
        with open("telemetry.log", "a") as f:
            f.write(json.dumps(entry) + "\n")
