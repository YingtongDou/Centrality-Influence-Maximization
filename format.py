

# open file
fin = open("MIT.txt", "r")
fout = open("out.txt", "w")
# header line
header = fin.readline() 
fout.write(header)
# data lines
for line in fin:
    dat_in = line.split()
    dat_in[0] = str(int(dat_in[0]) - 1)
    dat_in[1] = str(int(dat_in[1]) - 1)
    dat_out = " ".join(dat_in)
    fout.write(dat_out+"\n")
# close file   
fin.close()
fout.close()