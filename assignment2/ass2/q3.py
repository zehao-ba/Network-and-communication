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
reminder = int(msg1,2) % int(ref,2)

if (reminder == 0):
    transmit = msg
else:
    reminder_str = bin(reminder)[2:]
    print reminder_str
    transmit = str(msg) +str(reminder_str)
print ("The transmission number is: ",transmit)
    
    
    
    
    
    
