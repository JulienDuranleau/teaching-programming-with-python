# Position
x = 400
y = 300

# Velocity
speed_x = 0
speed_y = 0

# Key held down
a_is_down = False
d_is_down = False


def setup():
    size(800, 600)
    
def draw():
    global x, y, speed_x, speed_y
    background(25)
    
    fill(255)
    noStroke()
    
    # Air friction to reduce horizontal speed
    if speed_x > 0.5:
        speed_x -= 0.5
    elif speed_x < -0.5:
        speed_x += 0.5
    else:
        speed_x = 0
        
    # Horizontal movement
    if a_is_down:
        speed_x -= 1
    if d_is_down:
        speed_x += 1
        
    # Gravity
    speed_y += 0.5
    
    # Actually move the position according to the velocity
    x += speed_x
    y += speed_y
    
    # If we're going through the ground, reposition on the ground level
    if y > height - 50:
        y = height - 50
        speed_y = 0
    
    # Draw
    rect(x, y, 50, 50)

def keyPressed():
    global speed_y, a_is_down, d_is_down
    
    if key == "a":
        a_is_down = True
    if key == "d":
        d_is_down = True
    if key == " ":
        speed_y = -15 # Jump!
        
def keyReleased():
    global a_is_down, d_is_down
    
    if key == "a":
        a_is_down = False
    if key == "d":
        d_is_down = False
