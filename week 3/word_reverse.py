print("What phrase do you want to see in reverse?")
user_word = input()

print("Reversing")
print("The reverse word is: " , end="")

for position in range(len(user_word)-1, -1 , -1):
    print(user_word[position], end ="")
         

print("\n Done!")