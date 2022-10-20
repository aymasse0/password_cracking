"""john_restore.py
runs john the ripper on a list of sessions
"""
import os

curr_dir = os.getcwd() + "/" # may need to change this to a \ if windows
john_path = '/username/home/john/' # replace with the proper path
session_name_list = ["crack_1", "crack_6"] # extend this array arbitrarily
hash_file_list = ["crack_1.txt", "crack_6.txt"]
options = " --rules wordlist=mywordlist.txt " # keep the spaces

for session_name, hash_file in session_name_list, hash_file_list:
    # special case, session name is empty
    if session_name != "":
        if os.path.isfile(session_name):
            print("restoring", session_name)
            cmd_str = john_path + "john --restore=" + session_name
        else:
            print("starting", session_name)
            cmd_str = john_path + "john --session=" + session_name + options + hash_file
    else:
        rec_file_name = "john.rec"
        if os.path.isfile(rec_file_name) or os.path.isfile(john_path + rec_file_name): #checks if the recfile is in the current dir or in john's dir
            print("restoring *DEFAULT NAMELESS SESSION*")
            cmd_str = f"{curr_dir}{john_path}john --restore"
        else:
            print("starting *DEFAULT NAMELESS SESSION*")
            cmd_str = f"{curr_dir}{john_path}john {options} {hash_file}"
        rec_file_name = john_path + session_name + ".rec"
        

    stream = os.popen(cmd_str) # users decide what to do with this output