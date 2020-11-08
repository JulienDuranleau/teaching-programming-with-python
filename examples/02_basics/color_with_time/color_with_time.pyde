r = 0

def setup():
    size(400, 400)
    
def draw():
    global r
    
    background(25)
    
    r += 1
    
    # When r is higher than 255, reset to 0
    r = r % 255
    
    fill(r, 100, 200)
    rect(100, 100, 200, 200)
