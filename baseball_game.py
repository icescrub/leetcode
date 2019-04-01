from collections import deque

stack = []
q = deque(ops)

while q:
	value = q.popleft()
	if value == 'C':
		stack.pop()
	elif value == 'D':
		stack.append(2*stack[-1])
	elif value == '+':
		stack.append(stack[-1] + stack[-2])
	else:
		stack.append(int(value))

return sum(stack)
