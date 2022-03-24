print("THe method of calcuating sum of cubes\n")
no_of_inputs = int(input("Enter the number of sides in you cube::::"))
i = 0
while(i < no_of_inputs):
    x = int(input("Enter the size of cube side %i:::::" %(i+1) ))
    if(i == 0):
        sum = x
        i = i + 1
        continue
    sum = sum + x
    i = i + 1
print("The sum of your %i size cube is %i" %(no_of_inputs,sum))
