# def mouse_in_the_kitchen():
#     rows, cols = map(int, input().split(','))
#
#     cupboard = []
#     mouse_row = mouse_col = -1
#     for r in range(rows):
#         row = list(input())
#         cupboard.append(row)
#         if 'M' in row:
#             mouse_row, mouse_col = r, row.index('M')
#
#     while True:
#         command = input()
#         if command == 'danger':
#             print("Mouse will come back later!")
#             break
#
#         if command == 'up':
#             new_row, new_col = mouse_row - 1, mouse_col
#         elif command == 'down':
#             new_row, new_col = mouse_row + 1, mouse_col
#         elif command == 'left':
#             new_row, new_col = mouse_row, mouse_col - 1
#         elif command == 'right':
#             new_row, new_col = mouse_row, mouse_col + 1
#
#         if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
#             print("No more cheese for tonight!")
#             break
#
#         if cupboard[new_row][new_col] == '@':
#             continue
#         elif cupboard[new_row][new_col] == 'T':
#             cupboard[mouse_row][mouse_col] = '*'
#             mouse_row, mouse_col = new_row, new_col
#             cupboard[mouse_row][mouse_col] = 'M'
#             print("Mouse is trapped!")
#             break
#         elif cupboard[new_row][new_col] == 'C':
#             cupboard[mouse_row][mouse_col] = '*'
#             mouse_row, mouse_col = new_row, new_col
#             cupboard[mouse_row][mouse_col] = 'M'
#             if any('C' in row for row in cupboard):
#                 continue
#             else:
#                 print("Happy mouse! All the cheese is eaten, good night!")
#                 break
#         else:
#             cupboard[mouse_row][mouse_col] = '*'
#             mouse_row, mouse_col = new_row, new_col
#             cupboard[mouse_row][mouse_col] = 'M'
#
#     for row in cupboard:
#         print(''.join(row))
#
#
# mouse_in_the_kitchen()


rows, cols = map(int, input().split(','))

cupboard = []
mouse_row = mouse_col = -1
for r in range(rows):
    row = list(input())
    cupboard.append(row)
    if 'M' in row:
        mouse_row, mouse_col = r, row.index('M')

while True:
    command = input()
    if command == 'danger':
        print("Mouse will come back later!")
        break

    if command == 'up':
        new_row, new_col = mouse_row - 1, mouse_col
    elif command == 'down':
        new_row, new_col = mouse_row + 1, mouse_col
    elif command == 'left':
        new_row, new_col = mouse_row, mouse_col - 1
    elif command == 'right':
        new_row, new_col = mouse_row, mouse_col + 1

    if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
        print("No more cheese for tonight!")
        break

    if cupboard[new_row][new_col] == '@':
        continue
    elif cupboard[new_row][new_col] == 'T':
        cupboard[mouse_row][mouse_col] = '*'
        mouse_row, mouse_col = new_row, new_col
        cupboard[mouse_row][mouse_col] = 'M'
        print("Mouse is trapped!")
        break
    elif cupboard[new_row][new_col] == 'C':
        cupboard[mouse_row][mouse_col] = '*'
        mouse_row, mouse_col = new_row, new_col
        cupboard[mouse_row][mouse_col] = 'M'
        if any('C' in row for row in cupboard):
            continue
        else:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
    else:
        cupboard[mouse_row][mouse_col] = '*'
        mouse_row, mouse_col = new_row, new_col
        cupboard[mouse_row][mouse_col] = 'M'

for row in cupboard:
    print(''.join(row))
