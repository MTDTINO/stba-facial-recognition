import cv2 as cv
import  numpy as np

#load the image 
img = cv.imread('sample-images/images/2.jpg')

#convert the image to grayscale
grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#load cascade classifiers
cascade_default = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

#detect faces
faces_default = cascade_default.detectMultiScale(grayscale)

#draw rectangle around faces
def show_detection(image, faces):
    """Draws a rectangle over each detected face"""

    for (x, y, w, h) in faces:
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return cv.imshow('image',image)


#draw detected faces
show_detection(img, faces_default)
cv.waitKey(0)
cv.destroyAllWindows()

                                        # lbp vector #

# Define the offsets of the pixels in the circular neighborhood
radius = 1
n_points = 8 * radius
theta = np.linspace(0, 2*np.pi, n_points+1)[:-1]
circle_offsets = np.stack([np.round(radius*np.cos(theta)).astype(int), np.round(radius*np.sin(theta)).astype(int)], axis=1)

# If no face is detected, return None
if len(faces_default) == 0:
    print(None)

# Get the coordinates of the largest face
(x, y, w, h) = sorted(faces_default, key=lambda x: x[2]*x[3], reverse=True)[0]

# Crop the face from the image
face = grayscale[y:y+h, x:x+w]

# Resize the face to a fixed size
face = cv.resize(face, (48, 48))

# Calculate the LBP feature vector for the face
radius = 1
n_points = 8 * radius
lbp = np.zeros((48, 48), dtype=np.uint8)
for i in range(radius, 48 - radius):
    for j in range(radius, 48 - radius):
        center_pixel = face[i, j]
        pixel_values = [face[i + dx, j + dy] for (dx, dy) in circle_offsets]
        bit_values = [int(p >= center_pixel) for p in pixel_values]
        lbp_code = sum([bit_values[i] << i for i in range(n_points)])
        lbp[i - radius, j - radius] = lbp_code
lbp_hist, _ = np.histogram(lbp, bins=range(0, 2**(n_points+1), 2))

# Normalize the feature vector to have unit L2 norm
lbp_hist = lbp_hist.astype(float)  # Convert array to float type
lbp_hist /= np.sqrt(np.sum(lbp_hist**2))

# Return the feature vector
print (lbp_hist)


#write the lbp vector to a file
with open('vector.txt', 'w') as file:
    for number in lbp_hist:
        file.write(str(number) + '\n')
