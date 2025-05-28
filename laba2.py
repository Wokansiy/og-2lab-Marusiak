import matplotlib.pyplot as plt

# генератор напрямків
GENERATOR = [
    (1, 0), (0, 1), (0, 1), (1, 0), (1, 0),
    (0, -1), (-1, 0), (0, -1), (1, 0), (1, 0),
    (0, -1), (-1, 0), (0, -1), (1, 0), (1, 0),
    (0, 1), (0, 1), (1, 0)
]

def rotate_vector(vec):
   
    dx, dy = vec
    return (dx, dy)

def apply_generator(start, direction, depth):
  
    if depth == 0:
     
        end = (start[0] + direction[0], start[1] + direction[1])
        return [start, end]

    
    path = [start]
    current = start
    for move in GENERATOR:
        
        subpath = apply_generator(current, move, depth - 1)
        path.extend(subpath[1:])  # щоб не було дублювання
        current = subpath[-1]
    return path

# поч.точка і напрямок
start_point = (0, 0)
initial_direction = (1, 0)

# глибина
depth = 2

# генеарція
points = apply_generator(start_point, initial_direction, depth)

# побудова
x, y = zip(*points)
plt.figure(figsize=(12, 6))
plt.plot(x, y, 'ko-', lw=2, markersize=3)
plt.axis('equal')
plt.grid(True)
plt.title(f"2 лаба (рекурсія depth = {depth})")
plt.show()
