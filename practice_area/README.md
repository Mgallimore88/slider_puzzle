Hello from Mike. Here's what I figured out about using the PImage object:

loadpixels() is important - without it your PImage won't know what type of data it 
contains.

Images are lists of color values. If each colour value contains a single value the
is some important info for using PImagecolour will be greyscale. 3 values is RGB. 4 id RGBA. 5 is way out.
The list has a corresponding tuple key of the form
(x,y), which just tells the constructor what dimension the 1d list should fit into,
because for example a 20*30 or a 30*20 image will contain the same amount of pixels.
That's what the key is there for I think.
