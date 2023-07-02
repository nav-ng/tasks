# def add(num1,num2):
#     sum=0
#     for i in range(num2):
#         sum+=num1
#     return sum


# def multiplication(num1,num2):
#     if num2>0:
#         return add(num1,num2)
#     elif num2<0:
#         num1=-num1
#         num2=-num2
#         return add(num1,num2)
#     else:
#         return "answer = 0"
    

# print(multiplication(-3,-5))




# def multiply(a, b):
#     if b < 0:
#         a = -a
#         b = -b
#     result = 0
#     while b > 0:
#         result += a
#         b -= 1
#     return result

# # Example usage
# print(multiply(-3, -3))  # Output: 9




# input_string="hEllO guys"
# for i in input_string:
#     if i.lower() in ['a','e','i','o','u']:
#         input_string=input_string.replace(i,"")
# print(input_string)


input_str="893334333"
output_str=""
size=len(input_str)
for i in range(size):
    temp=i
    for j in range(size-1,i,-1):
        if input_str[i]==input_str[j]:
            output_str+=input_str[i]
            i+=1
        else:
            output_str=""
            i=temp
print(output_str)
