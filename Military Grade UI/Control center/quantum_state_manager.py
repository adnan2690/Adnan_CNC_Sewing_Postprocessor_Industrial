import json

class StateManager:
    def save_state(self, filename, state):
        with open(filename, 'w') as f:
            json.dump(state, f)
    
    def load_state(self, filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}