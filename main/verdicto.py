# !! Only use Verdicto if you are a horrible decision maker !!
import random

def decision_maker():
    problem = input("Please input what your problem is: ")
    decisions = []
    decision_num = 1
    while True:
        decision = input(f"Decision {decision_num}: ")
        decisions.append(decision)
        decision_num += 1
        if decision_num > 2:
            print("Is that it? (y/n)")
            while True:
                cmd_decs = input("> ").lower()
                if cmd_decs == 'n':
                    break
                elif cmd_decs == 'y':
                    pass
                else:
                    print("Please input either 'y' or 'n'")
                    continue
                fin_decision = random.choice(decisions)
                input("Press Enter to see your final decision. ")
                print(f"Your problem is {problem} and your decision is {fin_decision}")
                return None

def dice():
    print("Input how many number on your dice")
    while True:
        try:
            cmd_dicenum = int(input("> "))
            dice = range(cmd_dicenum)
        except ValueError:
            print("Please input a numeric value.")
            continue
        break
    print(f"The number you got is {random.choice(dice)}.")
    
def meight_ball():
    question = input("Please input your question: ")
    p_answer = ("Yes.", "No.", "Absolutely.", "Never.", "Maybe.", "Probably not.", "Most likely."
                , "My Advice: Don't.", "Yes, totally yes.", 'If I were you, I would stay away from it.', 'Very doubtful.',
                "You may rely on it.")
    print(random.choice(p_answer))
        

def end(cmd):
    cmd = cmd.lower()
    if cmd == 'n':
        return True
    elif cmd == 'y':
        return False
    else:
        return 'Nope'


if __name__ == '__main__':
    print("Welcome to Verdicto, your totally (un)reliable decision maker!")
    while True:
        print(
            f"Input a command bellow. \n(1) Decision Maker \n(2) Dice"
            f"\n(3) Magic 8-Ball \n(4) Quit"
        )
        cmd_main = input("> ")
        if cmd_main == '1':
            while True:
                decision_maker()
                print("Are there any more decision-making to do? (y/n)")
                end_dm = end(input("> "))
                if end_dm:
                    print("="*120)
                    break
                elif not end_dm:
                    pass
                else:
                    break
        
        elif cmd_main == '2':
            while True:
                dice()
                print("Are there any more dice-ing to do? (y/n)")
                end_dm = end(input("> "))
                if end_dm:
                    print("="*120)
                    break
                elif not end_dm:
                    pass
                else:
                    break
                
        elif cmd_main == '3':
            while True:
                meight_ball()
                print("Are there any more 8-balling to do? (y/n)")
                end_dm = end(input("> "))
                if end_dm:
                    print("="*120)
                    break
                elif not end_dm:
                    pass
                else:
                    break
        
        elif cmd_main == '4':
            break
        
        else:
            print("Please enter a valid command.")
