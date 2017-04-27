import sys
import math
import timeit
from operator import itemgetter, attrgetter, methodcaller

def left_distance(stalls,stall_index):
    distance = 0;
    for i in reversed(range(0,stall_index)):
        if stalls[i] == 1:
            return distance
        distance = distance +1
    return distance

def right_distance(stalls,stall_index):
    distance = 0;
    for i in range(stall_index+1,len(stalls)):
        if stalls[i] == 1:
            return distance
        distance = distance +1
    return distance

def find_d_for_last_occupant_iterative(stalls, num_occupants):
    max_d = 0
    min_d = math.floor(len(stalls) / 2)
    indices = [k for k in range(1,len(stalls)-1)]
    for i in range (0, num_occupants):
        # compute d
        max_d,min_d = find_best_stall(stalls,indices)
    return max_d,min_d

def find_best_stall(stalls,indices):
    # compute d
    closest = 0
    closest_max = 0
    index = indices[0]
    for j in indices:
        if stalls[j] != 1:
            right = right_distance(stalls, j)
            left = left_distance(stalls, j)
            # closest = min(left,right)
            if min(left, right) > closest:
                closest = min(left, right)
                closest_max = max(left, right)
                index = j
            if min(left, right) == closest:
                if max(left, right) > closest_max:
                    closest_max = max(left, right)
                    closest = min(left, right)
                    index = j

    stalls[index] = 1
    indices.remove(index)
    return closest_max,closest


def find_d_for_last_occupant_precompute(stalls, num_occupants):
    max_d = 0
    min_d = math.floor(len(stalls) / 2)
    indices = [k for k in range(1,len(stalls)-1)]
    while num_occupants > 0:
        # compute d
        # compute d
        best_stalls = []
        closest = 0
        closest_max = 0
        for j in indices:
            if stalls[j] != 1:
                right = right_distance(stalls, j)
                left = left_distance(stalls, j)
                # closest = min(left,right)
                if min(left, right) > closest:
                    closest = min(left, right)
                    closest_max = max(left, right)
                    index = j
                    best_stalls = best_stalls + [(j,min(left, right),max(left, right))]
                if min(left, right) == closest:
                    if max(left, right) > closest_max:
                        closest_max = max(left, right)
                        closest = min(left, right)
                        index = j
                        best_stalls = best_stalls + [(j,min(left, right),max(left, right))]


        #print closest
        # prune best_stall
        pruned_stalls = []
        for stall in best_stalls:
            if stall[1] == closest:
                pruned_stalls.append(stall)

        #print(pruned_stalls)

        if (num_occupants - len(pruned_stalls)) > 0:
            for stall in pruned_stalls:
                stall_index = stall[0]
                indices.remove(stall_index)
                stalls[stall_index] = 1
                num_occupants -= 1
        else:
            stalls[index] = 1
            indices.remove(index)
            return closest_max, closest
            num_occupants -= 1

    return max_d,min_d



# returns max(l_d,r_d), min(l_d,r_d)
def compute_distances(stalls):
    max_left_distance = 0
    min_left_distance = len(stalls)-1
    max_right_distance = 0
    min_right_distance = len(stalls) - 1
    for i in range(1,len(stalls)-1):
        left_d = left_distance(stalls,i)
        right_d = right_distance(stalls,i)
        if left_d > max_left_distance:
            max_left_distance = left_d
        if left_d < min_left_distance:
            min_left_distance = left_d
        if right_d > max_right_distance:
            max_right_distance = right_d
        if right_d > min_right_distance:
            min_right_distance = right_d

    #print (max(max_left_distance,max_right_distance), min(min_left_distance,min_right_distance))
    return max(max_left_distance,max_right_distance), min(min_left_distance,min_right_distance)


