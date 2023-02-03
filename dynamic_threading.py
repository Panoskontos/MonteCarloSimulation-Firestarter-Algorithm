import random
import sys
import time
import threading

UNBURNT= 0
SMOLDERING= 1
BURNING= 2
BURNT= 3
NUMS = 101

# Here you can change the number of threads
THREADS = 8

def main(argv, start, end):
    forest_size = 20
    n_trials = 50
    prob_min = start/100
    prob_max = end/100
    n_probs = end-start

    if len(argv) > 1:
        forest_size = int(argv[1])
    if len(argv) > 2:
        n_trials = int(argv[2])
    if len(argv) > 3:
        n_probs = int(argv[3])
    seed_by_time(0)
    forest = allocate_forest(forest_size)
    prob_spread = [0] * n_probs
    percent_burned = [0] * n_probs


    for i_prob in range(n_probs):
        if(n_probs-1!=0):
          prob_spread[i_prob] = prob_min + i_prob * (prob_max - prob_min) / (n_probs-1)
        else:
            prob_spread[i_prob] = prob_min + i_prob * (prob_max - prob_min) / (n_probs)
            
        for i_trial in range(n_trials):
            burn_until_out(forest_size, forest, prob_spread[i_prob], forest_size//2, forest_size//2)
            percent_burned[i_prob] += get_percent_burned(forest_size, forest)
        percent_burned[i_prob] /= n_trials
        print("{0}, {1}".format(prob_spread[i_prob], percent_burned[i_prob]))
        # print_forest(forest_size, forest)
    # delete_forest(forest_size, forest) 

def seed_by_time(offset):
    the_time = time.time()
    random.seed(int(the_time) + offset)

#    burn until fire is gone
def burn_until_out(forest_size, forest, prob_spread, start_i, start_j):
    count = 0
    initialize_forest(forest_size, forest)
    light_tree(forest_size, forest, start_i, start_j)
    while forest_is_burning(forest_size, forest):
        forest_burns(forest_size, forest, prob_spread)
        count += 1
    return count

def get_percent_burned(forest_size, forest):
    total = forest_size * forest_size - 1
    sum = 0
    for i in range(forest_size):
        for j in range(forest_size):
            if forest[i][j] == BURNT:
                sum += 1
    return (sum - 1) / total

def allocate_forest(forest_size):
    forest = []
    for i in range(forest_size):
        forest.append([0] * forest_size)
    return forest

def initialize_forest(forest_size, forest):
    for i in range(forest_size):
        for j in range(forest_size):
            forest[i][j] = UNBURNT

# def delete_forest(forest_size, forest):
#     for i in range(forest_size):
#         del forest[i]
#     del forest

def light_tree(forest_size, forest, i, j):
    forest[i][j] = SMOLDERING

def fire_spreads(prob_spread):
    return random.random() < prob_spread

def forest_burns(forest_size, forest, prob_spread):

    # burning trees burn down, smoldering trees ignite
    for i in range(forest_size):
        for j in range(forest_size):
            if forest[i][j] == BURNING:
                forest[i][j] = BURNT
            if forest[i][j] == SMOLDERING:
                forest[i][j] = BURNING

    # unburnt trees catch fire
    for i in range(forest_size):
        for j in range(forest_size):
            if forest[i][j] == BURNING:
                if i != 0:
                    if fire_spreads(prob_spread) and forest[i-1][j] == UNBURNT:
                        forest[i-1][j] = SMOLDERING
                if i != forest_size - 1:
                    if fire_spreads(prob_spread) and forest[i+1][j] == UNBURNT:
                        forest[i+1][j] = SMOLDERING
                if j != 0:
                    if fire_spreads(prob_spread) and forest[i][j-1] == UNBURNT:
                        forest[i][j-1] = SMOLDERING
                if j != forest_size - 1:
                    if fire_spreads(prob_spread) and forest[i][j+1] == UNBURNT:
                        forest[i][j+1] = SMOLDERING

def forest_is_burning(forest_size, forest):
    for i in range(forest_size):
        for j in range(forest_size):
            if forest[i][j] == SMOLDERING or forest[i][j] == BURNING:
                return True
    return False

def print_forest(forest_size,forest):
    for i in range(forest_size):
        for j in range(forest_size):
            if forest[i][j]==BURNT:
                print(".",end="")
            else:
                print("X",end="")
        print("\n")

def thread_function(name,start,end,j):
    print(f"Thread {j} : {start}")
    main(sys.argv,start,end)


if __name__ == '__main__':
    start_time = time.time()
    
i = 0
stop_loop = False
while(i<NUMS and not(stop_loop)):

    step = 2
    for j in range(1,THREADS):
        start = i+j
        end = start+1
        globals()['thread' + str(j)] =  threading.Thread(target=thread_function, args=(i,start,end,j) ) 
        if(start>=NUMS):
            stop_loop=True
            break
        else:
            globals()['thread' + str(j)].start()
            globals()['thread' + str(j)].join()
        
        
    i+=THREADS-1
    


end_time = time.time()
print("Execution time:", end_time-start_time)

