#-------------------------------------------------------------------------------
# Name:        download par http module
# Purpose:
#
# Author:      elacoursiere
#
# Created:     13/09/2013
# Copyright:   (c) elacoursiere 2013
# Licence:     enjoy
#-------------------------------------------------------------------------------

def main(chemins):
    import urllib2,os

    for chemin in chemins:
        connection = urllib2.urlopen(chemin)
        fichier = chemin.split('/')[-1]
        output = open(os.path.join("C:\\Quebec\\zip",fichier),'wb')
        output.write(connection.read())
        output.close()

if __name__ == '__main__':
    main(["http://depot.ville.montreal.qc.ca/polygones-arrondissements/data.zip"])
