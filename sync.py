import os
import sys
import subprocess as sub
from subprocess import Popen, PIPE
ret=sub.Popen("hg pull ssh://hg@bitbucket.org/Mythreyip/test", shell=True)
if ret.wait()!=0:
   print("pull failed x265 repo")
else:
    ret=sub.Popen("hg push ssh://hg@bitbucket.org/Mythreyip/test ", shell=True)
    if ret.wait()!=0:
        print("update failed git repo")
    else:
        print("updated at tip at git")

