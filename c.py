import sys
import math
import timeit



def c(input_nums):
    h_d = float(input_nums[0])
    a_d = float(input_nums[1])
    h_k = float(input_nums[2])
    a_k = float(input_nums[3])
    b = float(input_nums[4])
    d = float(input_nums[5])


    # lol forgot about debuff
    #edge cases
    turns = 0

    if a_d > h_k:
        return 1

    if a_k >= h_d:
        return 'IMPOSSIBLE'

    attacks_to_kill = math.ceil( float(a_d)/ h_k)

    turns_to_die = math.ceil(float(a_k) / h_d)

    print turns_to_die
    if b > a_k:
        print("here")
        #buffer strat
        left_side = 2 *float((h_k - float(a_d)))/b
        #start at sqrt
        start = math.sqrt(left_side)
        found = False
        check = start
        while not found:
            if b * check * (check+1)/2 + a_d >= h_k:
                attacks_to_kill = check
                found = True
            else:
                check += 1


    # check k * (n*b +a)
    #check_end = attacks_to_kill
    #for k in range(1,check_end):
    #    if k *( check_end*b + a_d) < attacks_to_kill


    if b * attacks_to_kill * (attacks_to_kill - 1)/2  + a_d > a_d * attacks_to_kill:
        # find min over b
        print("here2")
        check = attacks_to_kill
        while not found:
            if b * check * (check+1)/2 + a_d >= h_k:
                attacks_to_kill = check
                found = True
            else:
                check += 1




    if attacks_to_kill > turns_to_die:
        return attacks_to_kill
    else:
        print("here3")
        dead = False
        session = turns_to_die - 1
        print session
        # handle turns_to_die after first cure
        while not dead:
            if h_k - a_d * session < 0:
                # iterate over last turns
                for i in range(0,session):
                    turns += 1
                    h_k = h_k - a_d
                    if h_k <=0:
                        return turns

            if h_k - a_d * session == 0:
                return turns + session

            h_k = h_k - a_d * session
            turns += session
            # heal
            turns += 1
            #print turns


    return 'IMPOSSIBLE'

arg_list = sys.argv
input_file = open(arg_list[1])
output = open(arg_list[2], 'w')

j = 0
for line in input_file:
    if j ==0:
        num_cases = line
        j = j+1
    else:
        input_nums = line.replace('\n', '').split(' ')
        print("input: " + str(j) + ":" + str(input_nums))
        out = c(input_nums)
        print("Case #{}: {}".format(j, out))
        output.write("Case #{}: {}\n".format(j, out))
        j = j + 1