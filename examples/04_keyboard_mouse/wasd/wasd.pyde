# Position
x = 200
y = 200

# Movement speed
speed = 5

# Keys that are held down
w_is_down = False
a_is_down = False
s_is_down = False
d_is_down = False

def setup():
    size(400, 400)
    
def draw():
    global x, y
    
    background(25)
    
    if w_is_down:
        y -= speed
    
    if a_is_down:
        x -= speed
        
    if s_is_down:
        y += speed
        
    if d_is_down:
        x += speed
    
    rect(x, y, 50, 50)
    
def keyPressed():
    global w_is_down, a_is_down, s_is_down, d_is_down
    
    if key == "w":
        w_is_down = True
    if key == "a":
        a_is_down = True
    if key == "s":
        s_is_down = True
    if key == "d":
        d_is_down = True
        
def keyReleased():
    global w_is_down, a_is_down, s_is_down, d_is_down
    
    if key == "w":
        w_is_down = False
    if key == "a":
        a_is_down = False
    if key == "s":
        s_is_down = False
    if key == "d":
        d_is_down = False
