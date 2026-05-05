word = "indore@#$123"
count = 0

for i in word:
    if i.isalpha() == False and i.isnumeric() == False:
        count+=1
print(count)
