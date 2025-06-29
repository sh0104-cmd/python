import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result_list):
    primes = [n for n in range(start, end) if is_prime(n)]
    result_list.extend(primes)

def threaded_prime_checker(start_range, end_range, num_threads=4):
    threads = []
    results = []
    result_lock = threading.Lock()
    step = (end_range - start_range) // num_threads

    for i in range(num_threads):
        start = start_range + i * step
        end = start_range + (i + 1) * step if i < num_threads - 1 else end_range

        thread = threading.Thread(
            target=lambda s=start, e=end: check_primes_threadsafe(s, e, results, result_lock)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    results.sort()
    print("Primes:", results)

def check_primes_threadsafe(start, end, shared_list, lock):
    local_primes = [n for n in range(start, end) if is_prime(n)]
    with lock:
        shared_list.extend(local_primes)

# Example usage:
threaded_prime_checker(1, 100, num_threads=4)


import threading
from collections import Counter
import os

def count_words(lines, result_counter, lock):
    local_counter = Counter()
    for line in lines:
        words = line.strip().split()
        local_counter.update(words)

    with lock:
        result_counter.update(local_counter)

def threaded_word_count(file_path, num_threads=4):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    threads = []
    result_counter = Counter()
    lock = threading.Lock()
    chunk_size = len(lines) // num_threads

    for i in range(num_threads):
        start = i * chunk_size
        end = None if i == num_threads - 1 else (i + 1) * chunk_size
        thread_lines = lines[start:end]

        thread = threading.Thread(
            target=count_words, args=(thread_lines, result_counter, lock)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for word, count in result_counter.most_common(10):
        print(f"{word}: {count}")

# Example usage:
# Save some sample text to test:
with open("sample.txt", "w", encoding='utf-8') as f:
    f.write("hello world\nthis is a test file\nhello again\nthreading is fun\n")

threaded_word_count("sample.txt", num_threads=3)
