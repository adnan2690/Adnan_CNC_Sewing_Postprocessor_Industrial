class CommandDispatcher:
    def __init__(self):
        self.commands = {}
    
    def register(self, name, command):
        self.commands[name] = command
    
    def execute(self, name, *args):
        if name in self.commands:
            self.commands[name](*args)