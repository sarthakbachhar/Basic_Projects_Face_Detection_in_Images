import cv2

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier("C:\\Users\\Acer\\Desktop\\haarcascade_frontalface_default.xml")

# Load image
img = cv2.imread("C:\\Users\\Acer\\Desktop\\Project 10\\elon.jpg")

# Check if the image was loaded successfully 
if img is None:
  print("Unable to load image.")
  
else:
  # Convert image to grayscale 
  img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  # Detect faces in grayscale image
  faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=10, minSize=(30,30))

  # Draw rectangles around detected faces
  for(x,y,w,h) in faces:
   cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),2)

  # Resize the image for display (optional)
  display_img = cv2.resize(img, (800, 600))
    
  # Display the image with detected faces
  cv2.imshow("Detected Faces", display_img)
    
  # Wait until a key is pressed
  cv2.waitKey(0)

  # Destroy all windows opened by OpenCV
  cv2.destroyAllWindows()

  # Save the output image with detected faces
  cv2.imwrite("C:\\Users\\Acer\\Desktop\\Project 10\\elon_final.jpg", img)