#client
from dcm import data_chunking_level_1
from interpreter import image_interpreter
from oir import optical_image_recognition
import time
import PythonMagick as pm 
import os
import cv2
import numpy as np
from mine import primary_search,secondary_search




height=1200
width=1000

skip_color_start=170
skip_color_end=225

blue=0
red=255
green =0

primary_row=[9,248,165]
secondary_col=[8,255,-1]
secondary_row=[5,248,165]



key_word_name = 'patient name'
key_word_test_start_1 = 'test'
key_word_test_start_2 = 'investigat'
key_word_test_start_3 = 'urine'


index_of_name_chunk = 2
index_of_test_start_idetifier = 3
index_of_test_end_idetifier = index_of_test_start_idetifier+2

identifier_row_name = 3
identifier_column_name= 2


identifier_row_test = 2
identifier_column_test= 2



chunking = data_chunking_level_1(height,width,skip_color_start,skip_color_end)
interpret = image_interpreter(red,green,blue)
oir=optical_image_recognition()
out_final=[]
horizontal_chunks = []

input_pdf_name = raw_input("enter file name: ")
os.system("pdftk "+input_pdf_name+" Burst output pages/pdf_name%02d.pdf")


img = pm.Image()
img.density("500")

for page in os.listdir("pages"):
    if page.endswith(".pdf"):
        img.read("pages/"+page)
        img.write("image/"+str(page.split('.')[0])+".jpg")
	os.remove("pages/"+page)


for item in os.listdir("image"):
    if item.endswith(".jpg") or item.endswith(".png"):
        image = "image/"+item
        img = cv2.imread(image)
        resized_image = cv2.resize(img, (height,width))
        gray = cv2.cvtColor(resized_image,cv2.COLOR_BGR2GRAY)
        column_vector =  gray.mean(axis=0)
        temp = np.array(column_vector.tolist())
        temp2 = temp[temp<110]
        if len(temp2) < 5:
            no_of_lines = 5 - len(temp2)
            i = cv2.line(resized_image,(width-no_of_lines,50),(width-no_of_lines,1150),(0,0,0),2*no_of_lines)
            cv2.imwrite( image,i)

name_data = []
test_data = []

for item in os.listdir("image"):
    if item.endswith(".jpg") or item.endswith(".png"):
        image = "image/"+item    
        #start_t = time.time()
        data_dict,gray,horizontal_chunk_index= chunking.draw_table_on_image_file(image,primary_row,secondary_col,secondary_row)
        # horizontal_chunk_index, gray = chunking.draw_row_chunks_on_image_file(image,primary_row)
        # horizontal_chunks.append(horizontal_chunk_index)
        interpret.draw_primary_row_chunks(image,height,width,horizontal_chunk_index)
        interpret.draw_table(image,data_dict)
        # out=oir.crop_image(gray,data_dict)
        # out_final.append(out)
        # interpret.print_output_data(out)
        # find_start = primary_search()
        # data_list  = find_start.clean_data(out.tolist())
        # name_start_index = find_start.data_division_start(data_list,key_word_name,'*********','*******************',index_of_name_chunk, identifier_row_name ,identifier_column_name)
        # print('name:'+str(name_start_index))

        # test_start_index = find_start.data_division_start(data_list,key_word_test_start_1,key_word_test_start_2,key_word_test_start_3,index_of_test_start_idetifier, identifier_row_test, identifier_column_test)
        # print('test:'+str(test_start_index))

        # secondary_divide = secondary_search()
        # if name_start_index is not None and test_start_index is not None:
        #     divided_data_name = secondary_divide.secondary_division(name_start_index,test_start_index,data_list)
        #     name_data.append(divided_data_name)
        # test_end_index = len(data_list)
        # # print('end:'+str( test_end_index))
        # if test_start_index is not None:
        #     test_data.append(data_list[test_start_index:len(data_list)])

        # general_physical_exam = secondary_divide.general_physical(data_list)

        os.remove("image/"+item)
       #end_t = time.time()
#print("total: "+str(end_t-start_t))
#print(out_final)
# print(horizontal_chunks)
print(name_data)
print('\n')
print('\n')
print(test_data)
print('\n')
print('\n')
print(general_physical_exam)





