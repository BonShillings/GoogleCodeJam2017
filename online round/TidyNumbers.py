import sys

def findTidy(input_num):

    if is_tidy(input_num):
        return input_num

    return ''.join(makeTidy(list(input_num)))

def subtractTidy(num):
    num_i = int(num) -1
    if num_i <0:
        return '9'
    return str(num_i)

def is_tidy(num_str):
    if len(num_str) == 1:
        return True;

    for c in reversed(range(1,len(num_str))):
        if num_str[c] < num_str[c-1]:
            return False
    return True

def makeTidy(num_str):
    if is_tidy(num_str):
        return num_str
    for i in reversed(range(1,len(num_str))):
        #print("index: " + str(i))
        #print num_str[i]
        #print num_str[i-1]
        if num_str[i] < num_str[i-1]:
            nine_replace = ['9'] * (len(num_str) - i)
            num_str = num_str[:i] + nine_replace
            #num_str[i] = '9'
            num_str[i-1]= subtractTidy(num_str[i-1])

        #print num_str

    if num_str[0] == '0':
        return num_str[1:len(num_str)]
    return num_str



arg_list = sys.argv
input_file = open(arg_list[1])
output = open(arg_list[2], 'w')

j = 0
for line in input_file:
    if j ==0:
        num_cases = line
        j = j+1
    else:
        input_num = line.replace('\n', '')
        print("input: " + str(j) + ":" + input_num)
        print("Case #{}: {}".format(j, findTidy(input_num)))
        output.write("Case #{}: {}\n".format(j, findTidy(input_num)))
        j = j + 1







