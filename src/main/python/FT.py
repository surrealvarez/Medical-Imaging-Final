
import numpy as np
import cv2
from skimage.draw import circle
from skimage.draw import rectangle
from math import floor
from PIL import Image

class DFT:

    #generates the first phantom image
    def phantom1(self, x, y):
        #begins the first image with the size (x,y)
        img = np.zeros((y,x),dtype='uint8')

        rr, cc = circle(y/2,x/2,floor(x*.39))
        img[rr,cc] = 100

        recHeight = floor(y*.58)
        recWidth = floor(x*.12)

        originY = floor((y/2)-(recHeight/2))
        originX = floor((x/2)-(recWidth/2))
        #coordinate of the origin
        start = (originY, originX)
        extent = (floor(y*.58),floor(x*.12))
        rr, cc = rectangle(start, extent=extent,shape=img.shape)

        img[rr,cc] = 255

        # cv2.imwrite('phantom1.jpg',img)
        # cv2.imread('phantom1.jpg')
        return img

    #generates the second phantom image
    def phantom2(self, x, y):

        img = np.zeros((y,x),dtype='uint8')

        #main circle holding others
        rr, cc = circle(x*.5,y*.5,int(round(x*0.390625)))


        img[rr,cc] = 100
        #generates multiple circles at a ratio

        #vertical position, horizontal position, diameter
        rr, cc = circle(int(y*.5), int(round(x*0.15625)), int(round(x*0.01953125)) )
        img[rr,cc] = 255

        rr, cc = circle(int(y*.5), int(round(x*0.25390625)), int(round(x*0.0390625)))
        img[rr,cc] = 255

        rr, cc = circle(int(y*.5), int(round(x*0.390625)), int(round(x*0.05859375)))
        img[rr,cc] = 255

        rr, cc = circle(int(y*.5), int(round(x*0.56640625)), int(round(x*0.078125)))
        img[rr,cc] = 255

        rr, cc = circle(int(y*.5), int(round(x*0.771484375)), int(round(x*0.09765625)))
        img[rr,cc] = 255

        return img


    def load_display(self, image):

        #Create a output window
        cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)

        #shows image
        cv2.imshow("Image", image)

        cv2.waitKey(0)

        #destroy windows
        cv2.destroyWindow("Image")

    def magnitude(self, image):
        #gets the width and height of the input image
        height, width = image.shape
        #iterates and ensures values aren't negative
        for h in range(height):
            for w in range(width):
                # if negative convert to positive
                if image[h][w] < 0:
                    image[h][w] *= -1
        return image

    def radial(self, image, cutoff):

        """Computes a Ideal low pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the ideal filter
        returns a ideal low pass mask"""
        height = image.shape[0] # P
        width = image.shape[1] # Q


        mask = np.copy(image)

        for u in range(height):
            for v in range(width):
                #used the pythagorean theorem to check if the coordinate position is within range
                duv = ((u - height/2)**2 + (v - width/2)**2)**(1/2)
                if duv <= cutoff:
                    mask[u, v] = 1 #If in range leave at 1
                elif duv > cutoff:
                    mask[u, v] = 0 #If out of range change to black

        maskedimg = np.multiply(image, mask)

        return maskedimg

    def cartesianMask (self, image, repetitions):

        height,width = image.shape
        mask = image.copy()
        #0 is black
        #iterates through image depending on the user input
        for h in range (height):
            for w in range(width):
                if h < repetitions:
                    mask[h,w] = 1
                elif h >= repetitions:
                    mask[h,w] = 0

        maskedimg = np.multiply(image, mask)

        return maskedimg
    def shiftedDFT(self, img):
        # run dft on image
        img = np.fft.fft2(img)
        img = np.fft.fftshift(img)
        return img

    def revertDFT(self, img):
        #revert DFT to get back calculated image
        img = np.fft.ifftshift(img)
        img = np.fft.ifft2(img)
        return img


    def prepareFinalOutput(self, img):
        # Steps before outputting!----------------------------------------

        # this image will be returned
        magDFT = img.copy()
        magDFT = self.magnitude(magDFT)
        # magDFT = 10 * np.log(magDFT)
        magDFT = magDFT.astype("uint8") #Makes it a type that can output
        # --------------------------------
        return magDFT

    def prepareOutput(self, img):
        #Output for DFT k-spaces
        # this image will be returned
        magDFT = img.copy()
        magDFT = self.magnitude(magDFT)
        magDFT = 10 * np.log(magDFT)
        magDFT = magDFT.astype("uint8") #Makes it a type that can output

        # --------------------------------
        return magDFT

# if __name__ == '__main__':
#     dft = DFT()
#     #read image
#     #img = cv2.imread('Lenna0.jpg', 0)
#     img = dft.phantom1(512,512)
#     # dft.load_display(img)
#     height, width = img.shape
#     # 512*.5 =256
#     img = dft.shiftedDFT(img)
#     # img = dft.radial(img,cutoff=400)
#     img = dft.cartesianMask(img, 600)
#     # img = dft.prepareOutput(img)
#     # dft.load_display(img)
#
#     #Revert dft
#     img = dft.revertDFT(img)
#     img = dft.prepareFinalOutput(img)
#     dft.load_display(img)




