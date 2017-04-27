import sys
import math
import timeit
import math

arg_list = sys.argv
input_file = open(arg_list[1])
output = open(arg_list[2], 'w')

def process_packages(num_ingredients,recipe,packages):
    k_map = {}
    # key is str(j) + '-' + str(k_c)
    for package in packages:
        p_j = 0
        r_j = 1
        for j in range(0,num_ingredients):
            if package[j]!= 0:
                p_j = package[j]
                r_j = recipe[j]
                break
        k = float(p_j) / r_j

        # check ceil

        k_c = math.ceil(k)
        key = str(j) + '-' + str(k_c)
        if k < 1.10 * k_c and k > 0.9 * k_c:
            if k_map.has_key(key):
                k_map[key]


        # check floor
        if k < 1.10 * k_c and k > 0.9 * k_c:










def b(num_ingredients,recipe,packages):



    return 0

j = 0
for line in input_file:
    if j ==0:
        num_cases = line
        j = j+1
    else:
        input_num = line.replace('\n', '')
        print("input: " + str(j) + ":" + input_num)
        print("Case #{}: {}".format(j, b(input_num)))
        output.write("Case #{}: {}\n".format(j, b(input_num)))
        j = j + 1