

def is_valid(n):
    digits = [int(x) for x in str(n)]
    doubled = False
    for i in range(1,len(digits)):
        if digits[i] == digits[i-1]: doubled = True
        if digits[i] < digits[i-1]: return False
    return doubled

def is_valid2(n):
    digits = [int(x) for x in str(n)]
    doubled = {x: None for x in range(10)} #dirty solution but it works
    for i in range(1,len(digits)):
        if digits[i] == digits[i-1]:
            if doubled[digits[i]] is True:
                doubled[digits[i]] = False
            if doubled[digits[i]] is None:
                doubled[digits[i]] = True

        if digits[i] < digits[i-1]: return False
    return sum([x for x in doubled.values() if x])>0

result = []

for n in range(128392,643281+1):
    result.append(is_valid2(n))
print(sum(result))

