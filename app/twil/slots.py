class Example:
    __slots__ = ['var1', 'var2']

    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2


class RegExample:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2


if __name__ == '__main__':
    example = Example('lenny', 'boyatzis') # has no __dict__
    # dir(example) -> has no __dict__
    # dir(example) -> has no __weakref__

    regexample = RegExample('joey', 'tribiani')
    # dir(regexample) -> has __dict__
    # regexample.__dict__ = {'var1': 'joey', 'var2': 'tribiani'}
