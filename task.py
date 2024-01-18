num_array =[]
for x in range(1,20):
    if x%2==0:
        num_array.append(x)
print("even number",num_array)
num_array.sort(reverse=True)
print(num_array)