# https://medium.com/@peterkellyonline/weighted-random-selection-3ff222917eb6
# Add up all the weights for all the items in the list
# Pick a number at random between 1 and the sum of the weights
# Iterate over the items
# For the current item, subtract the item’s weight from the random number that was originally picked
# Compare the result to zero. If less than or equal to zero then break otherwise keep iterating.
# The key is that the larger the weight the more likely to be less than zero when compared to the random
# selection between zero and the sum of weights.
# If not less than zero, continue iterating over the list, all the while subtracting more and more weights off
# the random number chosen from the sum of the weights.


import random as random

# def generator(val, tmp_list):
def generator(val):

    prob_dict = {
        "legendary_prob": 0.015,
        "mystical_prob": 0.05,
        "gold_prob": 0.2,
        "silver_prob": 0.3,
        "bronze_prob": 0.435,
    }

    key_list = list(prob_dict.keys())
    val_list = list(prob_dict.values())

    for i in range(prob_dict.__len__()):
        val_list[i] *= 1000
        val_list[i] = int(val_list[i])

    sum_weights = sum(val_list)

    multiplier = 1

    if val == 1:
        multiplier *= 4
        for i in key_list[:2]:
            index = key_list.index(i)
            val_list[index] *= multiplier
    elif val == 2:
        multiplier *= 2
        for i in key_list[:2]:
            index = key_list.index(i)
            val_list[index] *= multiplier
    else:
        pass

    # Randomise a number
    rand_weight = random.randint(1, sum_weights)

    for i in range(prob_dict.__len__()):
        rand_weight -= val_list[i]

        if rand_weight <= 0:
            x = key_list[i]
            print(x)
            break

    # # For mass inputs
    # if x == "legendary_prob":
    #     tmp_list[0] += 1
    # elif x == "mystical_prob":
    #     tmp_list[1] += 1
    # elif x == "gold_prob":
    #     tmp_list[2] += 1
    # elif x == "silver_prob":
    #     tmp_list[3] += 1
    # elif x == "bronze_prob":
    #     tmp_list[4] += 1


flag = 0

while flag == 0:
    print("Insert a number between 1 to 3.")
    print("Number 1: Premium draw")
    print("Number 2: Super draw")
    print("Number 3: Normal draw")

    val = int(input())

    tmp_list = [1, 2, 3]
    if val not in tmp_list:
        print("Insert only number 1 - 3")
    else:
        print("Inserted number: " + str(val))
        generator(val)

        print("Play again? y/n")

        while True:

            play_again = input()
            if play_again == 'y':
                break
            elif play_again == 'n':
                flag = 1
                break
            else:
                print("Type only y/n")


# For mass inputs
# val = 3
# tmp_list = [0, 0, 0, 0, 0]
#
# for i in range(0,1000):
#
#     generator(val, tmp_list)
#
# print(tmp_list)
