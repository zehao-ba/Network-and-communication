#Question 1 <bridge processing> Zehao Ba <B00732676>

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
        print src,"\t",dest,"\t",port,"\t",
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
                print "FDB updated;",
                fdb_update = True
        if (Discarded):
            print "Frame Discarded"
        for item in fdb:
            src_1 = item[0]
            port_1 = item[1]
            if (compare(src_1,port_1,dest,port)):
                print "Frame Discarded"
                Discarded = True
                break;
            if src_1 == dest:
                port_process = port_1

        if (not Discarded):
            if (port_process == -1):
                print "Frame broadcast on all out ports"
            else:
                print  "Frame Sent on port",port_process
        if (fdb_update):
            print "Following is updated FDB "
            for line in fdb:
                print line
            fdb_update = False        

if __name__ == "__main__":
    fdb,numberOfPort = readFDB()
    frames = readTestFile()
    check(fdb,frames,numberOfPort)

