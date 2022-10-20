#!/bin/sh

program="JOHN" # could be cat
if [[ "${program}" == "JOHN" ]]; then
    crack_dir="YOUR_PATH_HERE/john/run"
    crack_program=${crack_dir}'/john'
    ext='rec'
    restore_option="--restore="${session_name}
else
    crack_dir="YOUR_PATH_HERE/hashcat-6.2.6"
    crack_program=${crack_dir}'/hashcat'
    ext='restore'
    restore_option="--restore --session "${session_name}
    module load cuda/11.0
fi

export PATH=$crack_dir:$PATH
file1=${crack_dir}'/'${session_name}'.'$ext

if [ -f $file1 ] || [ -f $file2 ]; then
    echo "restoring" $session_name
    $crack_program $restore_option
else
    $crack_program 
fi