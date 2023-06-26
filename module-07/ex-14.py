def to_indexed(source_file, output_file):
    with open(source_file, 'r') as pf:
        with open(output_file, 'w') as ph:
            filt = pf.readlines()
            counter = 0
            for item in filt:
                item = f'{counter}: {item}'
                counter += 1
                ph.write(item)


old = '.\output-14.txt'
new = '.\output-14_new.txt'
to_indexed(old, new)
