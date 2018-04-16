#EVEN OR Odd
#LOGIC- Even numbers = 0 when % by 2

number = int(input("Give me a number and I'll see if its even or odd!"))
mod = number % 2
if mod == 0:
    print(str(number)+" Is even!")
else:
    print(str(number)+" Is odd!")
