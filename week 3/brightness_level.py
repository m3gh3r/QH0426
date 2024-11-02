print("What level of brightness is required?")
brightness_level = int(input())

for brightness in range ( 0 , brightness_level , 2 ):
    print(f"brightness level is :{"*" * brightness} ")

