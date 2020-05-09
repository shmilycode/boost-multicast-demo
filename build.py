#!/usr/bin/env python

import sys
import os
import errno
import shutil
import multiprocessing
            
def GetExeSuffix():
    """Returns '' or '.exe' depending on how executables work on this platform."""
    if sys.platform.startswith(('cygwin', 'win')):
        return '.exe'
    return ''            

args = {"folder": "build"}
supported_build_platform = ["osx", "win2017", "android", "ios", "win2015", "hisilicon"]
supported_build_tool = ["ninja", "make"]
supported_build_system = ["windows", "linux", "mac"]
    
if (len(sys.argv) < 3):
    print("useage: build.py [%s] [%s] (%s)" % (",".join(supported_build_platform), ",".join(supported_build_tool), ",".join(supported_build_system)))
    exit(-1)

for parameter in sys.argv:
    if (parameter in supported_build_platform):
        build_platform = parameter
    elif(parameter in supported_build_tool):
        build_tool = parameter        
    elif (parameter in supported_build_system):
        build_system = parameter
    elif("build.py" in parameter):
        pass
    else:
        args["folder"] = parameter

print("Preparing build script for system: %s" % build_platform)

path = os.path.join(os.getcwd(), args["folder"], build_platform)
print(path)

work_counts = str(int(multiprocessing.cpu_count() / 2))
print("work process: ", work_counts)

if (build_tool == 'ninja'):
    os.system("ninja -C %s -j%s" % (path, work_counts))
else:
    os.system("cmake --build %s -- -j%s" % (path, work_counts))

os.system("echo build done.")
'''
if (build_platform == "android" and (build_system == "windows" or build_system == "linux")):
    stripExe = os.environ["NDK_ROOT"] + "/toolchains/arm-linux-androideabi-4.9/prebuilt/%s-x86_64/bin/arm-linux-androideabi-strip" % build_system
    cmdstrip = "%s --strip-all %s/lib/libPeerConnectionSDK.so" % (stripExe, path)
    print(cmdstrip)
    os.system(cmdstrip)
else:
    pass
'''