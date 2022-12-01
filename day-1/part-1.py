with open("input") as f:
    
    max = 0
    cur_sum = 0

    for line in f:
        # for each line - 
        # sum up lines up to '\n'
        if line != '\n': 
            cur_sum += int(line)
        else:  # if that line = '\n' break sequence 
            if cur_sum > max:  # is the sum bigger than max?
                max = cur_sum  # then replace max with sum
            cur_sum = 0  # reset sum
    
    print(max)




