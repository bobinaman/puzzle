import cv2
import puzzle_piece
import image_reading


# Create a Piece instance with initial arrays
piece = puzzle_piece.Piece([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])

# Print the initial arrays
piece.print_arrays()

# Update array1
piece.set_array1([13, 14, 15])

# Get the updated array1
updated_array1 = piece.get_array1()
print("Updated Array 1:", updated_array1)
print("Hello World")