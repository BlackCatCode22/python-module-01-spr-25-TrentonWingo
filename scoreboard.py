#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
score =input("Enter Score: ")
s = float(score)
if s >=0.9:
    print("you got an A")
elif s >=0.8:
    print("you got an B")
elif s >=0.7:
    print("you got an C")
elif s >=0.6:
    print("you got an D")
elif s <0.6:
    print("you got an F")