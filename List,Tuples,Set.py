courses=['Theory of computation','Computer Networks',"DBMS","DIP"]
print(courses[:2])
print(courses[2:])
courses.append('Cloud Computing')                   
courses.insert(0,'Machine Learning')
print(courses)
courses2=["Mathematics","Linux System"]
# courses.insert(0,courses2)
courses.extend(courses2)
print(courses)
courses.remove("Cloud Computing")
print(courses)
last_course=courses.pop()
print(last_course)
courses.reverse()
print(courses)
courses.sort()
print(courses)
num=[1,5,22,4,62]
# num.sort()
# print(num)
# num.sort(reverse=True)
# print(num)
sortedNumbers=sorted(num)
print("Sorted:",sortedNumbers)
print("Original: ",num)
print("minimum: ",min(num))
print("maximum: ",max(num))
print("Sum: ",sum(num))
print(courses.index("Mathematics"))
print(("Sanskrit" in courses)) 
for item in courses:
    print(item)
for index,course in enumerate(courses,start=1):
    print(index,course)
courseString=' - '.join(courses)
print(courseString)
newList=courseString.split(" - ")
print(newList)
print('Lists are mutable and Tuples are not muttable')
CourseSet={"Math","Math","History","Art"}
#Set helps us use in method like lsits but is optimised for it specificaaly
# and also Set operations
School={"Art","Design"}
print(CourseSet.intersection(School))
print(CourseSet.difference(School))
print(CourseSet.union(School))
emptyList=[]
emptyList2=list()
emptyTuple=()
emptyTuple2=tuple()
print("we cannot create empty set like emptySet={},\n this will result into an dictionary we will have to use builtin set()function")
