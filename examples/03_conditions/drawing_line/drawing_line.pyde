def setup():
    size(400, 400)
    background(25)
    
def draw():
    noStroke()
    
    stroke(255)
    strokeWeight(10)
    
    if mousePressed:
        line(pmouseX, pmouseY, mouseX, mouseY)