##
#
# Split Strategy
#
def find_d_for_last_occupant_split(stalls, num_occupants):
    max_d = 0
    min_d = math.floor(len(stalls) / 2)

    best_stall = int(math.ceil(len(stalls) / 2))
    left_occupants = math.ceil(num_occupants/2) - 1
    right_occupants = math.floor(num_occupants/2)
    stalls[best_stall] = 1

    closest_max_d,closest_min_d = find_best_stall_split(stalls[0:best_stall+1], left_occupants, min_d,max_d)
    right_max_d, right_min_d = find_best_stall_split(stalls[best_stall:len(stalls)], right_occupants, min_d,max_d)

    if right_min_d > closest_min_d:
        closest_min_d = right_min_d
        closest_max_d = right_max_d
    if right_min_d == closest_min_d:
        if right_max_d > closest_max_d:
            closest_min_d = right_min_d
            closest_max_d = right_max_d

    return int(closest_max_d), int(closest_min_d)

##
#
# Split Strategy
#
def find_best_stall_split(stalls, num_occupants, closest, closest_max):

    num_stalls = len(stalls)
    if num_stalls <= 3:
        return 0,0
    if num_stalls == 4:
        return 1,0

    if(num_occupants == 0):
        return closest_max,closest

    if(num_occupants == 1):
        best_stall = int(math.ceil(len(stalls) / 2))
        right = right_distance(stalls, best_stall)
        left = left_distance(stalls, best_stall)
        closest = min(left, right)
        closest_max = max(left, right)
        return closest_max,closest

    best_stall = int(math.ceil(len(stalls)/2))
    left_occupants = math.floor(num_occupants / 2)
    right_occupants = math.floor(num_occupants / 2)

    right = right_distance(stalls, best_stall)
    left = left_distance(stalls, best_stall)
    closest = min(left,right)
    closest_max = max(left,right)
    stalls[best_stall] = 1

    closest_max_d, closest_min_d = find_best_stall_split(stalls[0:best_stall + 1], left_occupants, closest, closest_max)
    right_max_d, right_min_d = find_best_stall_split(stalls[best_stall:len(stalls)], right_occupants, closest, closest_max)

    if right_min_d > closest_min_d:
        closest_min_d = right_min_d
        closest_max_d = right_max_d
    if right_min_d == closest_min_d:
        if right_max_d > closest_max_d:
            closest_min_d = right_min_d
            closest_max_d = right_max_d

    return closest_max_d, closest_min_d

def bathroom_stalls_log_logic(num_stalls,num_occupants):

    if num_stalls == 1:
        return 0,0
    if num_stalls == num_occupants:
        return 0,0
    if 2*num_occupants > num_stalls+2:
        return 0,0

    distance_min = num_stalls
    distance_max = num_stalls
    occupant_round = 0
    print num_stalls
    print num_occupants
    print distance_max
    print distance_min
    print "\n"
    while num_occupants > 0:
        distance_min = int(math.floor((num_stalls-1)/2))
        distance_max = int(math.ceil(num_stalls/2))
        num_stalls -= 1

        num_occupants = num_occupants - 2 ** occupant_round
        occupant_round += 1

        num_stalls = int(math.floor(num_stalls/ 2))
        print num_stalls
        print num_occupants
        print distance_max
        print distance_min
        print "\n"

    return distance_max,distance_min

def initialize_stalls(num_stalls):
    #print type(num_stalls)
    stalls = [0 for i in range(0,num_stalls+2)]
    stalls[0] = 1
    stalls [num_stalls+1] = 1
    return stalls

def bathroom_stalls(num_stalls, num_occupants):
    if num_stalls == num_occupants:
        return 0,0
    if 2*num_occupants > num_stalls:
        return 0,0
    stalls = initialize_stalls(num_stalls)
    #print(stalls)
    return find_d_for_last_occupant_precompute(stalls,num_occupants)


arg_list = sys.argv
input_file = open(arg_list[1])
output = open(arg_list[2], 'w')
j = 0
start_time = timeit.default_timer()
for line in input_file:
    if j ==0:
        num_cases = line
        j = j+1
    else:
        num_stalls,num_occupants = line.replace('\n', '').split(" ")
        print("input: " + str(j) + " : " + str(num_stalls) + " " +  str(num_occupants))
        max_d, min_d = bathroom_stalls_log_logic(int(num_stalls),int(num_occupants))
        print("Case #{}: {} {}".format(j,max_d,min_d))
        output.write("Case #{}: {} {}\n".format(j, max_d,min_d))
        j = j + 1
# code you want to evaluate
elapsed = timeit.default_timer() - start_time
print elapsed
