students={1:"Ram", 22:"Jayul",
3:"Rahul",44:"Anjali",50:"Riya"}
print(students)
students[33]="Hiral"
print(students)

students.setdefault(101,"Sita")
print(students)
students.setdefault(102,"")
students[102]="Ravan"
print(students)
