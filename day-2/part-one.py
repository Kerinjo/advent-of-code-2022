with open("day-2/input") as f:

    score = 0

    for line in f:
        opp_choice = line[0]
        your_choice = line[2]

        # your choice is scored separately
        # Z - 3 points, Y - 2 points, X - 1 point
        # Z - Scissors, Y - Paper   , X - Rock
        # loss - 0 points, draw - 3 points, win - 6 points

        if opp_choice == 'A':
            # if opp choose Rock
            if your_choice == 'Z':
                # if you choose scissors
                score += (3 + 0)
            elif your_choice == 'Y':
                # if you choose paper
                score += (2 + 6)
            elif your_choice == 'X':
                # if you choose rock
                score += (1 + 3)

        elif opp_choice == 'B':
            # if opp choose Paper
            if your_choice == 'Z':
                # if you choose scissors
                score += (3 + 6)
            elif your_choice == 'Y':
                # if you choose paper
                score += (2 + 3)
            elif your_choice == 'X':
                # if you choose rock
                score += (1 + 0)

        elif opp_choice == 'C':
            # if opp choose Scissors
            if your_choice == 'Z':
                # if you choose scissors
                score += (3 + 3)
            elif your_choice == 'Y':
                # if you choose paper
                score += (2 + 0)
            elif your_choice == 'X':
                # if you choose rock
                score += (1 + 6)
        
    print(score)