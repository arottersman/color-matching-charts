from PIL import Image
import math

def main():

    # PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
    img = Image.new( 'RGB', (1920,1080), "black") # create a new black image
    pixels = img.load() # create the pixel map

    img_screensize = 1920*1080
    img_w = 1920
    img_h = 1080
    usepixel = 1
    colorboxsize = 8
    myset = 1

    colours_length = 256*256*256
    colours = []
    for i in range(1, colours_length):
        colours.append(getRGBfromI(i))

    colours.sort(key=lambda rgb: lum(*rgb))

#
    for counter in range(1,33):

        for r in range(1,img_w,colorboxsize):  # for every col:
            for c in range(1,img_h,colorboxsize):  # For every row

                for rb in range(0,colorboxsize-1):
                    for cb in range(0,colorboxsize-1):
                        pixels[r, c] = colours[usepixel]

                usepixel += 4

        #usepixel = usepixel + (img_screensize / 4) # for now
        print(counter)
        filename = "D://Files2017_MaxoticsVideo_2//02_SLOG_Explain_2//TestImages//FillDisplaySize//in32LumaSortSkip4//colors_" \
                   +str(counter).zfill(2)+".bmp"
        print(filename)
        img.save(filename)

    #img.show()

def lum(r, g, b):
    return math.sqrt(.241 * r + .691 * g + .068 * b)

def getRGBfromI(RGBint):
    blue =  RGBint & 255
    green = (RGBint >> 8) & 255
    red =   (RGBint >> 16) & 255
    return red, green, blue

def getIfromRGB(rgb):
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    print red, green, blue
    RGBint = (red<<16) + (green<<8) + blue
    return RGBint

if __name__ == "__main__": main()