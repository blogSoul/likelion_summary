from django.shortcuts import render
# Create your views here.
def wordcount(request):
    return render(request,'wordcount.html')

def count(request):
    return render(request, 'count.html')

def calculation(request):
    full = request.GET['fulltext']
    number = request.GET['text']
    number = int(number)

    def CaesarCipher(text, key, enc=True):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        enc_rule = {}
        for i in range(len(alphabet)):
            enc_rule[alphabet[i]] = alphabet[(i + key) % len(alphabet)]
        dec_rule = dict([(j, i) for (i, j) in enc_rule.items()])

        if enc == True:
            rule = enc_rule
        else:
            rule = dec_rule

        res = ""
        list = []
        for x in text.lower():
            if x in alphabet:
                res += rule[x]
            else:
                res += x
        return res
    # 이 함수는 (원하는 문장, 얼마나 이동 시킬 것인지, True면 앞으로 False면 뒤로 이동한다.)이다.
    if number >=0:
        remeber = CaesarCipher(full, number, enc=True)
    else:
        number = (-1)*number
        remeber = CaesarCipher(full, number, enc=False)

    def countAlphabet(text):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
        # ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        rule = {}
        for i in range(len(alphabet)):
            rule[alphabet[i]] = alphabet[(i) % len(alphabet)]
        res = ""
        countlist = {}
        for x in text.lower():
            if x in alphabet:
                countlist[x] = text.count(x)
        ordered_tmp = list(countlist.items())
        ordered_tmp.sort(key=lambda x: x[1], reverse=True)
        return ordered_tmp
    # 이 함수는 텍스트 안에 알파벳이 얼마나 들어 있는지 확인할 수 있는 함수 입니다.
    countAlphabet = countAlphabet(full)
    countAlphabet = dict(countAlphabet)
    return render(request, 'calculation.html', {'fulltext': full, 'remeber': remeber, 'countAlphabet': countAlphabet.items()})