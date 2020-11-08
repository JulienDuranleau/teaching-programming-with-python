r = 255
g = 255
b = 255

def setup():
    size(800, 600)
    background(25)
    stroke(255)
    strokeWeight(5)
    
def draw():
    noStroke()
    fill(255, 0, 0)
    rect(0, 0, 40, 40)
    fill(0, 255, 0)
    rect(40, 0, 40, 40)
    fill(0, 0, 255)
    rect(80, 0, 40, 40)
    
    if mousePressed:
        stroke(r, g, b)
        line(pmouseX, pmouseY, mouseX, mouseY)

def mousePressed():
    global r, g, b
    
    if mouseX >= 0 and mouseX <= 40 and mouseY <= 40:
        r = 255
        g = 0
        b = 0 
        
    if mouseX >= 40 and mouseX <= 80 and mouseY <= 40:
        r = 0
        g = 255
        b = 0
        
    if mouseX >= 80 and mouseX <= 120 and mouseY <= 40:
        r = 0
        g = 0
        b = 255
