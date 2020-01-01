slice_with_step = slice(1, 10, 3)  # indexes 1, 4, 7 excluding 10
print(slice_with_step)  # slice(1, 10, 3)

powers_of_two = [1, 2, 4, 8, 16, 32, 64,
                 128, 256, 512, 1024]

print(powers_of_two[slice_with_step])  # [2, 16, 128]
