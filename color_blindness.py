#!/usr/bin/env python
# coding: utf-8

# In[157]:


pip install Pillow 


# In[158]:


from PIL import Image


# In[159]:


#img = Image.open('trial1.jpg')
#img = Image.open('trial2.webp')
image_path = input("Enter the path of the image:")
img = Image.open(image_path)
x,y = img.size
print(f"({x},{y})")
print(img.mode)
display(img)


# In[160]:


pixel =  list(img.getdata())

print(pixel[:10])
print(f'The total number of pixels are : {len(pixel)}')


# In[161]:


#to get unique pixels only

unique_pixels = set(pixel)
print(f'The unique number of pixels are : {len(unique_pixels)}')
print(unique_pixels )


# In[162]:


# 1 St 

from collections import Counter
rep = Counter(pixel)
most_rep = max(rep, key=rep.get )
print(most_rep)
repeated = rep[most_rep]
print(f'repeated : {repeated} times')


# In[163]:


#2ND 
unipix = list(unique_pixels)
rounded = set()
for r,g,b in unipix:
    rounded_r = round(r, -1)
    rounded_g = round(g, -1)
    rounded_b = round(b, -1)
    round_tup = (rounded_r,rounded_g,rounded_b)
    rounded.add(round_tup)
    
print(f'Total number of unique colors after rounding are:  {len(rounded)}')


# In[164]:


#3rd 

percentage = repeated/len(pixel)*100
print('========= COLOR REPORT ========== ')
print(f'Total Pixels         : {len(pixel)}')
print(f'Unique Color         : {len(rounded)}')
print(f'Most Dominant Color  : {most_rep}')
print(f'Dominance percentage : {percentage:.2f}%')
display(img)


# In[165]:


from PIL import ImageDraw, ImageFont


# In[166]:


#img = Image.open("trial_3.jpeg")
#draw = ImageDraw.Draw(img)
#draw.text((400, 280), "========= COLOR REPORT ========== ", fill=(255, 255, 255))
#draw.text((410, 290), f"Total Pixels         : {len(pixel)} ", fill=(255, 255, 255))
#draw.text((410, 300), f"Unique Color         : {len(rounded)} ", fill=(255, 255, 255))
#draw.text((410, 310), f"Most Dominant Color  : {most_rep} ", fill=(255, 255, 255))
#draw.text((410, 320), f"Dominance percentage : {percentage:.2f}% ", fill=(255, 255, 255))
#display(img)


# In[167]:


#For RED -GREEN colorblindness


# In[170]:


New_pixels = []

def GREEN(): # this is for lack of green cones
    for r, g, b in pixel:
        new_r = int(0.625*r + 0.375*g + 0*b)
        new_g = int(0.700*r + 0.300*g + 0*b)
        new_b = int(0.000*r + 0.300*g + 0.700*b)
        new_pixel = (new_r , new_g, new_b)
        New_pixels.append(new_pixel)
    img.putdata(New_pixels) 
    display(img) 
    
def RED():
    for r, g, b in pixel:
        new_r = int(0.567*r + 0.433*g + 0*b)
        new_g = int(0.558*r + 0.442*g + 0*b)
        new_b = int(0.000*r + 0.242*g + 0.758*b)
        new_pixel = (new_r , new_g, new_b)
        New_pixels.append(new_pixel)
    img.putdata(New_pixels) 
    display(img) 

def BLUE():
    for r, g, b in pixel:
        new_r = int(0.950*r + 0.050*g + 0*b)
        new_g = int(0.433*r + 0.567*g + 0*b)
        new_b = int(0.000*r + 0.475*g + 0.525*b)
        new_pixel = (new_r , new_g, new_b)
        New_pixels.append(new_pixel)
    img.putdata(New_pixels) 
    display(img) 
def GREY():
    img = Image.open(image_path)  # fresh copy!
    pixel = list(img.getdata())           # fresh pixels!
    New_pixels = []
    for r, g, b in pixel:
        grey = int(0.299*r + 0.587*g + 0.114*b)
        new_pixel = (grey, grey, grey)
        New_pixels.append(new_pixel)
    img.putdata(New_pixels)
    display(img)
    
print(""" Choose which Colorblindness to Check :
 1. Deuteranopia  ( Green cone absence )
 2. Protanopia    (Red-cone absence)
 3. Tritanopia    (Blue-cone absence) 
 4. Achromatopsia ( Greyscale )""")

choice = int(input("Enter the Number :"))

match choice:
    case 1: GREEN()
    case 2: RED()
    case 3: BLUE()
    case 4: GREY()


# In[ ]:




