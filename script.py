# Create a file handle for starbucks_us_locations.csv and the output csv file.

# With the location file open, read all the lines in the csv. make sure to skip
# the heading.

# For each line, split the line using commas. Extract the name column (third
# column), then extract the state abbreviation from the name column using
# index place 12 and 13.

# Append all of the state abbreviations to their own list.

# Create a dictionary with the state abbreviation as the key and the number of
# times its found in the list as the value.

# Write the dictionary to state_count.csv

import csv


def main():
    state_abbrev = []

    # file handles
    infile = r"C:\Users\lpbiz\OneDrive\Desktop\py4e\code3\starbucks_us_locations.csv"
    outfile = r"C:\Users\lpbiz\OneDrive\Desktop\py4e\code3\Lab4_L_Bizeau.csv"

    # read from CSV file
    with open(infile, 'r') as sbcsvfile:
        lines = sbcsvfile.readlines()
        for line in lines:
            # Skip the field headings/titles
            if line.startswith("L"):
                continue
            # Split the attributes in the line with commas as the delimiter.
            commasplit = line.split(",")
            # Extract the name column
            name = commasplit[2]
            # Extract the state abbreviation
            state = name[12]+name[13]
            # Add all abbreviations to master abbreviation list
            state_abbrev.append(state)
    # Create dictionary with state abbreviations as the key and the number of
    # times they're found in the list as value
    state_dict = {i:state_abbrev.count(i) for i in state_abbrev}

    # Write to a new CSV file
    with open(outfile, 'w', newline = '') as out:
        csv_out = csv.writer(out)
        # Write a heading for each of the fields.
        csv_out.writerow(['State', 'Count'])
        for key, value in state_dict.items():
            csv_out.writerow([key, value])


if __name__ == '__main__':
        main()
