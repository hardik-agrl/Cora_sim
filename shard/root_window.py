from collections import deque


class RootWindow:

    def __init__(self, size: int):
        self.size = size
        self.roots = deque(maxlen=size)

    def add(self, root: str):
        self.roots.append(root)

    def contains(self, root: str) -> bool:
        return root in self.roots

    def latest(self):
        if not self.roots:
            return None
        return self.roots[-1]