#!/bin/sh
cat $1 | sed 's/  */,/g' | sed 's/,//' | sed 's/*//g' | sed 's/Provisional//g' | sed 's/---/0/g' > $2

