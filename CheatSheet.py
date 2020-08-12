def solution(n):
  for index in range(1,int(n)+1):
      output = []
      if index%2 == 0:
        output.append('Codility')
      if index%3 == 0:
        output.append('Test')
      if index%5==0:
        output.append('Coders')

      if len(output) > 0:
        print(''.join(map(str,output)))
      else:
        print(str(index))

try:
  n= int(input())
  solution(n)
except EOFError:
  pass




def solution(s):
  tel_num = []

  for only_num in s:
    if only_num == '-' or only_num == ' ':
      continue
    tel_num.append(only_num)

  block_count = 0

  stop = 3*((len(tel_num)//3)-1)

  ans = []
        
  for index in range(stop):
    ans.append(tel_num[index])
    block_count += 1
    if block_count%3 == 0:
      ans.append('-')

  block_count = 0

  for i in range(stop,len(tel_num)):
    ans.append(tel_num[i])
    block_count += 1
    if block_count == 2 and len(tel_num)%3 == 1:
        ans.append('-')
    if block_count == 3 and len(tel_num)%3 == 2:
        ans.append('-')
            
  print(''.join(map(str,ans)))

try:
  s=input()
  solution(s)
except EOFError:
  pass
