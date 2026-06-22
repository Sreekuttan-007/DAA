import time
import random
import matplotlib.pyplot as plt

def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    comparisons = 0
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == key: return mid, comparisons
        elif arr[mid] < key: low = mid + 1
        else: high = mid - 1
    return -1, comparisons

def interpolation_search(arr, key):
    low, high = 0, len(arr) - 1
    comparisons = 0
    while low <= high and key >= arr[low] and key <= arr[high]:
        comparisons += 1
        if low == high: break
        # Position formula
        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (key - arr[low])))
        if arr[pos] == key: return pos, comparisons
        elif arr[pos] < key: low = pos + 1
        else: high = pos - 1
    return -1, comparisons

# Benchmarking
sizes = [1000, 5000, 10000, 50000, 100000]
results = []

for size in sizes:
    arr = sorted([random.randint(1, 1000000) for _ in range(size)])
    key = random.choice(arr)
    
    # Binary Search
    start = time.perf_counter()
    _, b_comp = binary_search(arr, key)
    b_time = (time.perf_counter() - start) * 1000
    
    # Interpolation Search
    start = time.perf_counter()
    _, i_comp = interpolation_search(arr, key)
    i_time = (time.perf_counter() - start) * 1000
    
    results.append([size, b_time, b_comp, i_time, i_comp])

# Display Table
print(f"{'Size':<10} | {'B-Time(ms)':<12} | {'B-Comp':<8} | {'I-Time(ms)':<12} | {'I-Comp':<8}")
for r in results:
    print(f"{r[0]:<10} | {r[1]:<12.6f} | {r[2]:<8} | {r[3]:<12.6f} | {r[4]:<8}")

# Plotting
plt.plot(sizes, [r[1] for r in results], label='Binary Search')
plt.plot(sizes, [r[3] for r in results], label='Interpolation Search')
plt.xlabel('Dataset Size')
plt.ylabel('Time (ms)')
plt.legend()
plt.title('Performance Comparison')
plt.show()
