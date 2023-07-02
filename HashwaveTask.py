# def duplicate_count(input_list):
#     output_dict = {}

#     if type(input_list) != list:
#         return "Invalid"
    
#     for i in range(len(input_list)):
#         count = 1
#         if input_list[i] not in output_dict.keys():
#             for j in range(i+1, len(input_list)):
#                 if input_list[i] == input_list[j]:
#                     count += 1
#             output_dict[input_list[i]] = count
    
#     return output_dict


def length(input_list):
    l=0
    for i in input_list:
        l+=1
    return l


def duplicate_count(input_list):
    temp_list=[]
    output_dict={}

    if type(input_list)!=list:
        return "Invalid"
    
    for i in range(length(input_list)):
        count=1
        if input_list[i] not in temp_list:
            for j in range(i+1, length(input_list)):
                if input_list[i]==input_list[j]:
                    count+=1
            temp_list.append(input_list[i])
            output_dict[input_list[i]]=count
    return output_dict



print(duplicate_count([1,3,5,2,2,7,7,9,4,5,"a","a","h","j","h"]))