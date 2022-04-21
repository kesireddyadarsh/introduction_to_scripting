#!/bin/bash
clear

<<com
read "Enter your name" name
echo "The name enter is $name"

read -p "Enter your name" name
echo "Entered name is $name"

read -s -p "Enter your name" name
echo "Entered name is $name"

read -t 5 p "Enter your name" name
echo "Entered name is $name"

filename="class_read.txt"

while read line
do
	echo "From txt: $line"
done < $filename

new_file=new_file.txt
ls>$new_file
echo $new_file.txt
com

filename="numbers.txt"
sum=0
while read line
do
	echo $line
	let sum+=$line
done < $filename
echo $sum
echo $sum >> $filename


