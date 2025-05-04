#task_1

Mark_list = {'Alice':85,'Nike':50,'Joy':70,'Prem':80}
A=str(input('Enter the student\'s name: '))
if A in Mark_list:
    print( A , '\'s' , ' marks: ',Mark_list[A] , '\n' )
else:
    print('Student not found.\n')

#task_2

list = [ i for i in range(1,11) ]
print("Original list: ", list)

Extract=list[0:5]
print("Extracted first five elements: ", Extract)
Extract.reverse()
print("Reversed extracted elements: ", Extract)

#end