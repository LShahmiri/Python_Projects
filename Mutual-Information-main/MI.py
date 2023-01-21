
"""MI FUNCTION.ipynb


import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imshow, imread
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from skimage import color, exposure, transform
from skimage.exposure import histogram, cumulative_distribution, equalize_hist
from skimage import img_as_ubyte, img_as_uint
import cv2
import numpy as np
from google.colab.patches import cv2_imshow
import glob
import matplotlib.pyplot as plt
from __future__ import print_function  # print('me') instead of print 'me'
from __future__ import division  # 1/2 == 0.5, not 0
import numpy as np  # the Python array package
import matplotlib.pyplot as plt
import nibabel as nib
import cv2


def mutual_information(hgram):
   pxy = hgram / float(np.sum(hgram))
   px = np.sum(pxy, axis=1) # marginal for x over y
   py = np.sum(pxy, axis=0) # marginal for y over x
   px_py = px[:, None] * py[None, :] # Broadcast to multiply marginals
# Now we can do the calculation using the pxy, px_py 2D arrays
   nzs = pxy > 0 # Only non-zero pxy values contribute to the sum
   return np.sum(pxy[nzs] * np.log(pxy[nzs] / px_py[nzs]))


plt.rcParams['image.cmap'] = 'BrBG'
plt.rcParams['image.interpolation'] = 'nearest'
path='/content/drive/MyDrive/dataset-new/100-chinesdataset/Magnolia/*.*'
img_number = 1  
for file in glob.glob(path):
    filename = os.path.basename(file)
    a= cv2.imread(file) 
    
    img1=cv2.imread('/content/drive/MyDrive/dataset-new/100-chinesdataset/Magnolia/85_1.jpg')
    np.corrcoef(img1.ravel(), a.ravel())[0, 1]
    hist_2d, x_edges, y_edges = np.histogram2d(img1.ravel(),a.ravel(),bins=20)
    c=mutual_information(hist_2d)
    
    print(c)
    img_number +=1 
    cv2.waitKey(1000) 
    cv2.destroyAllWindows()







