#!/bin/bash
#this is single line comment
clear
#echo "This is to print"
<<com
This is muiltple line
THis is line 2
com
#readonly test_variable="value"
#echo "this is varibale before $test_variable"
#test_variable="something"
#echo "This is new value $test_variable"
cat<<EOT
Multiple lines
EOT

echo $0
echo $1
echo $2
