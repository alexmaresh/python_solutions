# After starting the training, the skier ran 10 km on the first day.
# On each subsequent day, he increased his distance by 10% of the distance of the previous day.
# Determine on which day he will run more than x km (a natural number x is entered from the keyboard).
# Display the result (the desired day) on the screen.

def ski_day(x):
    f = 10
    count = 1
    while f <= x:
        f = f + f * 0.1
        count +=1

    return count