#!/bin/bash

opt=$1
opt1=$2 

if [ $# -eq  2 ]; then
	if [ $opt == 'test' -a $opt1 == 'aaa' ] || [ $opt == 'aaa' -a $opt1 == 'test' ] ; then		
		echo good
	else
		echo bad
	fi
else 
	echo Input two parameter!! 
fi

