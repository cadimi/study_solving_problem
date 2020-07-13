# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=574&sca=2010

while True:
    inputValue = input()
    x = int(inputValue.split(" ")[0])
    y = int(inputValue.split(" ")[1])
    if 1 <= x <= 9 and 1 <= y <= 9:
        break
    else:
        print("INPUT ERROR!")

for num in range(1, 10):
    print(f"{x} * {num} =  {x * num}   {y} * {num} =  {y * num}   ")
