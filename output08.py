# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=145&sca=10
#       item     count     price
#        pen        20       100
#       note         5        95
#     eraser       110        97


displayTuple = [
    "item", "count", "price",
    "pen", "20", "100",
    "note", "5", "95",
    "eraser", "110", "97",
]

for idx, val in enumerate(displayTuple):
    if idx % 3 == 2:
        print(val.rjust(10, " "), end="\n")
    else:
        print(val.rjust(10, " "), end="")
