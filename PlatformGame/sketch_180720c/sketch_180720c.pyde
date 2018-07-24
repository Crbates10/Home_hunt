def setup():
    size (800, 800)
    fill (0, 0, 255)
    global img 
    x = 0
    y= 0
    #draw until I get to the right edge
    while y <= 800:
        while x <= 800:
            if x % 3 == 0: 
                fill (0, 255, 0)
            elif x >=20:
                fill (0,0,255)
            rect (x, y, 20, 20)
            x = x + 20
        x= 0
        y= y+ 20
        img = loadImage("received_1984976631729081.jpg")
    image(img,0,190,190,160)
    y =0 
    while(y<700):
      image(img,0,y,190,160)
      y=y + 190
      x=20
      image(img,200,x,190,160)
      x =60
      
def draw():
    global  img 
    image (img, random(255),random(255),190,160)
    #image (img, random(255),random(255),290,260)
