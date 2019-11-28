from random import Random


class RandomInput:

    def __init__(self):
        self.generator = Random()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def read(self, _):
        return int(self.generator.random() * 10 + 0.5)


def select_input_stream(random=False, filename=None):
    if random:
        return RandomInput()
    return open(filename)
