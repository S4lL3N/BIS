from paramiko import SSHClient, AutoAddPolicy

def ssh_connect():
    '''
    connecting to linux server and rename the files.
    '''
    client = SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect('avery.nc.rod', username='root', password='aver763')
    print("connected")


    stdin, stdout, stderr = client.exec_command('ls /img/deedhold/re/000065/')
    #000001.003 -- we only what to change .001 suffix just make them hidden by renameing with a '.'
    #ls -ld /img/deedhold/re/000065/.*
    return client

client = ssh_connect()
stdin, stdout, stderr = client.exec_command('ls /img/deedhold/re/000065/')
files = stdout.readlines()
logfile = open("AverySSHLog.txt","w+")
client.close()
count = 0
count2 = 0
for file in files:
    count += 1
    #print("Count: "+ str(count) + " " + str(file))
    lastChar = file[len(file) - 2]
    nextToLastChar = file[len(file) - 3]
    if (lastChar ==  '1' and nextToLastChar != '0') or lastChar != '1':
        #print("last:"+ str(lastChar))
        #print("Next to last:"+ str(nextToLastChar))
        source = "/img/deedhold/re/000065/" + file.strip('\n')
        dest = "/img/deedhold/re/000065/." + file.strip('\n')
        command = " imgmv /img/deedhold/re/000065/" + file.strip("\n") + " /img/deedhold/re/000065/." + file.strip("\n") + "\n"
        #print(command)
        #print("Count: "+ str(count2) + " " + str(file))
        logfile.write(command)
    
logfile.close()




