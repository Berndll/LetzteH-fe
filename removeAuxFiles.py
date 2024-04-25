
import os, sys

for subdir, dirs, files in os.walk('.'):
    if subdir.find('.git') == -1:
        print(subdir)
        try:
            os.remove(subdir + "/main.aux")
        except:
            continue
    try:
        os.remove('main.aux')
    except:
        continue
