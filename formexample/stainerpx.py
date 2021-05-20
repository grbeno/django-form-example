import cv2
import numpy as np


def mask(coords):
    " ... " 
    path = "c:\\Python\\Python38-32\\Django\\form_example\\static\\images\\"
    img = cv2.imread(f'{path}K_09.24.PNG')  # images\\K_09.24.PNG
    
    coords = [ tuple(map(int, i.split(','))) for i in coords['coords'] ]
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
    masked = f'{path}dst.png' # images\\dst2.png 
    cv2.imwrite(masked,res)


" TESZT "

#coords = { 'coords': ['132,34', '147,87', '206,86', '217,139', '171,149', '187,210', '116,232', '182,575', '436,497', '281,79'] }
#folder = "c:\\Python\\Python38-32\\Django\\form_example\\static\\images"
#masked_image = mask(coords,folder)