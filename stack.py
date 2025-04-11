def insert_at_bottom(stack, element):
    if not stack:
        stack.append(element)
        return
    top = stack.pop()
    insert_at_bottom(stack, element)
    stack.append(top)

stack = [1, 2, 3, 4, 5]
insert_at_bottom(stack, 0)
print(stack) 
