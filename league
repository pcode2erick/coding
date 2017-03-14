#!/bin/bash

list=($@)
fname=${!#}
no=$(($#-1))
totalm=$((2*no-2))
declare -a teamlist
declare -a gf
declare -a ga
declare -a gd
declare -a point
declare -a win=(0 0 0 0 0)
declare -a draw=(0 0 0 0 0)
declare -a lose=(0 0 0 0 0)

#score=(`echo $value | grep -o -E '[0-9]+'`)
#teamlist=(`echo $value | grep -o -E '[a-z]+'`)
#size=${#teamlist[*]}
for i in {1..10}; do
value=(`cat $fname$i.txt`)

for((j=0;j<(${#value[*]});j++)); do
if [[ $((no%2)) -eq 1 ]]; then   #odd number of teams
for ((k=0;k<no;k++)); do
if [[ ${value[$j]} == ${list[$k]} ]]; then
gf[$k]=$((gf[$k]+value[$((j+1))]))
if [[ ( $((j%4)) -eq 0 ) && ( ${value[$((j+1))]} -lt  ${value[$((j+3))]}) ]]; then  #home team lose
ga[$k]=$((ga[$k]+value[$((j+3))]))
lose[$k]=$((lose[$k]+1))
elif [[ ( $((j%4)) -eq 2 ) && ( ${value[$((j+1))]} -lt  ${value[$((j-1))]}) ]]; then  #away team lose
ga[$k]=$((ga[$k]+value[$((j-1))]))
lose[$k]=$((lose[$k]+1))
elif [[ ( $((j%4)) -eq 0 ) && ( ${value[$((j+1))]} -gt  ${value[$((j+3))]}) ]]; then  #home team win
ga[$k]=$((ga[$k]+value[$((j+3))]))
win[$k]=$((win[$k]+1))
elif [[ ( $((j%4)) -eq 2 ) && ( ${value[$((j+1))]} -gt  ${value[$((j-1))]}) ]]; then  #away team win
ga[$k]=$((ga[$k]+value[$((j-1))]))
win[$k]=$((win[$k]+1))
elif [[ ( $((j%4)) -eq 0 ) && ( ${value[$((j+1))]} -eq  ${value[$((j+3))]}) ]]; then  #home team draw
draw[$k]=$((draw[$k]+1))
elif [[ ( $((j%4)) -eq 2 ) && ( ${value[$((j+1))]} -eq  ${value[$((j-1))]}) ]]; then  #away team draw
draw[$k]=$((draw[$k]+1))
fi
fi
done 
fi
done
done

for((z=0;z<no;z++)); do
gd[$z]=$((gf[$z]-ga[$z])) point[$z]=$((win[$z]*3+draw[$z]))
done

printf "Rank\tTeam\tP\tW\tD\tL\tGF\tGA\tGD\tPoints\n"| expand -t 7
for ((j=0;j<no;j++)); do
mcount=`grep ${list[$j]} round*.txt | wc -l`
if [[ $mcount -eq $totalm ]]; then
printf "${list[$j]}\t$mcount\t${win[$j]}\t${draw[$j]}\t${lose[$j]}\t${gf[$j]}\t${ga[$j]}\t${gd[$j]}\t${point[$j]}\n"
else
printf "${list[$j]}\t$totalm($mcount)\t${win[$j]}\t$((${draw[$j]}+$totalm-$mcount))(${draw[$j]})\t${lose[$j]}\t${gf[$j]}\t${ga[$j]}\t${gd[$j]}\t$((${point[$j]}+$totalm-$mcount))(${point[$j]})\n"
fi
done | sort -nrk9 | cat -n | expand -t 7
