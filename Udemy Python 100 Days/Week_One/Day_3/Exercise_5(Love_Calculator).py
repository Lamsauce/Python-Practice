# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

score_1 = 0
score_2 = 0

for letter in name1:
  if letter == "T":
    score_1 += 1
  elif letter == "R":
    score_1 += 1
  elif letter == "U":
    score_1 += 1
  elif letter == "E":
    score_1 += 1

for letter in name2:
  if letter == "L":
    score_2 += 1
  elif letter == "O":
    score_2 += 1
  elif letter == "V":
    score_2 += 1
  elif letter == "E":
    score_2 += 1

score_1 = str(score_1)
score_2 = str(score_2)

final_score = score_1 + score_2

print(f"Your score is: {final_score}")