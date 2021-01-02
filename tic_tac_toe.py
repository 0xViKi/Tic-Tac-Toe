import os

s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0
player = 0


def draw():
    print("\n")
    print('''
▀▀█▀▀ ▀█▀ ▒█▀▀█   ▀▀█▀▀ ░█▀▀█ ▒█▀▀█   ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀▀ 
 ▒█░░ ▒█░ ▒█░░░   ░▒█░░ ▒█▄▄█ ▒█░░░   ░▒█░░ ▒█░░▒█ ▒█▀▀▀ 
 ▒█░░ ▄█▄ ▒█▄▄█   ░▒█░░ ▒█░▒█ ▒█▄▄█   ░▒█░░ ▒█▄▄▄█ ▒█▄▄▄
        ''')
    print("| Creator: ViKi-R | Website: https://viki-r.github.io/ | \n")
    print(" +-----+-----+-----+")
    print(" | ", s[0], " | ", s[1], " | ", s[2], " | ")
    print(" +-----+-----+-----+")
    print(" | ", s[3], " | ", s[4], " | ", s[5], " | ")
    print(" +-----+-----+-----+")
    print(" | ", s[6], " | ", s[7], " | ", s[8], " | ")
    print(" +-----+-----+-----+")


def toggle_player(p1, p2):
    global player
    if player == p1:
        player = p2
    else:
        player = p1


def field():
    num_field = int(input(f"{player} Turn [0-9]: "))
    global count
    count += 1
    if num_field == 1:
        s[0] = player
    elif num_field == 2:
        s[1] = player
    elif num_field == 3:
        s[2] = player
    elif num_field == 4:
        s[3] = player
    elif num_field == 5:
        s[4] = player
    elif num_field == 6:
        s[5] = player
    elif num_field == 7:
        s[6] = player
    elif num_field == 8:
        s[7] = player
    elif num_field == 9:
        s[8] = player


def check():
    global player
    if s[0] == s[1] and s[1] == s[2]:
        return player
    if s[3] == s[4] and s[4] == s[5]:
        return player
    if s[6] == s[7] and s[7] == s[8]:
        return player
    if s[0] == s[3] and s[3] == s[6]:
        return player
    if s[1] == s[4] and s[4] == s[7]:
        return player
    if s[2] == s[5] and s[5] == s[8]:
        return player
    if s[0] == s[4] and s[4] == s[8]:
        return player
    if s[2] == s[4] and s[4] == s[6]:
        return player
    if count == 9:
        return 'd'
    return '/'


def winner(d, p1, p2):
    if d == p1:
        print(f"\n{p1} Wins!! ()==|:::::::::::> Game Over\n")
        return 1
    if d == p2:
        print(f"\n{p2} Wins!! ()==|:::::::::::> Game Over\n")
        return 1
    if d == 'd':
        print("\nDraw!! ()==|:::::::::::> Game Over\n")
        return 1


def clear():
    os.system('cls')


def play_again():
    print("Do you want to play again:")
    print("Y) Yes\nN) No")
    choice = input("Choose: ")
    if choice == 'Y' or choice == 'y':
        for i in s:
            s[i] = k[i]
        main()
    elif choice == 'N' or choice == 'n':
        clear()
        os.system("exit")


def main():
    x = 0
    clear()
    draw()
    player_one = input("Enter Player One's character: ").upper()[:1]
    player_two = input("Enter Player Two's character: ").upper()[:1]
    while x != 1:
        clear()
        draw()
        toggle_player(player_one, player_two)
        field()
        who_won = check()
        clear()
        draw()
        x = winner(who_won, player_one, player_two)

    if x == 1:
        play_again()


if __name__ == "__main__":
    main()
