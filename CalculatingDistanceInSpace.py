# first we will create an introduction so the user will understand 
def intro():
    introduction = print("This program will calculate the distance between two points " +
                    "in space given their respective X, Y, and Z coordinates" +
                    "\n" + "(Hint: If your two points are 2-dimensional, your Z-coordinates will be 0)")
    return introduction

# in order to calculate the distance between two points
# we'll need to know the coordinates of the two points
# create a function to get user defined coordinates
def get_coordinates():
    # we will use try/except to try and account for bad input
    # we can also gather all of the values at once using the map function
    while True:
        try:
            (x1, y1, z1, x2, y2, z2, *other ) = map(float, input("Enter X, Y, and Z coordinates for both points" +
                                                                 "\n(Separate your values with a comma): ").split(","))
            # we can print the given coordinates so the user can verify they are correct
            print("Point 1: [{}, {}, {}] \nPoint 2: [{}, {}, {}]".format(x1, y1, z1, x2, y2, z2))
            # if there are too many values we can let the user know and show them which value was extra
            if other:
                print ('you entered too many coordinates')
                print()
                print(other)
        # if the input is bad we'll give the user a little more guidance
        except ValueError:
            print("-------------------------------------------------------------------------")
            print("The coordinates should only contain numbers and be separated with a comma")
            # we'll also print a new line to allow some space between the instructions
            print()
        else:
            return x1, y1, z1, x2, y2, z2

# next we'll add our own square root function
def sqrt(x):
    square_root = x**(1/2)
    return square_root

# create a function to calculate distance using the coordinates provided by the user
def calculate_distance(given_coordinates):
    coordinates = []
    
    for coordinate in given_coordinates:
        coordinates.append(coordinate)
    
    diff_Xs = abs(coordinates[0] - coordinates[3]);
    diff_Ys = abs(coordinates[1] - coordinates[4]);
    diff_Zs = abs(coordinates[2] - coordinates[5]);

    distance = sqrt((diff_Xs**2) + (diff_Ys**2) + (diff_Zs**2));
    return round(distance, 3);

# create a function to print the calculated distance between the two points
def display_distance(calculated_distance):
    print("The distance between points (X1, Y1, Z1) and (X2, Y2, Z2) = " + str(calculated_distance))
# here we'll put it all together so it can be run by soley calling main()
def main():
    intro()
    coordinate_values = get_coordinates()
    calculated_distance = calculate_distance(coordinate_values)
    display_distance(calculated_distance)