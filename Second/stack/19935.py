s = input()
b = input()

arr = []
stack = []

for i in s:
    stack.append(i)
    if len(stack) >= len(b):
        if ''.join(stack[-len(b):]) == b:
            del stack[-len(b):]

print(''.join(stack) if len(stack) != 0 else "FRULA")
