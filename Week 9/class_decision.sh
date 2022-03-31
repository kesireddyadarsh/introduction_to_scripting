#!/bin/bash
clear
var_1=10
var_2=5
<<com
var_3=$((var_1 +var_2))

echo "$var_3"

RANDOM=$$
echo $(($RANDOM%10))

echo $((++var_1))


if [ $var_1 == $var_2 ]
then
	echo "Both are equal"
else
	echo "Both are not equal"
fi



var_name="test"
if [ -z "$var_name" ]
then
echo "whateever you want to say"
else 
echo "string has something in it"
fi
com


var_test=20 
#ranges 1 to 10, 11 to 20, more

if [[ $var_test=>1 && $var_test<=10 ]]
then 
echo "Between 1 to 10"
elif [[ $var_test=>11 && $var_test<=20 ]]
then 
echo "Between 11 to 20"
elif [ $var_test>20 ]
then
echo "greater than 20"
else
echo "less than 1"
fi
