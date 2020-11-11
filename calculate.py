math = "10 + 20 + 30"
math = math.split()

class Tree(object):

  def __init__(self):
    self.children = []
    self.parentTree = 0
    self.node = 0
    self.left = ""
    self.right = ""
    self.operation = ""
    self.result = ""
    self.calculate()

  def calculate(self):
    if self.operation == "+":
      self.result = self.left + self.right
    if self.operation == "-":
      self.result = self.left - self.right
    if self.operation == "*":
      self.result = self.left * self.right
    if self.operation == "/":
      self.result = self.left / self.right   
  def __str__(self):
    return str(self.node)
  def __repr__(self):
    return str(self.node)

class treeBoss():

  def __init__(self):
    self.treeList = []
    self.myTree = Tree()
    indices =[ [i, j] for i, j in enumerate(math)]
    self.nums = [ i for i in indices if i[1].isnumeric() == True]
    self.ops = [ i for i in indices if i[1].isnumeric() == False]
    self.debugInfo()

  def opPrecedence(self, ops):
    ''' Will build this class later'''
    pass

  def createBranches(self, nums):
    myTree = self.myTree
    numnodes = len(self.ops)
    for i in nums:
      if numnodes >= 2:
        self.mapTrees()
        myTree.left.right = int(i[1])
        myTree.left.operation = self.ops[1][1]
        numnodes=numnodes-1
      elif myTree.left.left == "":
        self.myTree.left.left = int(i[1])
      elif myTree.left.right == "":
        myTree.left.right = int(i[1])

  def mapTrees(self):
    myTree = self.myTree
    treeList = self.treeList
    node = self.myTree.node
    myTree.left = Tree()
    myTree.right = Tree()
    myTree.left.node = node +1
    myTree.right.node = node +2
    node = node+1
    treeList.append(myTree)
    treeList.append(myTree.left)
    treeList.append(myTree.right)
    myTree.children.append(myTree.left)
    myTree.children.append(myTree.right)

  def debugInfo(self):
    myTree = self.myTree
    self.createBranches(self.nums)
    print("------------------")
    print("Root Tree Node:", myTree.right.node)
    print("Parent Tree:", myTree.left.parentTree)
    print("Tree List:", self.treeList)
    print("Children", myTree.children)
    print("MyTree.right:", self.myTree.right)
    print("MyTree.left:", self.myTree.left)
    print("MyTree.left.left:", myTree.left.left)
    print("MyTree.left.operation:", myTree.left.operation)
    print("MyTree.left.right:", myTree.left.right)
    myTree.left.calculate()
    print("Answer for left tree:", myTree.left.result)

treeBoss()
