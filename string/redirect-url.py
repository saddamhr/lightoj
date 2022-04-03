# inputs = []

# with open('input.txt') as f:
#     inputs = f.readlines()

# test_case = int(inputs[0])


test_case = int(input())

count = 1
for i in range(0, test_case):
    # for input in inputs[1:]:
    # print(input)
    url = input()
    # url = input
    if(url[4] != 's'):
        url = url[:4] + 's' + url[4:]
    # print(f'line {count}: {line}')    
    print(f'Case {count}: {url}')
    count += 1
