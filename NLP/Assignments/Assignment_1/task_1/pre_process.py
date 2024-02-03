import csv

def pre_process(csv_file, out_csv_file, column_name):
    # read a csv file, in each line, remove characters apart from alphanumerics and whitespaces in the given column
    lines = []

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        lines = list(reader)

        # Index of the column to be pre processed
        column_index = lines[0].index(column_name)

        for i in range(1, len(lines)):
            lines[i][column_index] = ''.join([c for c in lines[i][column_index] if c.isalnum() or c.isspace()])

    # write the pre-processed data to the resulting csv file
    with open(out_csv_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(lines)

    print("Pre procesing completed")