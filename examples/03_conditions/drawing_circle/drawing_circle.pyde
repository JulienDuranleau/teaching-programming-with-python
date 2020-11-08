def setup():
    size(400, 400)
    background(25)
    
def draw():
    noStroke()
    
    fill(255)
    
    if mousePressed:
        circle(mouseX, mouseY, 40)
