def hanoi_solver(disks_total):
    source_rod = list(range(disks_total, 0, -1))
    aux_rod = []
    target_rod = []

    output = ''

    def save_move():
        nonlocal output
        output += f'{source_rod} {aux_rod} {target_rod}\n'

    def move_disks(n, source, target, aux):
        if n == 1:
            target.append(source.pop())
            save_move()
        else:
            move_disks(n - 1, source, aux, target)
            target.append(source.pop())
            save_move()
            move_disks(n - 1, aux, target, source)


    save_move()
    move_disks(disks_total, source_rod, target_rod, aux_rod)

    return output[:-1]

# ========================
# Example usage
# ========================

# print(hanoi_solver(3))
# # [3, 2, 1] [] []
# # [3, 2] [] [1]
# # [3] [2] [1]
# # [3] [2, 1] []
# # [] [2, 1] [3]
# # [1] [2] [3]
# # [1] [] [3, 2]
# # [] [] [3, 2, 1]

# print(hanoi_solver(2))
# # [2, 1] [] []
# # [2] [1] []
# # [] [1] [2]
# # [] [] [2, 1]

# print(hanoi_solver(5))
# # [5, 4, 3, 2, 1] [] []
# # [5, 4, 3, 2] [] [1]
# # [5, 4, 3] [2] [1]
# # [5, 4, 3] [2, 1] []
# # [5, 4] [2, 1] [3]
# # [5, 4, 1] [2] [3]
# # [5, 4, 1] [] [3, 2]
# # [5, 4] [] [3, 2, 1]
# # [5] [4] [3, 2, 1]
# # [5] [4, 1] [3, 2]
# # [5, 2] [4, 1] [3]
# # [5, 2, 1] [4] [3]
# # [5, 2, 1] [4, 3] []
# # [5, 2] [4, 3] [1]
# # [5] [4, 3, 2] [1]
# # [5] [4, 3, 2, 1] []
# # [] [4, 3, 2, 1] [5]
# # [1] [4, 3, 2] [5]
# # [1] [4, 3] [5, 2]
# # [] [4, 3] [5, 2, 1]
# # [3] [4] [5, 2, 1]
# # [3] [4, 1] [5, 2]
# # [3, 2] [4, 1] [5]
# # [3, 2, 1] [4] [5]
# # [3, 2, 1] [] [5, 4]
# # [3, 2] [] [5, 4, 1]
# # [3] [2] [5, 4, 1]
# # [3] [2, 1] [5, 4]
# # [] [2, 1] [5, 4, 3]
# # [1] [2] [5, 4, 3]
# # [1] [] [5, 4, 3, 2]
# # [] [] [5, 4, 3, 2, 1]
