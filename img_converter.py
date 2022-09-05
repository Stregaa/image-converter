# Converts images to greyscale
# pip install opencv-python

import cv2
import numpy as numpy

shades = 10

def input_image():
    # Asks user for the file to be converted
    file = input("File name of image: ")
    
    return file

def type_of_conversion():
    # Asks user for type of conversion
    conversion = int(input("Greyscale[1], paint-filter[2], or both[3]? "))
    
    return conversion

def convert_grey(file):
    # Converts image to greyscale and saves result
    img = cv2.imread(file, 0)
    save_image(img, file)

    return

def convert_paint(file):
    # Converts image to paint and saves result
    img = cv2.imread(file, 0)
    
    save_image(img, file)

    return

def convert_both(file):
    # Converts image to both greyscale and paint and saves result
    img = cv2.imread(file)
    
    # Convert image to greyscale as a float
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grey = grey.astype(numpy.float32)/255

    # Quantize and convert back to range 0 to 255 as 8-bits
    both = 255*numpy.floor(grey*shades+0.5)/shades
    both = both.clip(0,255).astype(numpy.uint8)

    save_image(both, file)

    return

def save_image(img, file):
    # Saves converted image and displays it in a window
    cv2.imshow("converted image", img)
    new_string = file.split(".")
    cv2.imwrite(new_string[0] + '_converted.png', img)

def main():
    file = input_image()
    conversion_type = type_of_conversion()

    if conversion_type == 1:
        convert_grey(file)
        print("Applied greyscale!")
    
    elif conversion_type == 2:
        print("Applied filter!")

    elif conversion_type == 3:
        convert_both(file)
        print("Applied both greyscale and filter!")
    
    else:
        print("Invalid conversion type - please choose 1, 2, or 3.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()