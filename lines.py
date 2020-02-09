import random
fout = open("pic.ppm","w")
size = 500
fout.write("P3\n"+str(size)+" "+str(size)+"\n255\n")


pixels = []
for i in range(500):
    pixels.append([])
    for j in range(500):
        pixels[i].append([255,255,255])

def line(x1,y1,x2,y2,r,g,b):
    if(x1==x2):
        for i in range(min(y1,y2),max(y1,y2)+1):
            pixels[x1][i]=[r,g,b]
        return
    if(y1==y2):
        for i in range(min(x1,x2),max(x1,x2)+1):
            pixels[i][y1]=[r,g,b]
        return
    m = (y1-y2)/(x1-x2)
    #print(m)
    if(abs(m)<1):
        if(x1>x2):
            line(x2,y2,x1,y1,r,g,b)
            return
        extra = 0
        shift = 0

        for i in range(x1,x2+1):
            pixels[i][y1+shift]=[r,g,b]
            extra += m
            shift=round(extra)
    if(abs(m)>1):
        m = 1/m
        if(y1>y2):
            line(x2,y2,x1,y1,r,g,b)
            return
        extra = 0
        shift = 0

        for i in range(y1,y2+1):
            pixels[x1+shift][i]=[r,g,b]
            extra += m
            shift=round(extra)

for i in range(6):
    line(random.randint(0,size-1),random.randint(0,size-1),random.randint(0,size-1),random.randint(0,size-1),random.randint(0,255),random.randint(0,255),random.randint(0,255))
for i in range(500):
    for j in range(500):
        fout.write(str(pixels[i][j][0])+" "+str(pixels[i][j][1])+" "+str(pixels[i][j][2])+" ")

    fout.write("\n")