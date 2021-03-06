#!/bin/bash
# Downloads files from http://ipsc.jrc.ec.europa.eu/index.php?id=197#c2744
set -e

FILES[0]="http://langtech.jrc.ec.europa.eu/Resources/DGT-TM-2007/Volume_1.zip"
FILES[1]="http://langtech.jrc.ec.europa.eu/Resources/DGT-TM-2007/Volume_2.zip"
FILES[2]="http://langtech.jrc.ec.europa.eu/Resources/DGT-TM-2007/Volume_3.zip"
FILES[3]="http://langtech.jrc.ec.europa.eu/Resources/DGT-TM-2007/Volume_4.zip"
FILES[4]="http://langtech.jrc.ec.europa.eu/Resources/DGT-TM-2007/Volume_5.zip"
FILES[5]="http://langtech.jrc.ec.europa.eu/Resources/DGT-TM-2007/Volume_6.zip"
FILES[6]="http://langtech.jrc.ec.europa.eu/Resources/DGT-TM-2007/Volume_7.zip"
FILES[7]="http://langtech.jrc.ec.europa.eu/Resources/DGT-TM-2007/Volume_8.zip"
FILES[8]="http://langtech.jrc.ec.europa.eu/Resources/DGT-TM-2007/Volume_9.zip"
FILES[9]="http://langtech.jrc.ec.europa.eu/Resources/DGT-TM-2007/Volume_10.zip"
FILES[10]="http://langtech.jrc.ec.europa.eu/Resources/DGT-TM-2007/Volume_11.zip"
FILES[11]="http://langtech.jrc.ec.europa.eu/Resources/DGT-TM-2007/Volume_12.zip"
FILES[12]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2004_1.zip"
FILES[13]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2004_2.zip"
FILES[14]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2005_1.zip"
FILES[15]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2005_2.zip"
FILES[16]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2005_3.zip"
FILES[17]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2006_1.zip"
FILES[18]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2006_2.zip"
FILES[19]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2006_3.zip"
FILES[20]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2006_4.zip"
FILES[21]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2006_5.zip"
FILES[22]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2007_1.zip"
FILES[23]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2007_2.zip"
FILES[24]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2007_3.zip"
FILES[25]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2008_1.zip"
FILES[26]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2008_2.zip"
FILES[27]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2008_3.zip"
FILES[28]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2008_4.zip"
FILES[29]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2009_1.zip"
FILES[30]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2009_2.zip"
FILES[31]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2009_3.zip"
FILES[32]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2009_4.zip"
FILES[33]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2010_1.zip"
FILES[34]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2010_2.zip"
FILES[35]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2010_3.zip"
FILES[36]="http://optima.jrc.it/Resources/DGT-TM-2011/Vol_2010_4.zip"
FILES[37]="http://optima.jrc.it/Resources/DGT-TM-2012/Vol_2011_1.zip"
FILES[38]="http://optima.jrc.it/Resources/DGT-TM-2012/Vol_2011_2.zip"
FILES[39]="http://optima.jrc.it/Resources/DGT-TM-2012/Vol_2011_3.zip"
FILES[40]="http://optima.jrc.it/Resources/DGT-TM-2012/Vol_2011_4.zip"
 
for f in "${FILES[@]}"
do
	wget -Nc $f
done;

md5sum -c hashes.md5
