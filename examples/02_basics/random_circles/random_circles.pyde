def setup():
    size(800, 600)
    background(25)
    frameRate(10) # Change the drawing speed
    
def draw():
    # Random position
    x = random(0, width)
    y = random(0, height)
    
    # Random color
    r = random(150, 255)
    g = 150
    b = random(150, 255)
    transparency = 200
    
    # Set drawing styles
    strokeWeight(2)
    stroke(0)
    fill(r, g, b, transparency)
    
    # Draw
    circle(x, y, 40)
