'''
████████ ██  ██████     ████████  █████   ██████     ████████  ██████  ███████
   ██    ██ ██             ██    ██   ██ ██             ██    ██    ██ ██
   ██    ██ ██             ██    ███████ ██             ██    ██    ██ █████
   ██    ██ ██             ██    ██   ██ ██             ██    ██    ██ ██
   ██    ██  ██████        ██    ██   ██  ██████        ██     ██████  ███████
'''
import os

s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0
player = 'ESC'


def draw():
    print("\n")
    print('''
        ######## ##  ######     ########  #####   ######     ########  ######  #######
           ##    ## ##             ##    ##   ## ##             ##    ##    ## ##
           ##    ## ##             ##    ####### ##             ##    ##    ## #######
           ##    ## ##             ##    ##   ## ##             ##    ##    ## ##
           ##    ##  ######        ##    ##   ##  ######        ##     ######  #######
        ''')
    print("\033[10;36HCreator: D4RK C0D3R \n")
    print("\033[12;40H" + str(s[0]) + " | " + str(s[1]) + " | " + str(s[2]))
    print("\033[13;39H" + "---+---+---")
    print("\033[16;40H" + str(s[3]) + " | " + str(s[4]) + " | " + str(s[5]))
    print("\033[18;39H" + "---+---+---")
    print("\033[20;40H" + str(s[6]) + " | " + str(s[7]) + " | " + str(s[8]))
    print('\n')


def TogglePlayer(p1, p2):
    global player
    if(player == p1):
        player = p2
    else:
        player = p1


def field():
    a = int(input("Choose the Number " + player + ": "))
    global count
    count += 1
    if(a == 1):
        s[0] = player
    elif(a == 2):
        s[1] = player
    elif(a == 3):
        s[2] = player
    elif(a == 4):
        s[3] = player
    elif(a == 5):
        s[4] = player
    elif(a == 6):
        s[5] = player
    elif(a == 7):
        s[6] = player
    elif(a == 8):
        s[7] = player
    elif(a == 9):
        s[8] = player


def check():
    global player
    if (s[0] == s[1] and s[1] == s[2]):
        return player
    if (s[3] == s[4] and s[4] == s[5]):
        return player
    if (s[6] == s[7] and s[7] == s[8]):
        return player
    if (s[0] == s[3] and s[3] == s[6]):
        return player
    if (s[1] == s[4] and s[4] == s[7]):
        return player
    if (s[2] == s[5] and s[5] == s[8]):
        return player
    if (s[0] == s[4] and s[4] == s[8]):
        return player
    if (s[2] == s[4] and s[4] == s[6]):
        return player
    if(count == 9):
        return 'd'
    return '/'


def winner(d):
    global a, b
    if(d == a):
        print(a + " Wins!! ()==|:::::::::::> Game Over\n")
        return 1
    if(d == b):
        print(b + " Wins!! ()==|:::::::::::> Game Over\n")
        return 1
    if(d == 'd'):
        print("Draw!! ()==|:::::::::::> Game Over\n")
        return 1


def clear():
    os.system('cls')


def playagain():
    print("Do you want to play again:")
    print("Y) Yes\nN) No")
    choice = input("Choose: ")
    if(choice == 'Y' or choice == 'y' or choice == '1'):
        for i in s:
            s[i] = k[i]
        main()
    if(choice == 'N' or choice == 'n' or choice == '2'):
        clear()
        os.system("exit")


def main():
    global a, b, count
    x = 0
    clear()
    draw()
    a = input("Enter Player One's character: ")
    b = input("Enter Player Two's character: ")
    while(x != 1):
        clear()
        draw()
        TogglePlayer(a, b)
        field()
        c = check()
        clear()
        draw()
        x = winner(c)

    if(x == 1):
        playagain()


if __name__ == "__main__":
    main()
