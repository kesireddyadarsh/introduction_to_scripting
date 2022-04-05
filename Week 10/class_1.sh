#!/bin/bash
clear


var_1=0
var_2=10
sum=0
until [ $var_1 -eq $var_2 ]
do 
	if [ $var_1 -le 8 ]
	then
		echo $var_1
	else
		break
	fi

	let "var_1++"
done

