def setup():
    size(400, 400)
    
def draw():
    background(25)
    
    # If mouse is over the rectangle
    if mouseX >= 100 and mouseX <= 300 and mouseY >= 100 and mouseY <= 300:
        # Change the color if it's pressed or not
        if mousePressed:
            fill(255, 100, 200)
        else:
            fill(255, 150, 250)
    else:
        fill(255)
    
    rect(100, 100, 200, 200)
