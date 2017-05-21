import os
import subprocess
ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).communicate()[0]


processes = ps.split('\n')

# this specifies the number of splits, so the splitted lines
# will have (nfields+1) elements
nfields = len(processes[0].split()) - 1
for row in processes[1:]:
    print row.split(None, nfields)