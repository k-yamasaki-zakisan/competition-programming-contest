from collections import deque

def main():
    s = deque(input())
    ans = 0
    #文字列を一定条件で全てpopできれば回分になる
    while s:
        top = s[0]
        tail = s[-1]
        if top != tail:
            if top != 'x' and tail != 'x':
                print(-1)
                exit()
            else:
                if top == 'x':
                    s.popleft()
                elif tail == 'x':
                    s.pop()
                ans += 1
        else:
            s.popleft()
            if s:
                s.pop()
    print(ans)

if __name__ == "__main__":
    main()