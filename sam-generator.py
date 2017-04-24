import numpy as np
import sys

f = open("generated-sam-file.bam", 'w')
f.write("@RG\tID:TestReadGroup0\tSM:TestSample0\tPL:ILLUMINA\tLB:TestLibrary0\tPU:TestReadGroup0\n")

if len(sys.argv) < 4:
	print("too few arguments")
	sys.exit()

lines_number = int(sys.argv[1])
N = int(sys.argv[2])
dub_number = int(sys.argv[3])

#lines_number = 10
#N = 100
#dub_number = 3

if dub_number > lines_number / 2:
	print("too many dublicates requested")
	sys.exit()

print(str(sys.argv))

nucl = {0:'A',1:'C',2:'G',3:'T'}
read = ""
flagint = 0
qint = 0

for i in range(lines_number):
	line = []

	if not (dub_number > 0 and i%2 == 1):
		flag = np.random.randint(0,2) == 0
		if i%2 == 0:
			flagint = 20
		else:
			flagint = 4
		if flag:
			qint = 0
		else:
			qint = 255
		read = ""
		for i in range(N):
			read += nucl[np.random.randint(0, 4)]
	else:
		dub_number -= 1

	line.append("TestReadGroup0")
	line.append(flagint)
	line.append("chr1")
	line.append(700)
	line.append(0)
	line.append("*")
	line.append("=")
	line.append(700)
	line.append(qint)
	line.append(read)
	line.append("*")

	for x in line:
		f.write(str(x))
		f.write('\t')

	f.write('\n')

f.close()