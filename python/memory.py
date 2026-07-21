import tracemalloc
import time

# 1. START TRACING
# tracemalloc.start(10) # Optional: set number of frames to store (default is 1)
tracemalloc.start()

# --- Snapshot 1 (Baseline) ---
snap1 = tracemalloc.take_snapshot()

# 2. CAUSE MEMORY ALLOCATION
data = []
for i in range(1000):
    # This line allocates memory for a string in each iteration
    data.append("A very long string that uses memory " * 10) 

# --- Snapshot 2 (After Operation) ---
snap2 = tracemalloc.take_snapshot()

# 3. COMPARE AND DISPLAY
print("--- Top 10 files using memory between Snapshots ---")
top_stats = snap2.compare_to(snap1, 'lineno') # 'lineno' groups by file and line number

for stat in top_stats[:10]:
    # Display the file, line number, size difference, and count difference
    print(f"{str(stat.traceback).split(' ')[-1]}: {stat.size_diff / 1024:.1f} KiB "
          f"({stat.count_diff} blocks)")

# 4. STOP TRACING (Good Practice)
tracemalloc.stop()

# Output will likely point to the line 'data.append(...)' in the current file.
