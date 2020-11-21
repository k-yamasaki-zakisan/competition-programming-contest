# https://atcoder.jp/contests/arc011/tasks/arc011_2

translater = {
    'b':'1',
    'c':'1',
    't':'3',
    'j':'3',
    'd':'2',
    'w':'2',
    'f':'4',
    'q':'4',
    'l':'5',
    'v':'5',
    's':'6',
    'x':'6',
    'p':'7',
    'm':'7',
    'h':'8',
    'k':'8',
    'n':'9',
    'g':'9',
    'z':'0',
    'r':'0'
}

N = int(input())
W = input()
W = W.lower()
ans = ''
breach = 0
for w in W:    
    if w in translater:
        if len(ans) and breach:
            ans += ' '
        breach = 0
        ans += translater[w]
    elif w == ' ':
        breach += 1
        
print(ans)