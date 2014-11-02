#Pseudocode master projex
#each exercise is split in two parts: 
#One in Galsim, which constructs the images(galaxies, shear, noise, etc)
#The other selfwritten, which calculates the moments and for this 
#calculates the measured shear

#Exercise 1: Ideal case(no noise, no PSF)
#Take the easiest case: image cube, with each slice only containing one galaxy
#Starting point: demo4.py

import numpy as np
import pyfits as pf
import galsim
import os


#creating output directory
if not os.path.isdir('output'):
   os.mkdir('output')

filename = os.path.join('output','galaxiesIdeal.fits')

#Initial conditions & Global constants
#values taken from demo4.py
random_seed = str(82415738435418735457811235518)
sky_level = 1.e6                # ADU / arcsec^2
pixel_scale = 1.0               # arcsec / pixel  (size units in input catalog are pixels)
gal_flux = 1.e6                 # arbitrary choice, makes nice (not too) noisy images
xsize = 64                      # pixels
ysize = 64                      # pixels

#reduced Shear
gal_g1 = -0.009                 #
gal_g2 = 0.011                  #

#Taking input Catalog from Galsim example
#only using the number of objects in the catalog
catalog_filename = os.path.join('./GalSim-1.1.0/examples/input','galsim_default_input.asc.txt')
cat = galsim.Catalog(catalog_filename)

#output list which will contain our galaxy images
images =[]

print 'number of items in catalog:\t' + str(cat.nobjects)

while len(random_seed) <= cat.nobjects:
   random_seed +=random_seed

for i in range(cat.nobjects):
   #creating random galaxy
   rndm = float(random_seed[i])
   rndm2 = float(random_seed[4+i])
   gal = galsim.Gaussian(flux = rndm*gal_flux, sigma = rndm2)
   
   #adding shear
   gal.applyShear(g1=gal_g1,g2=gal_g2)
   
   #shift the center
   gal.applyShift(dx = 1./rndm ,dy = 1./rndm2) 

   final = gal
   
   #Draw the profile
   image = galsim.ImageF(xsize,ysize)

   final.draw(image=image, scale=pixel_scale)
   
   #add the drawn image to the list
   images.append(image)
   print 'list length:\t', len(images)

#write images to .fits file
galsim.fits.writeCube(images, filename)

#----------------End of Galsim part-----------------


   
   










