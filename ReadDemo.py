import os

doscar = open('./DOSCAR', 'r')
lines = doscar.readlines()
doscar.close()

# read header
line = lines[0].split()
num_of_ions_empty_spheres = int(line[0])
num_of_ions = int(line[1])
partial_dos = line[2]
ncdij = line[3]

number_of_bins = int(lines[5].split()[2])

# read total dos
offset = 6
count = offset + number_of_bins  # rename count!
dens_of_state = lines[offset:count]
offset = count + 1

if not os.path.exists('Output'):
    os.mkdir('Output')

# write total dos
totalDos = open('./Output/total_dos.dat', 'w')
totalDos.writelines(dens_of_state)
totalDos.close()

# extract all other dos'
# for i in range(0, num_of_ions):
#     count = offset + number_of_bins
#     current_dens_of_state = lines[offset:count]
#
#     dos_file = open('./Output/dos' + str(i + 1) + '.dat', 'w')
#     dos_file.writelines(current_dens_of_state)
#     dos_file.close()

if not os.path.exists('Output'):
    os.mkdir('Output')

x = []
y = []

matrix = None
### extract Indium dos ###

# for the first 32 dos'
for i in range(0, 32):
    count = offset + number_of_bins
    current_dens_of_state = lines[offset:count]
    offset = count + 1

    num_of_columns = len(current_dens_of_state[0].split())
    matrix = [[0 for y0 in range(number_of_bins)] for y1 in range(num_of_columns)]

    # for all lines in one dos
    for j in range(0, number_of_bins):
        entries = current_dens_of_state[j].split()

        # fill up the x-axis only once
        if i == 0:
            matrix[0][j] = float(entries[0])

        # insert y elements into the matrix k = columns and j = rows, minus 1 because x already read
        for k in range(1, len(entries)):
            matrix[k][j] += float(entries[k])

# Write to files
    dos_file = open('./Output/In_dos' + str(i + 1) + '.dat', 'w')
    dos_file.writelines(current_dens_of_state)
    dos_file.close()

print(x)
# extract sulfur dos
for i in range(0, num_of_ions - 32):
    count = offset + number_of_bins
    current_dens_of_state = lines[offset:count]
    offset = count + 1

# Write to files
    dos_file = open('./Output/S_dos' + str(i + 1) + '.dat', 'w')
    dos_file.writelines(current_dens_of_state)
    dos_file.close()
