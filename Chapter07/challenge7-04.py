number = [2, 4, 5, 9, 0]
while True:
    a = input("数字を入力してください（'q'で終了）")
    if a == "q":
        break
    try:
        num = int(a)
    except ValueError:
        print("数字か'q'を入力してください")
    
    if num in number:
        print("正解")
    else:
        print("不正解")
    
