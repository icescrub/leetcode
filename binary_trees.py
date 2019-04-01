class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def mergeTrees(self, t1, t2):
	
	if t1 is None:
		return t2
	elif t2 is None:
		return t1
	else:
		t3.value = t1.value + t2.value
		t3.left = mergeTrees(t1.left, t2.left)
		t3.right = mergeTrees(t1.right, t2.right)
		return t3
