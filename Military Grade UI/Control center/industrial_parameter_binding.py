from PyQt5.QtCore import QObject, pyqtSignal

class ParameterBinder(QObject):
    parameterChanged = pyqtSignal(str, object)
    
    def __init__(self):
        super().__init__()
        self._parameters = {}
        self._widgets = {}
    
    def register_parameter(self, name, default_value):
        """Register industrial parameter"""
        self._parameters[name] = default_value
    
    def bind_widget(self, name, widget):
        """Bind widget to parameter"""
        if name not in self._parameters:
            raise ValueError(f"Unknown parameter: {name}")
            
        self._widgets[name] = widget
        
        # Connect based on widget type
        if hasattr(widget, 'valueChanged'):
            widget.valueChanged.connect(
                lambda value: self._update_parameter(name, value)
            )
        elif hasattr(widget, 'textChanged'):
            widget.textChanged.connect(
                lambda text: self._update_parameter(name, text)
            )
        elif hasattr(widget, 'currentIndexChanged'):
            widget.currentIndexChanged.connect(
                lambda index: self._update_parameter(name, widget.itemData(index))
            )
    
    def _update_parameter(self, name, value):
        """Update parameter value and notify"""
        self._parameters[name] = value
        self.parameterChanged.emit(name, value)
    
    def get_parameter(self, name):
        """Get parameter value"""
        return self._parameters.get(name)
