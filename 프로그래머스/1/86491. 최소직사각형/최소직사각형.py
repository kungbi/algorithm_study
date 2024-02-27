def solution(sizes):
    width_max = 0
    height_max = 0
    
    for size in sizes:
        if size[0] > size[1]:
            size[0], size[1] = size[1], size[0]
        width_max = max(width_max, size[0])
        height_max = max(height_max, size[1])
    return width_max * height_max
        