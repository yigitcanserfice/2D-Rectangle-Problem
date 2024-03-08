from Node import Node, Rect
class Packer():
    def __init__(self, min_w:int, min_h:int) -> None:
        self.root = Node((0,0), (min_w, min_h))
        self.bounds = (min_w, min_h)
        self.rects = []
    def fit(self, rects:list[Rect]) -> list[Rect]:
        """Dikdörtgenleri alana yerleştir. """
        self.rects = rects
        while True:
            self.rects = self._fit(rects)
            return self.rects
    def find_node(self, node:Node, w:int, h:int) -> Node:
        if node.used:
            return self.find_node(node.right, w, h) or self.find_node(node.down, w, h)
        elif w <= node.w and h <= node.h:
            return node
        else:
            return None
    def split_node(self, node:Node, w:int, h:int) -> Node:
        node.used = True
        node.down = Node(origin=(node.x, node.y + h), size=(node.w, node.h - h))
        node.right = Node(origin=(node.x + w, node.y), size=(node.w - w, h))
        return node
class MakePackage(Packer):
    def _fit(self, rects:list[Rect]) -> list[Rect]:
        for rect in rects:
            node = self.find_node(self.root, rect.w, rect.h)
            if node:
                rect.fit = self.split_node(node, rect.w, rect.h)
            if rect.fit:
                rect.inbounds = False if self.root.x+self.bounds[0] < rect.fit.x or self.root.y+self.bounds[1] < rect.fit.y else True
            else:
                rect.inbounds = False
        return rects

