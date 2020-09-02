# Cam-scanner-python
cam scanner python project made using opencv and numpy python library

# About project
The script takes an image as input and then scans the document from the image , applies few image processing techniques and gives output with scanned effect

# How does it work?
1.Resize the images using cv2.resize so OpenCV can handle it.

2.Guassian Blur to smoothen image.

3.Canny Edges to detect the edges.

4.Find contours and boundary of the page.

5.Map the end points of contours to 800 * 800 window.

6.Apply perspective trasform to get scanned or bird eye view of the image.
