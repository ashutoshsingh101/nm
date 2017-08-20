import re
import numpy as np



class primary_search():
    
    def __init__(self):
        pass

    def clean_data(self,data):
        for primary_segment in data:
            for row in primary_segment:
                for cell in row:
                    if type(cell) is dict:
                        if cell['text'] == '':
                            del cell
                        else:
                            cell['text'] = cell['text'].lower()
                    else:
                        del cell
        return data

    def locator(self,any_list,identifier):
        new_list = []
        if type(any_list) is not dict:
            if len(any_list) >= identifier+2:
                # new_list.extend([any_list[identifier-2],any_list[identifier-1],any_list[identifier],any_list[identifier+1],any_list[identifier+2]])
                new_list = any_list[identifier-2:identifier+2]
            elif len(any_list) >= identifier+1:
                # new_list.extend([any_list[identifier-2],any_list[identifier-1],any_list[identifier],any_list[identifier+1]])
                new_list = any_list[identifier-2:identifier+1]
            else:
                new_list = any_list
        return new_list



    def data_division_start(self,data_list,key_word_1,key_word_2,key_word_3,index_of_start_idetifier,identifier_row,identifier_column):
        start= []
        for primary_segment in range(len(data_list)):
            row_list = self.locator(data_list[primary_segment],identifier_row)
            if row_list is not None or len(row_list) != 0:
                for row in row_list:
                    column_list = self.locator(row,identifier_column)
                    if column_list is not None or len(column_list) != 0:
                        for column_offset in range(len(column_list)):
                            if key_word_1 in self.locator(row,identifier_column)[column_offset]['text'] or key_word_2 in self.locator(row,identifier_column)[column_offset]['text']or key_word_3 in self.locator(row,identifier_column)[column_offset]['text']:
                                start = primary_segment
                                return start
   

    def data_division_end(self,data_list,key_word,test_start_index):
        end= None
        end_found = False
        for primary_segment in range(test_start_index,len(data_list)):
            for row in data_list[primary_segment]:
                for column in row:
                    if type(column) is dict:
                        if column['text'].startswith(key_word):
                                end = primary_segment
                                end_found = True
                                break
                if end_found:
                    break
            if end_found:
                break
        return end




class secondary_search():

    def __init__(self):
        pass

    def secondary_division(self,start_index,end_index,data_list):
        divided_data = []
        for primary_segment in range(start_index,end_index):
            divided_data.append(data_list[primary_segment])
        return divided_data

    def general_physical(self,data_list):
        height_found = False
        for primary_segment in range(len(data_list)):
            for row in data_list[primary_segment]:
                for column in row:
                    if type(column) is dict:
                        if 'general physical' in column['text']:
                            return data_list
                        else:
                            if 'height' in column['text']:
                                height_found = True
                                if height_found == True:
                                    if 'weight' in column['text']:
                                        return data_list

    