# This is a quiz application program.

print("--Neet quiz--")
print("This quiz contains 10 questions 1 marks each, attempt all.")
score = 0

print(""""Q1. Which is the powerhouse of the cell?
    1. Nucleus
    2. Mitochondria
    3. Ribosome
    4. Golgi apparatus""")
ans = int(input("Ans: "))
if(ans==2):
    print("Correct answer.")
    score+=1
else:
    print("Wrong answer! Correct answer is 2")
print("""Q2. The SI unit of force is:
    1. Joule
    2. Newton
    3. Watt
    4. Pascal""")
ans = int(input("Ans: "))
if(ans==2):
    print("Correct answer.")
    score+=1
else:
    print("Wrong answer! Correct answer is 2")
print("""Q3. Which blood group is known as the universal donor?
    1. A
    2. B
    3. AB
    4. O Negative""")
ans = int(input("Ans: "))
if(ans==4):
    print("Correct answer.")
    score+=1
else:
    print("Wrong answer! Correct answer is 4")
print("""Q4. The functional unit of the kidney is:
    1. Alveolus
    2. Nephron
    3. Neuron
    4. Glomerulus""")
ans = int(input("Ans: "))
if(ans==2):
    print("Correct answer.")
    score+=1
else:
    print("Wrong answer! Correct answer is 2")
print("""Q5. Which of the following hormones decreases blood glucose levels?
    1. Glucagon
    2. Adrenaline
    3. Insulin
    4. Thyroxine""")
ans = int(input("Ans: "))
if(ans==3):
    print("Correct answer.")
    score+=1
else:
    print("Wrong answer! Correct answer is 3")
print("""Q6. Which of the following cell organelles contains its own DNA?
    1. Ribosome
    2. Lysosome
    3. Mitochondria
    4. Golgi apparatus""")
ans = int(input("Ans: "))
if(ans==3):
    print("Correct answer.")
    score+=1
else:
    print("Wrong answer! Correct answer is 3")
print("""Q7. Which of the following is not a vector-borne disease?
    1. Malaria
    2. Dengue
    3. Tuberculosis
    4.Chikungunya""")
ans = int(input("Ans: "))
if(ans==3):
    print("Correct answer.")
    score+=1
else:
    print("Wrong answer! Correct answer is 3")
print("""Q8. Which gas is liberated when zinc reacts with dilute hydrochloric acid?
    1. Oxygen
    2. Hydrogen
    3. Chlorine
    4. Carbon dioxide""")
ans = int(input("Ans: "))
if(ans==2):
    print("Correct answer.")
    score+=1
else:
    print("Wrong answer! Correct answer is 2")
print("""Q9. The pH of pure water at 25°C is:
    1. 5
    2. 6
    3. 7
    4. 8""")
ans = int(input("Ans: "))
if(ans==3):
    print("Correct answer.")
    score+=1
else:
    print("Wrong answer! Correct answer is 3")
print("""Q10. Which of the following is an example of a homologous organ?
    1. Wings of butterfly and bird
    2. Flippers of whale and wings of bat
    3. Eyes of octopus and humans
    4. Gills of fish and lungs of humans""")
ans = int(input("Ans: "))
if(ans==2):
    print("Correct answer.")
    score+=1
else:
    print("Wrong answer! Correct answer is 2")
print("You have completed the quiz.")
if(score==10):
    print(" Outstanding, You have scored 10/10.")
elif(score>=8):
    print(f"Congrats! Your score is {score}/10.")
elif(score>=5):
    print(f"Your score is {score}/10, Keep it up!")
else:
    print(f"Your score is {score}/10")
    print("You have failed the quiz , Better luck next time")

print("THANK YOU FOR ATTEMPTING THE QUIZ !")