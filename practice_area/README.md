Hello from Mike. Here's what I figured out about using the PImage object:

loadpixels() is important - without it your PImage won't know what type of data it 
contains.

Images are lists of color values. If each colour value contains a single value the
is some important info for using PImagecolour will be greyscale. 3 values is RGB. 4 id RGBA. 5 is way out.
The list has a corresponding tuple key of the form
(x,y), which just tells the constructor what dimension the 1d list should fit into,
because for example a 20*30 or a 30*20 image will contain the same amount of pixels.
That's what the key is there for I think.

Setting a pixel from one image to be the same as a pixel in another image is as simple as

first_image[x, y] = second_image[x, y]

You need to make a constructor to index into the array like this:
suppose width = 50, height = 100:
for x in range(width):
    for y in range(height):
        index = x + y * width # this is optional - it is the index into the pixels
        first_image[x, y] = second_image[x, y]


the object being exchanged is the colour value of a pixel. Just remember to load_pixel on both images.

If you need to assign a different region of pixels from the second image into the first image, apply an offset to the x and y indexes of the second image.
