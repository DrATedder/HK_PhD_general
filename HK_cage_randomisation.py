import random
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

# -----------------------
# Setup
# -----------------------

SEED = 42
random.seed(SEED)

timepoints = [0, 4, 8, 12, 16, 20]
early = timepoints[:3]
late = timepoints[3:]

male_cages = [1, 2, 3, 4, 5, 6]
female_cages = [7, 8, 9, 10, 11, 12]

def generate_mice(sex, cages, start_num):
    mice = {}
    num = start_num
    for cage in cages:
        mice[cage] = [f"{sex}-{num+i}-{cage}" for i in range(4)]
        num += 4
    return mice

male_mice = generate_mice("male", male_cages, 1)
female_mice = generate_mice("female", female_cages, 25)

# -----------------------
# Max dispersion assignment
# -----------------------

def assign_schedule_max_dispersion(mice_by_cage):
    cages = list(mice_by_cage.keys())
    random.shuffle(cages)

    # Shuffle mice within cages
    for cage in cages:
        random.shuffle(mice_by_cage[cage])

    schedule = defaultdict(list)

    # Assign each cage to one early and one late timepoint
    early_slots = early * 2  # 6 slots
    late_slots = late * 2

    random.shuffle(early_slots)
    random.shuffle(late_slots)

    assignments = []

    for cage in cages:
        e = early_slots.pop()
        l = late_slots.pop()
        assignments.append((cage, e, l))

    # Build timepoint → cages mapping
    tp_to_cages = defaultdict(list)

    for cage, e, l in assignments:
        tp_to_cages[e].append(cage)
        tp_to_cages[l].append(cage)

    # Sanity check (each timepoint must have 2 cages)
    for tp in timepoints:
        assert len(tp_to_cages[tp]) == 2, f"Timepoint {tp} invalid"

    # Assign mice (2 per cage per visit)
    for tp in timepoints:
        for cage in tp_to_cages[tp]:
            mice = mice_by_cage[cage][:2]
            mice_by_cage[cage] = mice_by_cage[cage][2:]
            schedule[tp].extend(mice)

    return schedule

male_schedule = assign_schedule_max_dispersion(male_mice)
female_schedule = assign_schedule_max_dispersion(female_mice)

# -----------------------
# Combine
# -----------------------

final_schedule = {}

for tp in timepoints:
    final_schedule[tp] = {
        "male": male_schedule[tp],
        "female": female_schedule[tp]
    }

# -----------------------
# Print
# -----------------------

for tp in timepoints:
    print(f"\nTime {tp}h")
    print("  Males:")
    for m in final_schedule[tp]["male"]:
        print(f"    {m}")
    print("  Females:")
    for f in final_schedule[tp]["female"]:
        print(f"    {f}")

# -----------------------
# Visualisation
# -----------------------

def plot_usage(schedule, cages, title):
    usage = {cage: [0]*len(timepoints) for cage in cages}

    for i, tp in enumerate(timepoints):
        for mouse in schedule[tp]:
            cage = int(mouse.split('-')[2])
            usage[cage][i] += 1

    matrix = np.array([usage[c] for c in cages])

    plt.figure()
    plt.imshow(matrix)
    plt.xticks(range(len(timepoints)), timepoints)
    plt.yticks(range(len(cages)), cages)
    plt.xlabel("Time (h)")
    plt.ylabel("Cage")
    plt.title(title)
    plt.colorbar(label="Mice sampled")
    plt.show()

plot_usage(male_schedule, male_cages, "Male Cage Usage (Max Dispersion)")
plot_usage(female_schedule, female_cages, "Female Cage Usage (Max Dispersion)")
