from ftplib import FTP
import os
servers = {'sss': {'ip':'192.168.43.160','username':'target','password':'123456' ,'path' :'/home/target/test','package':'testtest.text'},'MNP':{'ip':'192.168.43.160','username':'target','password':'123456' ,'path' :'/home/target/test','package':'testtest.text'},'bulk' : {'ip':'192.168.43.160','username':'target','password':'123456' ,'path' :'/home/target/test','package':'testtest.text'}}

for server in servers :
    print ('intialaizing connection to ' + servers[server]['ip'] + '.....')
    ftp = FTP(servers[server]['ip'])
    ftp.login(servers[server]['username'],servers[server]['password']) 
    print('connected and logged on')
    print('changing working dir ....')
    ftp.cwd(servers[server]['path'])
    filename = servers[server]['package']
    print('start copying process ....')
    with open(filename, "wb") as file:
    # use FTP's RETR command to download the file
        ftp.retrbinary(f"RETR {filename}", file.write)
    print(f'{filename} copied sucessfully ....')
    os.rename(filename, f'/home/hotburger/Test/{filename}')
    ftp.quit()