import random

def is_non_consecutive(a, b):
    """Return True if a and b are not consecutive."""
    return abs(a - b) != 1

N = 100000  # number of trials
count_non_consecutive = 0

for _ in range(N):
    # Step 1: Start with the full set [1..7]
    numbers = list(range(1, 10))

    # Step 2: Choose the first pair randomly
    pair1 = random.sample(numbers, 2)
    # Remove those numbers from the pool
    for x in pair1:
        numbers.remove(x)

    # Step 3: Choose the second pair randomly from remaining 5
    pair2 = random.sample(numbers, 2)

    # Step 4: If the second pair contains 1, replace it
    if 1 in pair2:
        pair2.remove(1)
        # Choose a new number from the remaining numbers (which does not include 1 or the existing item in pair2)
        possible_choices = [n for n in numbers if (n not in pair2 and n != 1)]
        new_num = random.choice(possible_choices)
        pair2.append(new_num)

    # Check if both pairs are made of non-consecutive numbers
    if (is_non_consecutive(*pair1) and is_non_consecutive(*pair2)):
        count_non_consecutive += 1

print(f"Out of {N} trials, {count_non_consecutive} had both pairs non-consecutive.")
print(f"Fraction = {count_non_consecutive / N:.3f}")
