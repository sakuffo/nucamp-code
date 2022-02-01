inches_snow = {"Monday": 2, "Thuesday": 4, "Wednesday": 5}

# write a function named print_total_snowfall


def print_total_snowfall(inches_snow):
    total_inches = 0
    for inches in inches_snow:
        total_inches += inches_snow[inches]
    print(f'Total snowfall inches: {total_inches}')
    thurs_snow = input("How many inches of snow fell on Thursday? ")
    total_inches += int(thurs_snow)
    print(f'Total snowfall inches: {total_inches}')
    return total_inches


print_total_snowfall(inches_snow)
