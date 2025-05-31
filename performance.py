import time

def measure_performance(search_algorithm, problem, verbose=False):
    """
    Wrapper function to measure the time and space performance of the search algorithm.
    """
    # Start measuring time
    start_time = time.time()

    # Run the search algorithm, capturing the solution and max frontier size
    solution_result, max_frontier_size = search_algorithm(problem, verbose=verbose)

    # Measure elapsed time
    elapsed_time = time.time() - start_time

    return {
        'solution': solution_result[0] if solution_result else None,
        'cost': solution_result[1] if solution_result else 0,  # Ensure the cost is captured
        'elapsed_time': elapsed_time,
        'max_frontier_size': max_frontier_size  # Return the max number of nodes in the frontier
    }
