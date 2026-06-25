name = input("Enter student name: ")
sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total/5

print("\nStudent Name:", name)
print("Total Maeks:", total)
print("Percentage:", percentage)

if percentage >=90:
  print("Grade: A+")
elif percentage >= 75:
  print("Grade: A")
elif percentage >= 60:
  print("Grade: B")
elif percentage >= 40:
  print("Grade: C")
else:
  print("Grade: F")
