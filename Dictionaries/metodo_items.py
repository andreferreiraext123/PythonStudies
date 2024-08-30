classmates = {
    "André":    [10,2,7,9],
    "Mateus":   [10,9,1,8],
    "Felipe":   [9,10,2,7],
    "Luiz":     [9,1,2,5],
}

items = classmates.items()
print('\n',items,'\n')

for student, grades in classmates.items(): # Using method items (for) for iterate the tuple from dictionary classmates
    print(f"Aluno:  {student}, Grades:  {grades}")

print()

for student in classmates:
    print(f"Aluno:  {student}") # The repetition structure (for) just can iterate the key in dicionaries
