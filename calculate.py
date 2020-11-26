import copy
import time
class Tree(object):

  def __init__(self):
    self.node = 0
    self.left = None
    self.right = None
    self.data = ""
    self.parent = None
  def __str__(self):
    return str(self.node)
  def __repr__(self):
    return str(self.node)

children = []

def splitEquation(math):
  nums = []
  ops = []
  answer = ""
  for i in math:
    if i == "=":
      answer = math[-1]
      break
    if i.isdigit() == True:
      nums.append(i)
    if i.isdigit() == False:
      ops.append(i)
  return nums, ops, answer

def inputEquation():
  math = "10 * 10 = 100"
  math = math.split()
  answer = "blank"
  nums, ops, answer = splitEquation(math)
  splitEquation(math)
  numOfNums = len(nums)
  if numOfNums < 2:
    print("This is not the proper form of a question. Please try again.")
    inputEquation()
  elif answer == "blank":
    print("This is not the proper form of a question. Please try again.")
    inputEquation()
  else:
    eq = Equation()
    eq.nums = nums
    eq.ops = ops
    eq.answer = answer
    eq.math = math
  return eq

class Equation(object):
  ''' Parses input given to the calculator'''
  def __init__(self):
    self.math = ""
    self.answer = ""
    self.nums = []
    self.ops = []

class calculate(object):
  ''' This is sloppy as fuck and needs to be fixed '''
  def __init__(self, ops, nums):
    self.answer = 0
    self.ops = ops
    self.nums = nums
    self.operation()
  def operation(self):
    ''' call a function depending upon operator '''
    opDict = {
        "+": self.add,
        "-": self.subtract,
        "/": self.divide,
        "*": self.multiply}
    # Checks operator, then passes self.nums to function.
    self.choice = opDict[self.ops[0]](self.nums)
  def add(self, *args):
    '''For whatever reason self.choice turns changes nums into a tuple. So we need to unpack it.'''
    args = args[0]
    for i in args:
      i = int(i)
      self.answer += i
  def subtract(self, *args):
    args = args[0]
    for i in args:
      i = int(i)
      self.answer -= i
  def multiply(self, *args):
    args = args[0]
    result = int(args[0])
    args.pop(0)
    for i in args:
      i = int(i)
      result *= i
    self.answer = result
  def divide(self, *args):
    args = args[0]
    result = int(args[0])
    args.pop(0)
    for i in args:
      i = int(i)
      result /= i
    self.answer = result
  def __str__(self):
    return str(self.answer)
  def __repr__(self):
    return str(self.answer)

def createTrees(nums, ops):
  nums = copy.deepcopy(nums)
  ops = copy.deepcopy(ops)
  for i in nums:
    tree = Tree()
    tree.data = ops[0]
    tree.left = Tree()
    tree.right = Tree()
    trees = [tree.right, tree.left]
    count = 1
    for i in trees:
      i.parent = tree.node
      i.node = tree.node + count
      count = count + 1
      i.data = nums[0]
      nums.pop(0)
    ops.pop(0)
    children.insert(0,tree)
    children.extend(trees)
  else:
    pass # This needs to be expanded to solve for more complex equations

class refreshTrees(object):
  def __init__(self):
    self.updateTrees()
  def isOperator(self, tree):
    # Add code which check if operator is valid
    if tree.data.isdigit() == True:
      return False
    else:
      return True

  def updateTrees(self):
    for i in children:
      if self.isOperator(i) == True:
        nums = [i.right.data, i.left.data]
        operator = i.data
        i.data = calculate(operator, nums)
        children.remove(i.right)
        children.remove(i.left)
        i.right = None
        i.left = None

def checkAnswer(parseTree):
  ''' Lots of type coercsion in this function, probably a much better way to do this'''
  correctAnswer = children[0].data.answer
  userAnswer = int(parseTree.answer)
  if userAnswer == correctAnswer:
    print("You entered", userAnswer, "which is the correct answer. Congratulations!")
    return True
  else:
    print("Sorry, that's the wrong answer. Try again.")
    return False


def answerChecker():
  equation = inputEquation()
  nums = equation.nums
  ops = equation.ops
  createTrees(nums, ops)
  refreshTrees()
  checkAnswer(equation)


class memoryBank():
  ''' This is the budget version. The bigger version would involve a database'''
  def __init__(self):
    self.inputBank = ["10 * 10", "10 * 4"]
    self.questionBank = []
    self.answerBank = []
    self.count = 0
  def createQuestions(self):
    # print("Enter as many questions as you would like, or press X to exit")
    # for i in range(10):
    #   x = input("Enter a new question: ")
    #   if x == "x":
    #     break
    #   inputBank.append(x)
    for i in self.inputBank:
      i = i.split()
      self.questionBank.append(splitEquation(i))
    for i in self.questionBank:
      nums = i[0]
      ops = i[1][0]
      self.answerBank.append(calculate(ops, nums))
  def answerQuestions(self):
    for i in self.inputBank:
      print("-----------------------\n")
      print(i, "=", end = " ")
      start = time.time()
      answer = int(input())
      end = time.time()
      correctAnswer = self.answerBank[self.count].answer
      if answer == correctAnswer:
        print("\n\nYes, the answer was", correctAnswer)
        print("It took","%.2f" % (end-start), "seconds to answer the question\n\n")
        input("Press any key to continue.")
        print("\n")
      else:
        print("No, sorry the answer was", correctAnswer)
      self.count = self.count + 1

game = memoryBank()
game.createQuestions()
game.answerQuestions()
