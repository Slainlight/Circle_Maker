from PIL import Image
import math

def circle(size,repetitions):
    img = Image.new('RGBA', (size+1, size+1))

    radius = size/2
    for i in range(repetitions):
        xpos = round(radius*(math.cos(i)+1))
        ypos = round(radius*(math.sin(i)+1))
        img.putpixel((xpos,ypos), (0,0,0))
        
    
    img.save('img.png')
    return img

circle(100,1000)
