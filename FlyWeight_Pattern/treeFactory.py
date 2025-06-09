from tree import Tree

class TreeFactory:
    _trees : dict[str, Tree] = {}
    
    @classmethod
    def get_tree(cls, tree: int) -> Tree:
        if not tree in cls._trees:
            cls._trees[tree] = Tree(tree)
        return cls._trees[tree]

    @classmethod
    def get_count(cls) -> int:
        return len(cls._trees)