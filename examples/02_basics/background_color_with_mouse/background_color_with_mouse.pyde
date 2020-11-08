def setup():
    size(400, 400)
    
def draw():
    r = mouseX
    g = mouseY
    b = 255 - mouseX
    
    background(r, g, b)
