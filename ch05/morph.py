class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return f"{self.surface} {self.base} {self.pos} {self.pos1}"

    def __repr__(self):
        return self.__str__()
