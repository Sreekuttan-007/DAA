import time
import random

def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1
    probes = 0

    while low <= high and key >= arr[low] and key <= arr[high]:
        probes += 1
        
        # Edge case: if low equals high
        if low == high:
            if arr[low] == key:
                return low, probes
            return -1, probes

        # Formula: pos = low + [(key - arr[low]) * (high - low) / (arr[high] - arr[low])]
        # Using integer division
        pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (key - arr[low])))

        if arr[pos] == key:
            return pos, probes
        
        if arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1
            
    return -1, probes

def get_dataset():
    print("\n--- Dataset Configuration ---")
    dist_type = input("Choose distribution (1: Uniform, 2: Non-Uniform): ")
    size = int(input("Enter number of elements: "))
    
    if input("Generate randomly? (y/n): ").lower() == 'y':
        if dist_type == '1':
            # Uniform: Step-based generation
            data = sorted([random.randint(1, size * 10) for _ in range(size)])
        else:
            # Non-Uniform: Clustered/Exponential generation
            data = sorted([int(random.expovariate(0.1)) for _ in range(size)])
    else:
        data = sorted([int(x) for x in input("Enter elements separated by space: ").split()])
    
    return data

# Execution
data = get_dataset()
key = int(input("Enter search key: "))

start_time = time.perf_counter()
index, probes = interpolation_search(data, key)
end_time = time.perf_counter()

print(f"\n--- Results ---")
print(f"Index: {index if index != -1 else 'Not Found'}")
print(f"Probes: {probes}")
print(f"Time Taken: {(end_time - start_time) * 1000:.4f} ms")
