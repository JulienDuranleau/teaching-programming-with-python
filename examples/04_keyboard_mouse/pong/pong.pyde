paddle1_y = 300 - 50
paddle2_y = 300 - 50
ball_x = 400
ball_y = 300
up_arrow = False
down_arrow = False
w_key = False
s_key = False

def setup():
    size(800, 600)
    
def draw():
    global paddle1_y, paddle2_y, ball_x, ball_y
    
    background(25)
    
    if w_key:
        paddle1_y -= 5
    if s_key:
        paddle1_y += 5
        
    if up_arrow:
        paddle2_y -= 5
    if down_arrow:
        paddle2_y += 5
    
    rect(50, paddle1_y, 25, 100)
    rect(width - 50 - 25, paddle2_y, 25, 100)
    circle(ball_x, ball_y, 40)
    
def keyPressed():
    global up_arrow, down_arrow, w_key, s_key
    
    if keyCode == 38:
        up_arrow = True
    elif keyCode == 40:
        down_arrow = True
    elif key == "w":
        w_key = True
    elif key == "s":
        s_key = True
        
def keyReleased():
    global up_arrow, down_arrow, w_key, s_key
    
    if keyCode == 38:
        up_arrow = False
    elif keyCode == 40:
        down_arrow = False
    elif key == "w":
        w_key = False
    elif key == "s":
        s_key = False
