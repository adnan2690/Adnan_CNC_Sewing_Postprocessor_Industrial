import requests

class OTASecurityUpdater:
    UPDATE_URL = "https://updates.adnancnc.com/industrial"
    
    def check_for_updates(self):
        """Industrial over-the-air update check"""
        response = requests.get(f"{self.UPDATE_URL}/version")
        return response.json().get("latest_version")
    
    def apply_update(self, version):
        """Industrial secure update application"""
        print(f"Applying security update: {version}")