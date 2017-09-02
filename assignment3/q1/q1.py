#Question 1 <bridge processing> Zehao Ba <B00732676>
a = open("text result.txt",'wb')
def readFDB():
    file = open("FDB.txt")
    fdb = []
    numberOfPort = file.readline()

    line = file.readline()
    while line:
        line = line.strip('\n')
        t_list = line.split(' ')
        fdb.append(t_list)
        line = file.readline()
    file.close()
    return fdb,numberOfPort

def readTestFile():
    #read the second file
    file = open("FRAME.txt")
    frame = []
    line = file.readline()
    while line:
        line = line.strip("\n")
        t_list = line.split()
        frame.append(t_list)
        line = file.readline()
    file.close()
    return frame
    
def compare(src_1,port_1,src_2,port_2):
    if src_1 == src_2 and port_1 == port_2:
        return True
    return False

def check(fdb,frames,numberOfPort):
    for frame in frames:
        src = frame[0]
        dest = frame[1]
        port = frame[2]
        Discarded= False
        port_process = -1;
        src_match = False
        fdb_update = False
        #print scr,"\t", dest,"\t",port,"\t",
        a.write(src)
        a.write(dest)
        a.write(port+'\n')
        for item in fdb:
            src_1 = item[0]
            port_1 = item[1]
            if (compare(src_1,port_1,src,port)):
                src_match = True
        if (not src_match):
            if (port > numberOfPort):
                Discarded = True
            else:
                fdb.append([src,port])
                a.write( "FDB updated;" +'\n')
                fdb_update = True
        if (Discarded):
            a.write( "Frame Discarded" +'\n')
        for item in fdb:
            src_1 = item[0]
            port_1 = item[1]
            if (compare(src_1,port_1,dest,port)):
                a.write( "Frame Discarded" +'\n')
                Discarded = True
                break;
            if src_1 == dest:
                port_process = port_1

        if (not Discarded):
            if (port_process == -1):
                a.write( "Frame broadcast on all out ports"+'\n')
            else:
                a.write(  "Frame Sent on port"+port_process +'\n')
        if (fdb_update):
            a.write( "Following is updated FDB " +'\n')
            for line in fdb:
                a.write( str(line))
            fdb_update = False


if __name__ == "__main__":    
    fdb,numberOfPort = readFDB()
    frames = readTestFile()
    check(fdb,frames,numberOfPort)
    a.close()
