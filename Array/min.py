#Find The Lowest Value in an Array

arr=[7, 12, 9, 4, 11]
min=arr[0]
for i in arr:
    if (i<=min):
        min=i

print(min)