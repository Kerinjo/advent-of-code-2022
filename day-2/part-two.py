with open("day-2/input") as f:

    score = 0

    for line in f:
        opp_choice = line[0]
        your_choice = line[2]

        # Z - Win, Y - Draw, X - Lose
        # loss - 0 points    , draw - 3 points , win - 6 points
        # scissors - 3 points, paper - 2 points, rock - 1 point

        if opp_choice == 'A':
            # if opp choose Rock
            if your_choice == 'Z':
                # if you win - paper
                score += (2 + 6)
            elif your_choice == 'Y':
                # if you draw - rock
                score += (1 + 3)
            elif your_choice == 'X':
                # if you lose - scissors 
                score += (3 + 0)

        elif opp_choice == 'B':
            # if opp choose Paper
            if your_choice == 'Z':
                # if you win - scissors
                score += (3 + 6)
            elif your_choice == 'Y':
                # if you draw - paper
                score += (2 + 3)
            elif your_choice == 'X':
                # if you lose - rock
                score += (1 + 0)

        elif opp_choice == 'C':
            # if opp choose Scissors
            if your_choice == 'Z':
                # if you win - rock
                score += (1 + 6)
            elif your_choice == 'Y':
                # if you draw - scissors
                score += (3 + 3)
            elif your_choice == 'X':
                # if you lose - paper
                score += (2 + 0)
        
    print(score)