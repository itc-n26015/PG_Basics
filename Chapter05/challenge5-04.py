introduction = {}

introduction = {"1": "volleyball", "2": "bike"}

x = input("数字を入力してください:")
if x in introduction:
    introduction = introduction[x]
    print(introduction)
else:
    print("見つかりません。")

