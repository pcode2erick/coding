#!/bin/bash

result=($@)
noOfSuj=$#
score=0
pass='Fail'
grade=(1 2 3 4 5 5s 5ss)
for((i=0;i<$noOfSuj;i++)); do
if [[ ${result[$i]} == ${grade[0]} ]]; then
score=$(($score+1))
elif [[ ${result[$i]} == ${grade[1]} ]]; then
score=$(($score+2))
elif [[ ${result[$i]} == ${grade[2]} ]]; then
score=$(($score+3))
elif [[ ${result[$i]} == ${grade[3]} ]]; then
score=$(($score+4))
elif [[ ${result[$i]} == ${grade[4]} ]]; then
score=$(($score+5))
elif [[ ${result[$i]} == ${grade[5]} ]]; then
score=$(($score+6))
elif [[ ${result[$i]} == ${grade[6]} ]]; then
score=$(($score+7))
fi
done

for((j=0;j<5;j++)); do
pass='Fail'
if [[ $j -le 1 ]]; then
for((k=2;k<7;k++)); do
if [[ ${result[$j]} == ${grade[$k]} ]]; then
pass='Pass'
fi
done
else
for((a=1;a<7;a++)); do
if [[ ${result[$j]} == ${grade[$a]} ]]; then
pass='Pass'
fi
done
fi
if [[ $pass == 'Fail' ]]; then
break
fi
done
echo "$pass : score for $noOfSuj subjects is $score"