import socket
import struct
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class QuantumCommSystem:
    HEADER = b'QNTM'
    VERSION = 1
    
    def __init__(self, encryption_key):
        self.encryption_key = encryption_key[:32].ljust(32, b'\0')
        self.iv = b'ADNAN_CNC_IV_16B'
        self.sock = None
    
    def connect(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self._handshake()
    
    def _handshake(self):
        self.sock.sendall(self.HEADER)
        self.sock.sendall(bytes([self.VERSION]))
        response = self.sock.recv(4)
        if response != self.HEADER:
            raise ConnectionError("Quantum handshake failed")
    
    def send(self, data):
        cipher = Cipher(algorithms.AES(self.encryption_key), modes.CBC(self.iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padded = self._pad_data(data)
        encrypted = encryptor.update(padded) + encryptor.finalize()
        
        self.sock.sendall(struct.pack('!I', len(encrypted)))
        self.sock.sendall(encrypted)
    
    def receive(self):
        size_data = self.sock.recv(4)
        if len(size_data) != 4:
            return None
        size = struct.unpack('!I', size_data)[0]
        encrypted = self.sock.recv(size)
        
        cipher = Cipher(algorithms.AES(self.encryption_key), modes.CBC(self.iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted = decryptor.update(encrypted) + decryptor.finalize()
        return self._unpad_data(decrypted)
    
    def _pad_data(self, data):
        pad_size = 16 - (len(data) % 16)
        return data + bytes([pad_size] * pad_size)
    
    def _unpad_data(self, data):
        pad_size = data[-1]
        return data[:-pad_size]
    
    def close(self):
        if self.sock:
            self.sock.close()