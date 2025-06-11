# Ask user for width and loop until they
# enter a number that is more than zero
def int_check(question, low):

    error = f"Please enter a number that is more than or equal to {low}\n"
    while True:

        try:
            # ask the user for a number
            response = int(input(question))

            # check that the number is more than zero
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# calculates how many bits are needed to represent and integer
def image_clac():
    # Get the image dimensions
    width = int_check("Width: ", 1)
    height = int_check("Height: ", 1)

    # calculate the number of pixels and multiply by 24 to get number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # Set up answer and return it
    answer = (f"Number of pixels: {width} x {height} = {num_pixels} "
             f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer


# Main routine goes here
image_ans = image_clac()
print(image_ans)