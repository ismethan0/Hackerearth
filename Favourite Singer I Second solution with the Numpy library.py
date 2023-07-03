import numpy as np

n = int(input())
playlist = np.array(input().split(), dtype=int)

unique_elements, counts = np.unique(playlist, return_counts=True)
max_count = np.max(counts)

cashe = unique_elements[counts == max_count]

print(len(cashe) if len(cashe) > 0 else 1)
