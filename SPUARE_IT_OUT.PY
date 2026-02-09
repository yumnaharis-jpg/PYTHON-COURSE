start = int(Iinput("enter starting number:"))
end = int(input("enter ending number:"))
squares = []
even_squares = []
odd_squares = []
for number in range(start,end + 1):
    square = number * number
    squares.append(square)
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)










