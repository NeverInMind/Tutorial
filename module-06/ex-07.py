def sanitize_file(source, output):
    with open(source, 'r') as pf:
        lines = pf.readline()
        no_digit = ''
        for i in lines:
            if not i.isdigit():
                no_digit += i
    with open(output, 'w') as of:
        of.write(no_digit)


source_path = ".\source-07.txt"
output_path = ".\output-07.txt"

sanitize_file(source_path, output_path)
