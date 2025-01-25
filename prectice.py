questions = [
  ["Which one is a frout", "Read", "Corn", "Papaya", "None", 4],
  ["Which one is a Vagitable", "Dhaka", "Rangpur", "Papaya", "None", 4],
  ["Which one is a City", "Dhaka", "Bangladesh", "Dhili", "Turky", 2],
  ["Which one is a Animul", "Bus", "Apple", "Dog", "Street", 4],
  ["Who is the derector of interstellar movie", "christopher nolan", "American film     director", "James Cameron", "David Fincher", 2],  
  ["Who is fascist of bangladesh", "Hasina", "Khalida", "Ziaur Rahman", "None", 2],
]

levels = [1000, 2000, 4000, 8000, 16000, 32000]
money = 0
for i in range(0, len(questions)):
  questions = questions[i]
  print(f"Question for MPR. {levels[i]}")
  print(f"a. {questions[i][1]}          b. {questions[i][2]}")
  print(f"c. {questions[i][3]}          d. {questions[i][4]}")
  reply = int(input("Enter your Ans (1-4) "))
  if(reply == question[-1]):
    print(f"Correct answer, you have won MRR. {levels[i]}")
    if (i == 1):
      money = 1000
    elif (i == 2):
      money = 2000
    elif (i == 3):
      money = 4000
    elif (i == 4):
      money = 8000
    elif (i == 5):
      money = 16000
    elif (i == 6):
      money = 32000  
  else:
    print("Worng answer!")
    break   

print(f"your take home money is {money}")