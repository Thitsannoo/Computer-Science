gap = 4
base = 50
heightChk = True

while heightChk == True:
    length = int(input('Enter length: '))
    width = int(input('Enter width: '))
    height= int(input('Enter the height (between 1 and 100) :'))
    if height<=1 and height>=100:
        heightChk = False

panel = 2*length + 2*width - gap
area = 0.5 * base * height
print ('Base of the triangle: ',base)
print ('Height of the triangle', height)
print ('Area of the triangle: ', area)
print ('The number of panels needed is ',panel)