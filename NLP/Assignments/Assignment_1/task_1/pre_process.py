import csv

def pre_process(csv_file, column_name):
    # read a csv file, in each line, remove characters apart from alphanumerics and whitespaces in the given column
    
    lines = []

    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        lines = list(reader)
        column_index = lines[0].index(column_name)
        for i in range(1, len(lines)):
            lines[i][column_index] = ''.join([c for c in lines[i][column_index] if c.isalnum() or c.isspace()])
        
    # write the pre-processed data to a new csv file named "pre_processed + csv_file" in the same directory
    
    # get csv file directory
    csv_file_dir = csv_file.split('/')

    # get csv file name
    csv_file_name = csv_file_dir[-1]

    # add "pre_processed" to the csv file name
    pre_processed_csv_file_name = "pre_processed_" + csv_file_name

    # get csv file directory
    csv_file_dir = csv_file_dir[:-1]

    # get the final path of the resulting csv file
    pre_processed_csv_file_path = '/'.join(csv_file_dir) + '/' + pre_processed_csv_file_name

    # write the pre-processed data to the resulting csv file
    with open(pre_processed_csv_file_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(lines)