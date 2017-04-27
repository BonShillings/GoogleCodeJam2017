import sys
arg_list = sys.argv
input_file_1 = open(arg_list[1])
input_file_2 = open(arg_list[2])
all_match = True
failed_test = 1
for j in range(1,101):
    line_1 = input_file_1.readline()
    line_2 = input_file_2.readline()
    if line_1 != line_2:
        all_match = False
        failed_test = j
        break;

if all_match:
    print("ALL MATCHED")
else:
    print("{} failed".format(failed_test))
