#!/bin/bash
clear


function_name (){
	echo "Print this to the terminal"
}

#function_name

function_passing_parameters(){
	a=$1
	b=$2
	let  c=a+b
	echo $c
}

#function_passing_parameters 1 2

function_return (){
	a=$1
	b=$2
	let c=a+b
	return $c
}

function_return 2 3
print_1=$?
echo $print_1

<<com
values=($(seq 1 10))
sum_values=0
sum(){
	let sum_value+=$1
}


for val in ${values[*]}
do
	sum val
	echo $sum_value
done


first_fun(){
	echo "This is first function"
	second_fun
}

second_fun(){
	echo "This is second function"
}

first_fun


factorial (){
	if(($1==0))
	then
		echo 1
	else
		last=$(factorial $(( $1 - 1 )))
		echo $(( $1*last ))
	fi
		
}

#factorial 5

com
