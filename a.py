import sys
import math
import timeit

def a(num_row,num_col,input_mat):
    rows_to_replace = []
    replace_row = input_mat[0]
    for i in range(0,num_row):
        found = False
        ind_to_replace = []
        row = input_mat[i]
        replace_char = '?'
        if row == ['?' for k in range(0,num_col)]:
            rows_to_replace.append(i)
            if i == num_row -1:
                for rows in rows_to_replace:
                    input_mat[rows] = replace_row

        else:
            for j in range(0,num_col):
                if not found:
                    if row[j] == '?':
                        ind_to_replace.append(j)
                    else:
                        replace_char = row[j]
                        for ind in ind_to_replace:
                            row[ind] = replace_char
                        found = True
                else:
                    if row[j] == '?':
                        input_mat[i][j] = replace_char

                    if row[j] != '?':
                        replace_char = row[j]
            replace_row = input_mat[i]
            for rows in rows_to_replace:
                input_mat[rows] = replace_row
            rows_to_replace = []


    return input_mat


arg_list = sys.argv
input_file = open(arg_list[1])
output = open(arg_list[2], 'w')

j = 0
current_row = 0
input_mat = []
is_input_start = True
for line in input_file:
    if j ==0:
        num_cases = line
        j = j+1
    else:
        if is_input_start:
            print("\n")
            num_row, num_col = line.replace('\n', '').split(" ")
            print(num_row)
            print(num_col)
            current_row = 0
            is_input_start = False
        else:
            if current_row < num_row:
                #read line to mat
                input_mat += [list(line.replace('\n', ''))]
                print current_row
                print(input_mat)
                current_row += 1

            if current_row == int(num_row):
                print("input: " + str(j) + ":" + str(input_mat))
                output_mat = a(int(num_row),int(num_col),input_mat)
                print("Case #{}:".format(j))
                output.write("Case #{}:\n".format(j))
                for entry in range(0,len(output_mat)):
                    print "{}".format("".join(output_mat[entry]))
                    output.write("{}\n".format("".join(output_mat[entry])))
                j = j + 1
                is_input_start = True
                input_mat = []
