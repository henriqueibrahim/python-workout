def run_timing():
    total_runs = 0
    total_time = 0

    while True:
        run = input("Enter 10 km run time: ")

        if not run:
            break

        total_runs += 1
        total_time += float(run)

        avg = total_time / total_runs

    print(f"Average of {avg}, over {total_runs}")

run_timing()


