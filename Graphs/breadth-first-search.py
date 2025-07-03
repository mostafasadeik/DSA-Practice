# Graphs (DFS) - Depth First Search
# This code implements a depth-first search (DFS) algorithm for traversing a graph.

# تعريف الكلاس
class Node: 
    def __init__(self,name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    def breadthFirstSearch(self, array):
        queue = [self]
        while queue:
            current = queue.pop(0)
            array.append(current.name)
            queue.extend(current.children)
        return array
    
# مثال عملي (test case)
# نعمل الجذر (root)
root = Node("A")
# نضيف الأبناء
root.addChild("B").addChild("C").addChild("D")  # A -> B, C, D
# نضيف أبناء لـ D
root.children[2].addChild("E").addChild("F")    # D -> E, F
# نبدأ بـ BFS
result = root.breadthFirstSearch([])
# نطبع النتيجة
print(result)  # المفروض تطلع: ['A', 'B', 'C', 'D', 'E', 'F']
        




