#!/bin/bash

input="user.dat"

while IFS=',' read -r username uid gid comment
do
	echo "delete $username"
	userdel -r $username
done < $input
