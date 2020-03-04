options = []
right = ""
middle = ""
n, m = map(int, input().split())

for _ in range(n):
    x = input()
    y = x[::-1]
    if y in options:
        right += x
    if x == y:
        middle = x
    options.append(x)
palindrome = right + middle + right[::-1]

print(len(palindrome))
print(palindrome)
