#Name:
#Programming Assignment #3
#this program iterates through a given tuple containing arrays of data on different cars
#and outputs it in simple rows and collumns
#Create a tuple and add array of cars
cars=(
["Chevloret", "Silverado", 586675, 28595],
["Chevloret", "Equinox", 270994, 25000],
["Ford", "F-Series", 787422, 30635],
["GMC", "Sierra", 253016, 29695],
["Honda", "CR-V", 333502, 26525],
["Honda", "Civic", 261225, 22000],
["Lamborgini", "Huracan", 1095, 208571],
["Toyota", "RAV4", 430387, 27325],
["Toyota", "Camry", 294348, 27325]
)

#A function to format all the car data
def fomarting(list):

    car_make= list[0]
    car_model=list[1]
    units_sold=list[2]
    starting_price=list[3]

    #formating units_sold
    new_unit_sold="{:,}".format(units_sold)

    curr="$"

    #formating starting_price
    new_starting_price='{:,.2f}'.format(starting_price)

    #align final string
    final_string = '{:<15} {:<10} {:>15}    {:<3} {:>10}'.format(car_make, car_model, new_unit_sold, curr, new_starting_price)

    return final_string

span='-----------'
#inputting the headings and the dotted lines
header='{:<15} {:<10} {:>15} {:>15}'.format("Car Make","Car Model", "Units Sold", "   Starting Price")
line='{:<15} {:<10} {:>15} {:>15}'.format(span,span,span,span)

print(header)
print(line)

#while loop to iterate through the tuple with cars and output columns and rows of the data
i=0
while(i<len(cars)):
    print(fomarting(cars[i]))

    if (i > len(cars)):
        break

    i+=1
