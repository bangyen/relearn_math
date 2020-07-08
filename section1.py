def dec2bin_ex(target): #2進数変換
    #targetを整数部と小数部に分ける
    i = int(target) #整数部
    f = target - i #小数部

    #整数部を2進数に変換
    a = []  #あまりを入れるリスト

    # 割り算の商が0になるまで
    while i != 0:
        a.append(i % 2) #余り
        i = i // 2 #商
    #要素を逆順に
    a.reverse()

    #小数部を2進数に変換
    b = [] #整数部を入れるリスト
    n = 0  #繰り返した回数

    # 2をかけた後の小数部が0になるまで
    while (f != 0):
        temp = f * 2 #小数部×2
        b.append(int(temp)) #整数部
        f = temp - int(temp) #小数部 
        n += 1
        if (n >= 10):
            break

    return a,b

def dec2hex(target):
    amari = []

    while target != 0:
        amari.append(target % 16)
        target = target // 16

    for i in range(len(amari)):
        if 9 < amari[i] < 16:
            amari[i] = chr(55 + amari[i])

    amari.reverse()
    return amari

def any2dec(target, m):

    n = len(target) -1
    sum = 0

    for i in range(len(target)):
        letters = 'ABCDEF'
        if target[i] in letters:
            num = letters.index(target[i]) + 10
        else:
            num = int(target[i])

        sum += (m ** n)*num
        n -= 1 #参照のケタを減らして次のループに入る
    return sum
