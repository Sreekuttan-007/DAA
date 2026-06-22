import random
import math
import time
import matplotlib.pyplot as plt

# Interpolation Search Function
def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high and key >= arr[low] and key <= arr[high]:

        if low == high:
            if arr[low] == key:
                return low
            return -1

        # Interpolation Formula
        pos = low + int(
            ((float(high - low) / (arr[high] - arr[low]))
             * (key - arr[low]))
        )

        if arr[pos] == key:
            return pos

        if arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1

    return -1


# -------- Main Program --------
n = int(input("Enter the number of elements to generate: "))

# Generate Uniformly Distributed Sorted Array
arr = [i * 10 for i in range(1, n + 1)]

print("\nUniform Sorted Array Generated Successfully.")

key = int(input("Enter the element to search: "))

# Execution Time Measurement
start_time = time.perf_counter()

result = interpolation_search(arr, key)

end_time = time.perf_counter()

execution_time = (end_time - start_time) * 1000000  # microseconds

# Display Result
if result != -1:
    print(f"\nElement {key} found at index {result}")
else:
    print(f"\nElement {key} not found")

# Complexity Information
print("\nComplexity Analysis")
print("-------------------")
print("Best Case Time Complexity    : O(1)")
print("Average Case Time Complexity : O(log log n)")
print("Worst Case Time Complexity   : O(n)")
print("Space Complexity             : O(1)")

print(f"\nExecution Time: {execution_time:.4f} microseconds")

# ---------- Time Complexity Graph ----------
sizes = [100, 500, 1000, 5000, 10000, 50000, 100000]

# Theoretical O(log log n)
complexity_values = [math.log2(math.log2(x)) for x in sizes]

plt.figure(figsize=(8, 5))
plt.plot(sizes, complexity_values, marker='o')

plt.title("Interpolation Search Time Complexity Growth")
plt.xlabel("Input Size (n)")
plt.ylabel("log₂(log₂(n))")
plt.grid(True)
plt.show()
