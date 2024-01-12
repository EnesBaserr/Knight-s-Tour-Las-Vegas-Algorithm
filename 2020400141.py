import random
import time
import main2
import sys
import math


if(str(sys.argv[1]) == "part1"):

    def is_valid_move(x, y, n, visited):
        return 0 <= x < n and 0 <= y < n and visited[x][y] == -1

    def knights_tour(n, p):
        start_time = time.time()
        total_squares = n * n
        min_successful_squares = int(total_squares * p)

        def random_move(x, y, visited):
            possible_moves = [
                (x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2),
                (x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1)
            ]
            random.shuffle(possible_moves)
            for move_x, move_y in possible_moves:
                if is_valid_move(move_x, move_y, n, visited):
                    return move_x, move_y
            return None

        def run_tour(file):
            knight_x, knight_y = random.randint(0, n - 1), random.randint(0, n - 1)
            visited = [[-1 for _ in range(n)] for _ in range(n)]
            count = 0

            file.write(f"Run {i}: starting from ({knight_x},{knight_y})\n")

            while count < total_squares:
                visited[knight_x][knight_y] = count
                count += 1
                if(count !=1):

                    file.write(f"Stepping into ({knight_x},{knight_y})\n")

                next_move = random_move(knight_x, knight_y, visited)
                if next_move is None:
                    break

                knight_x, knight_y = next_move

            successful = count > min_successful_squares
            result_str = f"{'Uns' if not successful else 'S'}uccessful - Tour length: {count}\n"
            file.write(result_str)

            for j in range(n):
                file.write(" ".join(map(str, visited[j])))
                file.write("\n")

            return successful, count

        successful_tours = 0
        total_trials = 100000
            
        with open(f"results_{p}.txt", "w") as file:
                
            for i in range(1, total_trials + 1):
                    
                successful, count = run_tour(file)
                end_time = time.time()
                elapsed_time = end_time - start_time

                if successful:
                    successful_tours += 1

                #if i == 1:
                    #print(f"Elapsed time: {elapsed_time} seconds\n")

        probability = successful_tours / total_trials

        print(f"LasVegas Algorithm With p = {p}")
        print(f"Number of successful tours: {successful_tours}")
        print(f"Number of trials: {total_trials}")
        print(f"Probability of a successful tour: {probability}")
        print()
       # print(f"Elapsed time: {elapsed_time} seconds\n")
       #print(f"Reason for termination: {'Reached minimum successful squares' if successful else 'Unable to reach minimum successful squares'}")

    #print(str(sys.argv[1]))
    knights_tour(8, 0.7)
    
    knights_tour(8, 0.8)
   
    knights_tour(8, 0.85)
elif (str(sys.argv[1]) == "part2"):
    def is_valid_move(x, y, n, visited):
        return 0 <= x < n and 0 <= y < n and visited[x][y] == -1

    def knights_tour(n, p_value, k):
        start_time = time.time()
        total_squares = n * n
        min_successful_squares = (total_squares * p_value)

        def random_move(x, y, visited):
            possible_moves = [
                (x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2),
                (x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1)
            ]
            random.shuffle(possible_moves)
            for move_x, move_y in possible_moves:
                if is_valid_move(move_x, move_y, n, visited):
                    return move_x, move_y
            return None

        def run_tour():
            knight_x, knight_y = random.randint(0, n - 1), random.randint(0, n - 1)
            visited = [[-1 for _ in range(n)] for _ in range(n)]
            count = 0

            #file.write(f"Run {i}: starting from ({knight_x},{knight_y})\n")

            # Fix the first k moves
            for _ in range(k):
                visited[knight_x][knight_y] = count

                count += 1
                #file.write(f"{count} Stepping into ({knight_x},{knight_y})\n")
                next_move = random_move(knight_x, knight_y, visited)
                if next_move is None:
                    break
                knight_x, knight_y = next_move

            # Continue with backtracking
            def backtrack(x, y):
                nonlocal count
                visited[x][y] = count
                count += 1
                #file.write(f"{count} Stepping into ({x},{y})\n")

                if count >= min_successful_squares:
                    return True  # Tour successful

                possible_moves = [
                    (x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2),
                    (x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1)
                ]
                random.shuffle(possible_moves)
                possible_moves.sort(key=lambda move: len([
                    1 for i, j in possible_moves if is_valid_move(i, j, n, visited)
                ]))

                for move_x, move_y in possible_moves:
                    if is_valid_move(move_x, move_y, n, visited):
                        if backtrack(move_x, move_y):
                            
                            return True  # Successful tour
                visited[x][y] = -1  # Backtrack
                return False

            if not backtrack(knight_x, knight_y):
                result_str = f"Unsuccessful - Tour length: {count}\n"
            else:
                result_str = f"Successful - Tour length: {count}\n"

            #file.write(result_str)

            
        # print(f"Count is {count}")
            return count >(min_successful_squares)

        successful_tours = 0
        total_trials = 100000

    
    
        
        for i in range(1, total_trials + 1):
            successful = run_tour()
            if successful:
                successful_tours += 1

        probability = successful_tours / (total_trials )
        
        print(f"LasVegas Algorithm With p = {p_value} and k = {k}")
        print(f"Number of successful tours: {successful_tours}")
        print(f"Number of trials: {total_trials}")
        print(f"Probability of a successful tour: {probability}")
        print()
        #print(f"Elapsed time: {time.time() - start_time} seconds\n")

    print(f"--- p = {0.7} ---")    
    knights_tour(8, 0.7, 0)
    knights_tour(8, 0.7, 2)
    knights_tour(8, 0.7, 3)
    print(f"--- p = {0.8} ---")
    knights_tour(8, 0.8, 0)
    knights_tour(8, 0.8, 2)
    knights_tour(8, 0.8, 3)
    print(f"--- p = {0.85} ---")

    knights_tour(8, 0.85, 0)
    knights_tour(8, 0.85, 2)
    knights_tour(8, 0.85, 3)

