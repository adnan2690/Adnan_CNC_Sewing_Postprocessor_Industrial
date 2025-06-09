class PathPreview:
    def generate_preview(self, paths):
        """Generate industrial preview data"""
        preview_data = []
        for path in paths:
            preview_data.append({
                "coords": path.coords,
                "color": (0.1, 0.3, 0.8),
                "width": 1.5
            })
        return preview_data