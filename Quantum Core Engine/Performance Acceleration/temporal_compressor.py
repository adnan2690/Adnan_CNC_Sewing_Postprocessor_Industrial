import time

class TemporalCompressor:
    def time_fold(self, ratio):
        """Compress computation time"""
        start = time.time()
        yield
        duration = time.time() - start
        print(f"Time compressed by {ratio}x: {duration:.4f}s -> {duration/ratio:.4f}s")