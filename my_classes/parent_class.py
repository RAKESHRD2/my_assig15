class ParentClass:
    def __init__(self, value):
        self.value = value

    def do_something(self):
        raise NotImplementedError("Subclasses must implement this method")
