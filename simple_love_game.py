print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Covnert the names to all lower case
name1 = name1.lower()
name2 = name2.lower()
#adding the names together
combined_names = name1 + name2
#Variables for the game 
t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e = combined_names.count('e')
true = t + r + u + e
l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')
e = combined_names.count('e')
love = l + o + v + e
final_score = int(str(true) + str(love))
# Code that is going to make the game run
if (final_score < 10) or (final_score > 90):
    print(f"Your score is {final_score}, you go together like coke and mentos")
elif (final_score >= 40) and final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")
