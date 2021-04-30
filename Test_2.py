""" 

In this program we will use the grades in the Final.txt file
to calculate the number of grades, average grades, and percentage of grades above average. 


"""
"""
Creat Main function
crat dicionary
read Final.txt using open()
close infile
for i in range
GRADES [] = INT IGRADES 
average= Sum grades / len grades
get percentage average of above average grades. 
if grades > average

print (number of grades)
print (average grade)
print(Precentage of grade above average)

"""


def main():
    finaldict = create.dictionary("Final.txt")
    displayinfoavoutfinalgrades(finaldict)

infile = open("Final.txt", 'r')
grades = [line.rstrip() for line in infile]
infile.close()

for i in range(len(grades)):
    grades [i] = int(grades [i])
average = sum(grades) / len(grades)
num = 0
for grade in grades:
    if grade>average:
        num += 1
print("Number of grades:", len(grades))
print("Average grade:", average)
print("Percentage of grades above average: {0:.2f}%".format(100 * num / len(grades)))

