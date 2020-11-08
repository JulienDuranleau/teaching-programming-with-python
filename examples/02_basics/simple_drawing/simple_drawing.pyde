def setup():
    # Set the canvas size
    size(800, 600)
    
    # Paint the background
    background(200, 250, 255)
    
    # Remove the outline of all future shapes
    noStroke()
    
    # Set the color of all future shapes
    fill(240, 124, 74)
    
    # Draw the base of the P
    rect(325, 150, 50, 300)
    
    # Draw the top part of the P
    rect(325, 150, 180, 150, 0, 25, 25, 0)
                           # ^^^^^^^^^^^^
                           # rounded borders
    
    # Draw the inside of the top part of the P
    # with the background color
    fill(200, 250, 255)
    rect(375, 200, 85, 50, 0, 10, 10, 0)
    
    # We're done!
