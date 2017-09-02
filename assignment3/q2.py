#Question 2 <Packet routing at a router> Zehao Ba <B00732676>

def readTable():
	file = open("RoutingTable.txt")
	table = []

	line = file.readline()
	while line:
		line = line.strip('\n')
		t_list = line.split(' ')
		table.append(t_list)
		line = file.readline()
	file.close()
	return table

def readPackets():
	file = open("Packet.txt")
	packet = []

	line = file.readline()
	while line:
		line = line.strip('\n')
		#print line
		packet.append(line)
		line = file.readline()

	file.close()
	#print packet
	return packet
	
def ANDComputation(mask_1, dest_1):
	#split mask_1 to list, convert items to binary
	address1 = []
	address1 = mask_1.split('.')
	mask =[]
	for num in address1:
		address1_int = int(num)
#		address1_bin = bin(int(num))
#		address1_bin = address1_bin[2:]
#		address1_bin = address1_bin.zfill(7)
		mask.append(address1_int)
	print "mask is", mask



	#split dest_1 to list, convert items to binary

	address2 = dest_1.split('.')
	destination = []

	for num in address2:
		address2_int = int(num)
#		address2_bin = bin(int(num))
#		address2_bin = address2_bin[2:]
#		address2_bin = address2_bin.zfill(7)
		destination.append(address2_int)
	print "destination is", destination

	#AND computation, convert to decimal
	result = []

	for i in range (0,4):
		a = mask[i]
		b = destination[i]
		res = a&b 
		#print "And computation", res
		result.append(res)
	print "And computation is", result
	return result

def compare(dest_1,dest_2):
	dest1_list = dest_1.split('.')

	for i in range(0,4):
		if dest1_list[i] != str(dest_2[i]):
			return False
	return True


def check(table, packets):
	for packet in packets:
		for item in table:
			mask = item[0]
			dest = item[1]
			hop = item[2]
			interface = item[4]
			dest_match = False
		#	print "MASK", mask
			result = ANDComputation(mask, packet)
		#	print "this is the result", result
		#	print "this is the PACKET", packet
			if(compare(dest, result)):
				dest_match = True
				print "Packet with destination address",dest, "will be forwarded to",hop, "out on interface",interface
			else:
				continue

	if(not dest_match):
		print "No destination matched. Please try other packet."
			

if __name__ == "__main__":
	table = readTable()
	packet = readPackets()
	check(table, packet)




