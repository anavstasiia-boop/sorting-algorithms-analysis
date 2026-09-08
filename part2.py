"""
Created on Wed Dec 16 16:37:28 2025

@author: anastasiavereshchak
"""


import random
import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter


def generate_rnd_array1(n, vmax=1000):
    x = np.zeros(n)
    for i in range(n):
        x[i] = random.randint(0, vmax) * 0.01 * i
    return x


def generate_rnd_array2(n, vmax=1000):
    x = np.zeros(n)
    for i in range(n):
        x[i] = i + 10 * np.sin(2 * np.pi * 0.01) * random.randint(0, vmax)
    return x


def quicksort(arr2sort):
    arr2sort = arr2sort.copy()
    if arr2sort.shape[0] <= 1:
        return arr2sort
    pivot = arr2sort[-1]
    i = 0
    for j in range(arr2sort.shape[0]):
        if arr2sort[j] <= pivot:
            arr2sort[i], arr2sort[j] = arr2sort[j], arr2sort[i]
            i += 1
    first = arr2sort[:i - 1]
    second = arr2sort[i:]
    return np.concatenate((quicksort(first), np.array([arr2sort[i - 1]]), quicksort(second)))


def mergesort(list2sort):
    if len(list2sort) <= 1:
        return list2sort
    middle = len(list2sort) // 2
    first_sorted = mergesort(list2sort[:middle])
    second_sorted = mergesort(list2sort[middle:])

    combined = []
    i = j = 0
    while i < len(first_sorted) and j < len(second_sorted):
        if first_sorted[i] < second_sorted[j]:
            combined.append(first_sorted[i]);
            i += 1
        else:
            combined.append(second_sorted[j]);
            j += 1
    combined.extend(first_sorted[i:])
    combined.extend(second_sorted[j:])
    return combined


def bubblesort(arr2sort):
    arr2sort = arr2sort.copy()
    for i in range(1, arr2sort.shape[0]):
        for j in range(arr2sort.shape[0] - i):
            if arr2sort[j] > arr2sort[j + 1]:
                arr2sort[j], arr2sort[j + 1] = arr2sort[j + 1], arr2sort[j]
    return arr2sort


def average_time(data: np.ndarray, n: int, f):
    if n < 10:
        n = 10
    total = 0.0
    for _ in range(n):
        temp = data.copy()
        t0 = perf_counter()
        f(temp)
        t1 = perf_counter()
        total += (t1 - t0)
    return total / n


def estimate_complexity(data: np.ndarray, max_n: int, f):
    results = []
    for sample in range(1, max_n + 1):
        nums = data[:sample]
        results.append(average_time(nums, 10, f))
    return results


def main():
    arr1 = generate_rnd_array1(1000)
    arr2 = generate_rnd_array2(1000)

    fig, axs = plt.subplots(3, 1, figsize=(6, 8))

    axs[0].plot(arr1, label="Unsorted values")
    axs[0].plot(bubblesort(arr1), label="Sorted values (Bubble)")
    axs[0].set_ylabel("Values")
    axs[0].legend()

    axs[1].plot(arr2, label="Unsorted values")
    axs[1].plot(np.array(mergesort(arr2)), label="Sorted values (Merge)")
    axs[1].set_ylabel("Values")
    axs[1].legend()

    comp1 = estimate_complexity(arr1, 1000, bubblesort)
    comp2 = estimate_complexity(arr1, 1000, mergesort)
    comp3 = estimate_complexity(arr1, 1000, quicksort)

    axs[2].plot(range(1, 1001), comp1, label="Bubble")
    axs[2].plot(range(1, 1001), comp2, label="Merge")
    axs[2].plot(range(1, 1001), comp3, label="Quick")

    axs[2].set_ylabel("Average time to sort (s)")
    axs[2].set_xlabel("Number of samples")
    axs[2].legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
