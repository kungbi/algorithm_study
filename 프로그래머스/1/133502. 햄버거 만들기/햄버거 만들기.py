def solution(ingredients):
    answer = 0
    stack = []
    
    for ingredient in ingredients:
        stack.append(ingredient)
        
        if ingredient != 1:
            continue
        if len(stack) < 4:
            continue
        
        if stack[-4::] != [1,2,3,1]:
            continue
            
        answer += 1
        for _ in range(4):
            stack.pop()
        
            
    return answer