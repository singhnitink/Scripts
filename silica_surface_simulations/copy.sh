#!/bin/bash
for b in 2 3
do
for a in 1 2 3 4 5 6 7 8 9 10
do
cp job_1-${a}.sh job_${b}-${a}.sh

done
done
