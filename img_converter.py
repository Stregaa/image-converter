# Converts images to greyscale
# pip install opencv-python

import cv2
import numpy as np

shades = 10

def input_image():
    # Asks user for the file to be converted
    file = input("File name of image: ")
    
    return file

def type_of_conversion():
    # Asks user for type of conversion
    conversion = int(input("Greyscale[1], paint-filter[2], both[3], or the bonus sp00ky filter[4]? "))
    
    return conversion

def convert_grey(file):
    # Converts image to greyscale and saves result
    img = cv2.imread(file, 0)
    save_image(img, file)

    return

def convert_paint(file):
    # Converts image to paint and saves result
    img = cv2.imread(file)
    
    # Converts image to RGB as a float
    bgr = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    bgr = bgr.astype(np.float32)/255

    # Quantize and convert back to range 0 to 255 as 8-bits
    paint = 255*np.floor(bgr*shades+0.5)/shades
    paint = paint.clip(0,255).astype(np.uint8)

    save_image(paint, file)

    return

def convert_both(file):
    # Converts image to both greyscale and paint and saves result
    img = cv2.imread(file)
    
    # Converts image to greyscale as a float
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grey = grey.astype(np.float32)/255

    # Quantize and convert back to range 0 to 255 as 8-bits
    both = 255*np.floor(grey*shades+0.5)/shades
    both = both.clip(0,255).astype(np.uint8)

    save_image(both, file)

    return

def convert_spooky(file):
    # Converts image to paint and saves result
    img = cv2.imread(file)
    
    # Converts image to RGB as a float
    bgr = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    bgr = bgr.astype(np.float32)/255

    # Quantize and convert back to range 0 to 255 as 8-bits
    paint = 255*np.floor(bgr*shades+0.5)/shades
    paint = paint.clip(0,255).astype(np.uint8)

    save_image(paint, file)

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
        convert_paint(file)
        print("Applied paint filter!")

    elif conversion_type == 3:
        convert_both(file)
        print("Applied both greyscale and paint filter!")
    
    elif conversion_type == 4:
        convert_spooky(file)
        print("Applied sp00ky filter!")
    
    else:
        print("Invalid conversion type - please choose 1, 2, 3, or 4.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()