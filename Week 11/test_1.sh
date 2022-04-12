#!/bin/bash
clear
<<com
TESTA[0]="Remo"
TESTA[1]="Range"
echo ${#TESTA}

echo ${TESTA[@]}

TESTA[2]=fifth
echo ${TESTA[@]}
TESTA[2]=newFifth
echo ${TESTA[@]}


temp_val=(This is to test the array)
echo ${temp_val[*]}
echo "Temp without all"
echo ${temp_val}

check_v="ThisISthestring"
temp_val[2]="${temp_val[0]:1:3}"
echo ${temp_val[2]}

array_len=(fint the length of the array)
echo ${#array_len}
echo ${#array_len[3]}


array_len=("array" "with" "9848" "78985")
#echo ${array_len[@]/*[a-zA-Z]*/}

for var_1 in ${array_len[@]}
do
	echo $var_1
done


#unset array_len[0]
#echo ${array_len[@]}
com

num=(1 2 3 4)
#for loop to do summation of the elements
sum=0
for n in ${num[@]}
do
	let sum+=n
done
echo $sum





