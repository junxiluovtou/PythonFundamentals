import sys, csv

if sys.argv != 3:
    if len(sys.argv) > 3:
        sys.exit("Too much")
    elif len(sys.argv) < 3:
        sys.exit("Not enough")
input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, "r") as infile:
        reader = csv.DictReader(infile)

        with open(output_file, "w") as outfile:
            colnames = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=colnames)
            writer.writeheader()

            for row in reader:
                last, first = row["name"].split(", ")
                house = row["house"]
                write_dict = {"first": first, "last": last, "house": house}
                writer.writerow(write_dict)

except FileNotFoundError:
    sys.exit("Print error message stating that file was not found")
