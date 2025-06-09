from treeFactory import TreeFactory

# Simulate rendering 5 trees of only 2 types
positions = [(10, 20), (15, 25), (20, 30), (10, 22), (17, 26)]
types = ["oak", "pine", "oak", "oak", "pine"]

for t, p in zip(types, positions):
    tree = TreeFactory.get_tree(t)
    tree.render(*p)
    
    
print(f"Total distinct tree types created: {TreeFactory.get_count()}")