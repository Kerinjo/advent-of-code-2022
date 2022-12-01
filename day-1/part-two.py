with open("input") as f:
    

    top_three = [0, 0, 0]
    cur_sum = 0

    for line in f:
        # for each line - 
        # sum up lines up to '\n'
        if line != '\n': 
            cur_sum += int(line)
        else:  # if that line = '\n' break sequence 
            for i in range(len(top_three)):
                if cur_sum > top_three[i]:
                    
                    temp = top_three[i]
                    top_three[i] = cur_sum
                    cur_sum = temp  # replace with previous element
                    # so that it can compare with the rest of the list        
                   
            cur_sum = 0  # reset sum
    
    top_sum = 0
    for elem in top_three:
        top_sum += elem

    print(top_sum)

