#Qusetion 2 <Bit Stuffing> Zehao Ba <B00732676>
#read file and convert text to binary 
file = open("Note.txt")
result=""
while 1:
    line = file.readline()
    if not line:
        break
    for letter in line:
        ascii=ord(letter)
        binary=bin(ascii)[2:]
        result=result+binary.zfill(7) #to make sure each binary has seven bits

#add "0" after every five consecutive "1" and save the binary values to "bit stream.txt"        
count = 0
finalresult = ""
for num in result:
    if num == '1':
        count = count + 1
    if num == '0':
        count = 0
    finalresult = finalresult + num
    if count == 5:
        count = 0
        finalresult = finalresult + '0'
f = open("bit stream.txt",'wb')
f.write(finalresult)
f.close()

#delete the "0" we added before 
file = open("bit stream.txt", 'rb')
iniresult= ""
count = 0
while 1:
    line = file.readline()
    if not line:
        break
    else:
        for num in line:
            if num == '1':
                count = count + 1
            if count == 5 and num == '0': #delete 0;
                count = 0
                continue
            if num == '0':
                count = 0
            iniresult= iniresult + num

#for every seven bits binary, convert it to text and save those text to "text file.txt"
num7=""
final_result =""
for num in iniresult:
        num7 = num7+num
        if (len(num7)==7):
            dec_num = int(num7,2)
            num7 = str(unichr(dec_num))
            final_result = final_result + num7
            num7=""
#print final_result
a = open("text file.txt",'wb')
a.write(final_result)
a.close()
    
