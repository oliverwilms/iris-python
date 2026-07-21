import tracemalloc
import time

# Example function that allocates memory
def my_function():
    # Simulate some memory usage
    data = [x ** 2 for x in range(100000)]
    time.sleep(0.05)  # Simulate work
    return sum(data)

def measure_memory_over_runs(func, runs=5):
    tracemalloc.start()  # Start tracing memory allocations
    
    prev_snapshot = tracemalloc.take_snapshot()
    
    for i in range(1, runs + 1):
        func()  # Run the target function
        
        # Get current and peak memory usage
        current, peak = tracemalloc.get_traced_memory()
        print(f"[Run {i}] Current: {current / 1024:.1f} KB | Peak: {peak / 1024:.1f} KB")
        
        # Compare snapshots to see what changed
        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.compare_to(prev_snapshot, 'lineno')
        
        print(f"  Top memory changes since last run:")
        for stat in top_stats[:3]:  # Show top 3 changes
            print(f"    {stat}")
        
        prev_snapshot = snapshot  # Update for next comparison
    
    tracemalloc.stop()  # Stop tracing

if __name__ == "__main__":
    measure_memory_over_runs(my_function, runs=5)
