import zlib
import lzma

class CompressionEngine:
    def compress(self, data, method='quantum'):
        if method == 'quantum':
            return lzma.compress(data, preset=9)
        elif method == 'industrial':
            return zlib.compress(data, level=9)
        else:
            return data
    
    def decompress(self, data, method='quantum'):
        if method == 'quantum':
            return lzma.decompress(data)
        elif method == 'industrial':
            return zlib.decompress(data)
        else:
            return data