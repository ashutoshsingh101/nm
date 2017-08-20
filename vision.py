# from google.cloud import vision
# import io
import matplotlib.pyplot as plt
import cv2



# vision_client = vision.Client()

# image_file= io.open('image/pdf_name02.jpg','rb')
# content = image_file.read()
# image = vision_client.image(content=content)
# want = image.detect_full_text()

# print(want.text)



img = cv2.imread('pdf_name12.jpg')
resized_image = cv2.resize(img, (800,600))
gray = cv2.cvtColor(resized_image,cv2.COLOR_BGR2GRAY)

row_vector = gray.mean(axis=1)


column_vector =  gray.mean(axis=0)
fig = plt.figure(figsize= (10,10))

for i in range(len(column_vector)):
	plt.scatter(i,column_vector[i])
	


plt.margins(0.2)
plt.show()
plt.savefig('nm.png',type = 'png')