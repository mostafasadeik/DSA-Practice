# Graphs (DFS) - Depth First Search
# This code implements a depth-first search (DFS) algorithm for traversing a graph.

# تعريف الكلاس
class Node: 
    def __init__(self,name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self  # علشان نقدر نستخدم السلسلة (method chaining)

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


# مثال عملي (test case)

# نعمل الجذر (root)
root = Node("A")

# نضيف الأبناء
root.addChild("B").addChild("C").addChild("D")  # A -> B, C, D

# نضيف أبناء لـ D
root.children[2].addChild("E").addChild("F")    # D -> E, F

# نبدأ بـ DFS
result = root.depthFirstSearch([])

# نطبع النتيجة
print(result)  # المفروض تطلع: ['A', 'B', 'C', 'D', 'E', 'F']

