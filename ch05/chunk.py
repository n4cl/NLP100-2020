from morph import Morph

class Chunk:
    def __init__(self) -> None:
        self.morphs = []
        self.dst = -1
        self.srcs = []

    def __str__(self) -> str:
        return f"dst[{self.dst}] srcs{self.srcs} morphs{self.morphs}"

    def __repr__(self) -> str:
        return self.__str__()

    def add_morph(self, morph: Morph) -> None:
        self.morphs.append(morph)

    def set_dst(self, dst: int) -> None:
        self.dst = dst

    def add_src(self, src: int) -> None:
        self.srcs.append(src)
