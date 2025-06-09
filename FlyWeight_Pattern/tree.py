class Tree:
    def __init__(self, tree_type: str):
        self.tree_type = tree_type  # Intrinsic attribute

    def render(self, x: int, y: int):
        print(f"Rendering {self.tree_type} at ({x}, {y})")