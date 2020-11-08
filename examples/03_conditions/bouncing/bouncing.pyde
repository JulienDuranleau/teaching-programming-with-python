x = 400
y = 300
speed_x = 5
speed_y = 5

def setup():
    size(800, 600)
    
def draw():
    global x, y, speed_x, speed_y
    
    background(25)
    
    x = x + speed_x
    y = y + speed_y
    
    # Left
    if x < 0:
        speed_x = 5
    
    # Right
    if x > width:
        speed_x = -5
    
    # Top
    if y < 0:
        speed_y = 5
    
    # Bottom    
    if y > height:
        speed_y = -5
    
    circle(x, y, 40)
