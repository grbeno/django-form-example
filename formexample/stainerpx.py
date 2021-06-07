import cv2
import numpy as np
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


" MASKING IMAGE "

def mkmask(coords,path):
    
    " Masking image by polygon pixel coordinates " 
    
    img = cv2.imread(f'{path}K_09.24.PNG')
    coords = [ tuple(map(int, i.split(','))) for i in coords ]
    pts = np.array(coords, np.dtype('int'))

    # Crop the bounding rect
    
    rect = cv2.boundingRect(pts)
    x,y,w,h = rect
    croped = img[y:y+h, x:x+w].copy()
    
    # Make mask
    
    pts = pts - pts.min(axis=0)
    mask = np.zeros(croped.shape[:2], np.uint8)
    cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)
    
    # Do bit-op
    
    dst = cv2.bitwise_and(croped, croped, mask=mask)
    
    # Add the white background
    
    bg = np.ones_like(croped, np.uint8)*255
    cv2.bitwise_not(bg,bg, mask=mask)
    res = bg + dst
    masked = f'{path}prepared.png'
    cv2.imwrite(masked,res)

    return masked


" STAINER METHOD "

def stainer(colors,path):
        
    " Stainer folt/színbecslő módszer - Stainer method for colour measuring "
    
    st_data = []
    
    gray = cv2.imread(f'{path}prepared.png')
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    new = cv2.imread(f'{path}prepared.png')
    height, width = new.shape[1], new.shape[0]
    size = height * width

    # CreateStColors 

    st_color_ints = [ (0,254,255) ]
    st_colors = []
    
    decrease = [0,0,127,84,63,50,42,36,31,28,25,23,21,19,18,16,15] # decrease from 254&('from' values) till lowest, with [i]
    blueColors = [
        (240,248,255),(230,230,250),(135,206,250),(0,191,255),(176,195,222),
        (30,144,255),(70,130,180),(95,158,160),(72,61,139),(65,105,225),
        (138,43,226),(0,109,176),(75,0,130),(0,0,255),(0,0,128),(0,0,57)
    ]
    
    for i in range(colors):
        intvs_len = len(st_color_ints)-1
        start = st_color_ints[intvs_len][1]-decrease[colors]
        end = st_color_ints[intvs_len][1]-1
        index = intvs_len
        add_intv = tuple([index,start,end])
        st_color_ints.append(add_intv)
    
    bright_blues = math.ceil(colors/2)
    dark_blues = colors - bright_blues
    st_colors = blueColors[:bright_blues] + blueColors[-dark_blues:]
    st_colors.insert(0,(255,255,255)) # background
    
    st_data = [0 for x in range(len(st_colors))]
    colors = []
    for i in range(width):
        for j in range(height):
            for(index,start,end) in st_color_ints:
                if start <= gray[i,j] and gray[i,j] <= end:
                    new[i,j]= st_colors[index]
                    if st_colors[index] not in colors and index > 0: # no duplicate, no background!
                        colors.append(st_colors[index])
                    count=st_data[index]
                    st_data[index]=count+1
                    break
    
    new = cv2.cvtColor(new, cv2.COLOR_BGR2RGB)
    cv2.imwrite(f'{path}stain.png', new)
    
    new_data = [ i for i in st_data[1:] if i > 0 ] # no 0 values, no background!
    percent = [ float(format(data/(size-st_data[0])*100,'.2f')) for data in new_data ] #if data/(size-st_data[0])*100 > 1 ] # no 0-1 %-s
    
    " PIE diagram " # on Heroku ???

    colors = [ tuple([i/255 for i in rgb]) for rgb in colors ]
    
    plt.clf()
    plt.pie(new_data,colors=colors,labels=percent)
    plt.savefig(f'{path}pie_st.png')
    
    return percent


" CLUSTERING METHOD "