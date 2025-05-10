import random
winning_list = []
for i in range(0, 5):
    n = random.randint(1, 70)
    winning_list.append('%02d' % n)
    winning_list.sort()

n_last = random.randint(1, 25)
winning_list.append('%02d' % n_last)

print(winning_list)