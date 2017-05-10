import numpy as np
import cv2
import sys
import subprocess
from subprocess import *

img = cv2.imread('redShirt.png')
b,g,r = cv2.split(img)
img2 = cv2.merge((b,g,r))
(h,w) = img2.shape[:2]
center = (w/2, h/2)
M = cv2.getRotationMatrix2D(center, 270,1.0)
rotated = cv2.warpAffine(img, M,(w,h))
rotated[:] = (0,0,0) 
cv2.imshow('Rotated', rotated)
cv2.waitKey(10000)
cv2.destroyAllWindows()

#####



# Get user supplied values
subprocess.call(['streamer' ,'-f', 'jpeg', '-o', 'TestPic.jpeg'])

imagePath = 'TestPic.jpeg'
cascPath = sys.argv[1]

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)



#############



from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import webcolors


def distance(color1, color2):
    return math.sqrt(sum([(e1-e2)**2 for e1, e2 in zip(color1, color2)]))

def best_match(sample, colors):
    by_distance = sorted(colors, key=lambda c: distance(c, sample))
    # print(by_distance[0])
    return by_distance[0]


img = cv2.imread('TestPic.jpeg')
height, width, dim = img.shape


img = img[(height/4):(3*height/4), (width/4):(3*width/4), :]
height, width, dim = img.shape

img_vec = np.reshape(img, [height * width, dim] )

kmeans = KMeans(n_clusters=3)
kmeans.fit( img_vec )



unique_l, counts_l = np.unique(kmeans.labels_, return_counts=True)
sort_ix = np.argsort(counts_l)
sort_ix = sort_ix[::-1]

fig = plt.figure()
ax = fig.add_subplot(111)
x_from = 0.05

colors = [

(0,0,0),
(255,255,255),
(255,0,0),
(0,0,255),
(255,255,0),
(128,128,128),
(0,128,0),
(128,0,128),
(255,165,0),
(255,192,203),
(192,192,192),
(128,128,128),
(128,0,0),
(255,0,255),
(255,0,255),
(128,128,0),
(0,0,128),
(0,128,128),
(0,255,255),
(165,42,42),
(210,180,140)

]
count = 0;
for cluster_center in kmeans.cluster_centers_[sort_ix]:
    facecolor = ''
    actual_name = ''
    closest_name = ' '
    ax.add_patch(patches.Rectangle( (x_from, 0.05), 0.29, 0.9, alpha=None,
                                    facecolor='#%02x%02x%02x' % (cluster_center[2], cluster_center[1], cluster_center[0] ) ) )
    # print 'facecolor is: ' + webcolors.hex_to_name('#%02x%02x%02x' % (cluster_center[2], cluster_center[1], cluster_center[0] ))


    # print colordb.nearest('#%02x%02x%02x' % (cluster_center[2], cluster_center[1], cluster_center[1] ))
    requested_colour = (  int(cluster_center[2]), int(cluster_center[1]), int(cluster_center[0]))

    # print (webcolors.rgb_to_name(requested_colour))
    # print (webcolors.rgb_to_name((0,0,0)))
    if (count == 0):
        print(webcolors.rgb_to_name(best_match(requested_colour,colors)))
        count += 1

    # print requested_colour
    # actual_name, closest_name = get_colour_name(requested_colour)
    # print actual_name
    x_from = x_from + 0.31


# plt.show()

# requested_colour = (119, 172, 152)
# actual_name, closest_name = get_colour_name(requested_colour)

# print "Actual colour name:", actual_name, ", closest colour name:", closest_name


