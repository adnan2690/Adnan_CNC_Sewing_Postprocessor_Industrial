class ParameterBinder:
    def bind(self, ui_element, parameter):
        """Industrial-grade UI binding"""
        ui_element.valueChanged.connect(
            lambda value: setattr(parameter, ui_element.propertyName(), value)
        )