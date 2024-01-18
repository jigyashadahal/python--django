import asyncio
# num_array =[]
# for x in range(1,20):
#     if x%2 !=0:
#         num_array.append(x)
# print("even number",num_array)
# num_array.sort(reverse=True)
# print(num_array)



# stringArray=["ram","shyam","hari","kaka","kaki","pustakalaya"]

# print(len(stringArray))
# evenArray=[]
# for x in range (1,len(stringArray)):
#     if x%2==0:
#         evenArray.append(x)
# print(evenArray)
# stringArray.pop(2)
# stringArray.insert(2,'hari dahal')
# print(stringArray)

# for index,value in enumerate(stringArray):
#     if index%2==0:
#             print(f"this is {index} and value is {value}")



 
#wap to convert temperatures to and from celcius and fahrenheit.
#[ formula : c/5= f-32/9[ where c  temperature in 
#celcius and f= temperature in fahrenheit]


# c= 60
# f=(c/5)*9 +32
# print(f)
    
# a= 2 
# b= 3
# print(a*b)




# anonymousFunction = lambda x, y: x+y
# print(anonymousFunction(10,6))

# def outerFunction(x):
#     def innnerFunction(y):
#         return x * y
#     return innnerFunction
# closure_instance = outerFunction(4)

# # print(closure_instance)

# result=closure_instance(5)

# print("result", result)

# def aFunction(a,b)
#     try:
#         result =a/b
#         return result 
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed")
#         return None
#     except Exception as e:
#         print(f"this is error:{e}")



#take auser input and pass it to the function parameters 
        #to take  input use input() function





# def bFunction(a,b):
#     try:
#         result= a/b
#         return result
#     except ZeroDivisionError:
#         print("Error: Divisible Zero is not allowed")
#         return None
#     except Exception as e:
#         print(f"this is an error:{e}")

# value_a =int(input('enter the number to be divided:'))
# value_b= int(input('enter the divisor number:'))
# print(bFunction(value_a, value_b))\


#wap to find to and form celcius and farenheit using function
#create both  function celciusToFarenheit and farenheitToCelcius
#formula f=(celcius *9/5) + 32 )* 5/9



# def celciusToFarhenheit(c):
#     f=(c * 9/5) + 32
#     return f


# def farenheitToCelcius(f):
#     c=(f - 32) * 5/9
#     return c


# n= int(input("to convert celcius to farhenheit  enter : 1 or to convert farhenheit to celcius ener 2"))
# if n==1:
#     c=int(input("enter celcius"))
#     result= celciusToFarhenheit(c)
#     print(result)

# else:
#     f=int(input("enter farhenheit"))
#     resultt= farenheitToCelcius(f)
#     print(resultt)

async def getData():
    print(" loading.......")
    print("loading.....")
    print("loadiang......")


    await asyncio.sleep(2)
    print('i am here after 2 second')
     
asyncio.run(getData())
    










