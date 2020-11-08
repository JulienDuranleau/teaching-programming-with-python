def setup():
    size(400, 400)
    
def draw():
    noStroke()
    
    # ========= Left side
    
    if mouseX < width / 2:
        fill(255, 100, 100) # red
    else:
        fill(100, 255, 100) # green
        
    rect(0, 0, width / 2, height)
    
    # ========= Right side
    
    if mouseX > width / 2:
        fill(255, 100, 100) # red
    else:
        fill(100, 255, 100) # green
        
    rect(width / 2, 0, width / 2, height)
