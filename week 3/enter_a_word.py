print("Please enter a word")
user_word = input()
for position in range(0,len(user_word) , 1 ):
    print(f" character {user_word[position]} available at position {position} ")