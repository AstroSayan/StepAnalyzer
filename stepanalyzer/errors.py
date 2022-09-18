class SysError(Exception):
    pass


class PropertyError(Exception):
    pass


class StabilityError(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


class InputError(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'
