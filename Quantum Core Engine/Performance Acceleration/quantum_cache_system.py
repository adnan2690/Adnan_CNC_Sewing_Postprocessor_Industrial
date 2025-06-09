import hashlib
import json

class QuantumCache:
    def __init__(self):
        self.cache = {}
    
    def get(self, key):
        return self.cache.get(self._hash(key))
    
    def set(self, key, value):
        self.cache[self._hash(key)] = value
    
    def _hash(self, data):
        return hashlib.sha256(json.dumps(data).encode()).hexdigest()