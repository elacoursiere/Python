#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      elacoursiere
#
# Created:     13/09/2013
# Copyright:   (c) elacoursiere 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    import ftplib
    host = "ftp.esri.ca"
    user = "queadmin"
    password = "gaspe"
    connect = ftplib.FTP(host,user,password)
    #Changer de repertoire
    connect.cwd("incoming")
    connect.dir()
    connect.ret
    connect.quit()


if __name__ == '__main__':
    main()
