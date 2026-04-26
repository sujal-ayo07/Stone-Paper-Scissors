import random
import time

choices = ["stone", "paper", "scissors"]

emojis = {"stone": "🪨","paper": "📄","scissors": "✂️"}


#Formatting
print("\n"+"~"*90)
print("\n                                   Stone Paper Scissors \n")
print("~"*90)
print()


while True:
    user_score = 0
    comp_score = 0

    rounds = 5
    i = 1

    while i <= rounds:

        #formatting again hehehehe
        print("\n"+"-"*90)
        print(f"                                       🔹 Round {i}")
        print("-"*90 +"\n")

        user_ch = input("Enter stone / paper / scissors: ").lower()

        if user_ch not in choices:
            print("❌ Invalid input, try again")
            continue

        comp = random.choice(choices)

        print("\n⏳ Processing..", end="")
        time.sleep(0.7)
        print(".", end="",flush=True)
        time.sleep(0.7)
        print(".", end="",flush=True)
        time.sleep(0.7)
        print(".",flush=True)
        time.sleep(0.7)

        print(f"\n🧑 You: {user_ch} {emojis[user_ch]}")
        time.sleep(0.1)
        print(f"💻 Computer: {comp} {emojis[comp]}",flush=True)
        time.sleep(0.1)


        if user_ch == comp:
            print("\n🤝 Ohoo it's a Draw!")
            time.sleep(0.1)
            print("\n📊 You: 0 | Computer: 0 ")

        elif ((user_ch == "stone" and comp == "scissors") or
             (user_ch == "paper" and comp == "stone") or
             (user_ch == "scissors" and comp == "paper")):
            print("\n✅ Yuhuuuuu YOU WIN")
            user_score += 1
            time.sleep(0.1)
            print("\n📊 You: +1 | Computer: 0 ")

        else:
            print("\n❌ hehehe COMPUTER WINS")
            comp_score += 1
            time.sleep(0.1)
            print("\n📊 You: 0  | Computer: +1 ")

        

        i += 1

    time.sleep(0.1)

    print("\n"+'.'*90)
    print("                                     🎊 Final Result ")
    print('.'*90)

    time.sleep(0.9)
    a="So are you ready for the final result....?"
    for i in a:
        print(i,end="",flush=True)
        time.sleep(0.05)
    
    b="\nAnnouncing in ..."
    for j in b:
        print(j,end="",flush=True)
        time.sleep(0.1)

    c="\n321"
    for k in c:
        print(k,flush=True)
        time.sleep(1)


    if user_score > comp_score:
        print("\n🎉 You won the game!")
    elif comp_score > user_score:
        print("\n💻 Computer won the game!")
    else:
        print("\n🤝 It's a draw!")

    time.sleep(0.1)
    print(f"\n🎯 You: {user_score} | Computer: {comp_score}")

    time.sleep(0.1)
    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        time.sleep(0.1)
        print("\n👋 Thanks for playing!\n")
        break