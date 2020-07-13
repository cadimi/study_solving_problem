# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2076&sca=2010


while True:
    inputValue = input()
    if 1 <= int(inputValue.split(" ")[0]) <= 9 and 1 <= int(inputValue.split(" ")[1]) <= 9:
        break
    else:
        print("INPUT ERROR!")

for num in range(1, 10):
    print(f"{int(inputValue.split(' ')[0])} * {num} =  {int(inputValue.split(' ')[0]) * num}   ", end="")
    if num % 3 == 0: print("", end="\n")

print("")

for num in range(1, 10):
    print(f"{int(inputValue.split(' ')[1])} * {num} =  {int(inputValue.split(' ')[1]) * num}   ", end="")
    if num % 3 == 0: print("", end="\n")
