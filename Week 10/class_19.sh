#!/bin/bash
clear

<<com
for var in 1 2 3 4 5
do 
	echo $var
done


for i in $( seq 5)
do
	echo $i
done


for (( i=1; i<=5; i++ ))
do
	echo $i
done

sum=0
for i in $( seq 10 )
do 
	if [[ $(( i%2 )) -eq 0 ]]
	then
		let sum+=i
		echo $sum
	fi
done
echo $sum
com
select var in "class_1" "class_2" "class_3" "exit"
do
	case $var
	in
	"class_1")
		echo "Test 1"
	;;
	"exit")
		break
	;;
	esac
done









