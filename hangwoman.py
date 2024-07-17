def hangwoman():
    
    wrong = 0
    stages = [
        "",
        "_______       ",
        "|             ",
        "|       |     ",
        "|       0\    ",
        "|      /|\    ",
        "|      / \    ",
        "|             ",
    ]
    
    word = input('Set your answer:').lower()
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print('Welcome to Hangwoman!')
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter:"
        char = input(msg).lower()
        
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "@"
        else:
            wrong += 1
            
        print(" ".join(board))
        print("\n".join(stages[:wrong+1]))
        
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
        
    if not win:
        print("\n".join(stages[:wrong+1]))
        print("You lose! It was {}.".format(word))
        
if __name__ == '__main__':
    hangwoman()    