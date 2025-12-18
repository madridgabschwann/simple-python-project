# Interactive Science Quiz Game
# This program asks science questions and shows the user's score

print("🧪 Welcome to the Interactive Science Quiz Game!")
print("Answer the questions by typing A, B, or C.")
print("---------------------------------------------")

# Variable to store the score
score = 0

# Question 1
print("\n1. What planet is known as the Red Planet?")
print("A. Earth")
print("B. Mars")
print("C. Jupiter")
answer1 = input("Your answer: ").upper()

if answer1 == "B":
    print("Correct! 🎉")
    score += 1
else:
    print("Wrong ❌ The correct answer is B. Mars")

# Question 2
print("\n2. What gas do plants need for photosynthesis?")
print("A. Oxygen")
print("B. Nitrogen")
print("C. Carbon Dioxide")
answer2 = input("Your answer: ").upper()

if answer2 == "C":
    print("Correct! 🎉")
    score += 1
else:
    print("Wrong ❌ The correct answer is C. Carbon Dioxide")

# Question 3
print("\n3. What organ pumps blood through the body?")
print("A. Brain")
print("B. Lungs")
print("C. Heart")
answer3 = input("Your answer: ").upper()

if answer3 == "C":
    print("Correct! 🎉")
    score += 1
else:
    print("Wrong ❌ The correct answer is C. Heart")

# Question 4
print("\n4. What force keeps us on the ground?")
print("A. Magnetism")
print("B. Gravity")
print("C. Friction")
answer4 = input("Your answer: ").upper()

if answer4 == "B":
    print("Correct! 🎉")
    score += 1
else:
    print("Wrong ❌ The correct answer is B. Gravity")

# Question 5
print("\n5. What part of the plant makes food?")
print("A. Roots")
print("B. Stem")
print("C. Leaves")
answer5 = input("Your answer: ").upper()

if answer5 == "C":
    print("Correct! 🎉")
    score += 1
else:
    print("Wrong ❌ The correct answer is C. Leaves")

# Display final score
print("\n🎯 Quiz Finished!")
print("Your final score is:", score, "out of 5")

# Performance message
if score == 5:
    print("Excellent! 🌟 You got a perfect score!")
elif score >= 3:
    print("Good job! 👍 Keep studying science!")
else:
    print("Keep practicing! 📘 You can do better next time!")