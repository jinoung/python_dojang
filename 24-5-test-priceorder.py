s = list(map(int, input().split(';')))
s.sort(reverse=True)
for i in range(len(s)):
    print('%9s' % format(s[i], ','))
