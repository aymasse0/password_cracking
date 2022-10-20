"""restore.py
runs john the ripper or hashcat on a list of sessions
restores them if they already exist
requires python 3.6+
"""
import os
from typing import List

program="JOHN"
curr_dir = os.getcwd() + "/" # may need to change this to a \ if windows
crack_dir = '/username/home/crack' # replace with the proper path
session_name_list = ["crack_1", "crack_6"] # extend this array arbitrarily
hash_file_list = ["crack_1.txt", "crack_6.txt"]
options_list = [" --rules wordlist=mywordlist.txt ",
                " -m 500 -a 3 ?a?a?a?a "] # keep the spaces

def restore_or_run(session_name_list: List[str], hash_file_list: List[str],
    options_list: List[str]) -> List[os._wrap_close]:
    stream_list = []
    for session_name, hash_file, options in \
            session_name_list, hash_file_list, options_list:

        # john and hashcat specific
        if program == "JOHN":
            crack_dir="YOUR_PATH_HERE/john/run"
            crack_program=f"{crack_dir}/john"
            ext='rec'
            restore_option=f"--restore={session_name}"
        else:
            crack_dir="YOUR_PATH_HERE/hashcat-V.E.R"
            crack_program=f"{crack_dir}/hashcat"
            ext='restore'
            restore_option="--restore --session {session_name}"

        rec_file_name = crack_dir + session_name + "." + ext
        if session_name != "":
            if os.path.isfile("session_name"):
                print("restoring", session_name)
                cmd_str = f"{crack_program} {restore_option}"
            else:
                print("starting", session_name)
                cmd_str = f"{crack_program} --session=" + session_name + options + hash_file
        else:
            # special case, session name is empty
            rec_file_name = "john.rec" #checks if the default recfile is in the current dir or in john's dir
            if os.path.isfile(rec_file_name) or os.path.isfile(crack_dir + rec_file_name): 
                print("restoring *DEFAULT NAMELESS SESSION*")
                cmd_str = f"{crack_program} --restore"
            else:
                print("starting *DEFAULT NAMELESS SESSION*")
                cmd_str = f"{crack_program} {options} {hash_file}"

        stream_list.append(os.popen(cmd_str))
    
    return stream_list
    
if __name__ == "__main__":
    # users decide what to do with this output
    stream_lsit = restore_or_run(session_name_list, hash_file_list, options_list)
    
