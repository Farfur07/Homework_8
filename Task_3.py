x = input()

res = {}

for item in x:
    if res.get(item):
        res[item] += 1
    else:
        res[item] = 1

print(res)
# thing how to do with "count" function

y = input()
substring = 'a'
print(y.count(substring[0:]))

