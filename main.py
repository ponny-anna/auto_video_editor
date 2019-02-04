from crawler import crawel

def main():
    while True:
        print('[0]: 画像クローリング [1]: 顔抽出 [2]: 自動動画編集')
        input_process = input('>> ')
        if input_process.isdecimal() == True:
            input_process = int(input_process)
        else:
            print("数値を入力してください。")
            continue

        if input_process == 0:
            crawel()
        elif input_process == 1:
            print("顔検出")
        elif input_process == 2:
            print("自動動画編集")
        else:
            print(f'{input_process}は不正な値です。')
        
        print('終了しますか? [0]: No / [1]: Yes')
        end_flg = input('>> ')

        if end_flg.isdecimal() == True and int(end_flg) == 1:
            break

if __name__== '__main__':
    main()