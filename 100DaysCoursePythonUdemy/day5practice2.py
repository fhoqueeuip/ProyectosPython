# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
masAlto = 0
for nota in student_scores:
    if nota > masAlto:
        masAlto = nota
print(f"La nota mas alta es {masAlto}")

