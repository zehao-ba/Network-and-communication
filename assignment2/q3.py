msg = raw_input("Enter the message: ")
#msg = int (msg)
#msg = bin (msg)[2:]
ref = raw_input("Enter the common reference number: ")
#ref = int(ref)
#ref = bin(ref)[2:]
print ("Message is: ",msg)
print ("Common reference number is: ",ref)
zero = ""
count = 0
while (len(zero) < len(ref) - 1):
    zero = zero + '0'
    count = count +1
while (len(zero) == len(ref) - 1):
    count = 0
    break
msg1 = msg + zero
print ("message prime is: ",msg1)
msg1 = list(msg1)
ref = list(ref)
print count
for i in range(len(msg1)-3):
    if msg1[i] == '1':
        for j in range(len(ref)):
            
            msg1[i+j] = str((int(msg1[i+j])+int(ref[j]))%2)
result = '' .join(msg1[-len(zero):])
print msg+result
'''
if (reminder == 0):
    transmit = msg
else:
    reminder_str = bin(reminder)[2:]
    print reminder_str
    transmit = str(msg) +str(reminder_str)
print ("The transmission number is: ",transmit)
'''
    
    
    
    
    
