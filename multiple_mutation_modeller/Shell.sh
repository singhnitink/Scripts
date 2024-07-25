#!/bin/bash
#conda activate
i=1
j=0
#ASP 9 73 79 149 198 214 230
#GLU 26 39 41 52 158 164 166 204
for a in 9 73 79 149 198 214 230
do
if [ $i == 1 ]
then
  echo $i
python modeller_mutate.py AF-P42212-F1-model_v2 ${a} ASP A > mutate${i}.log
mv AF-P42212-F1-model_v2ASP${a}.pdb mutation_${i}.pdb
else
python modeller_mutate.py mutation_${j} ${a} ASP A > mutate${i}.log
mv mutation_${j}ASP${a}.pdb mutation_${i}.pdb
  echo $i
fi
i=`expr $i + 1`
j=`expr $i - 1`
echo $i $a $j
done

#ASP 9 73 79 149 198 214 230
#GLU 26 39 41 52 158 164 166 204
for a in 26 39 41 52 158 164 166 204
do
if [ $i == 8 ]
then
  echo $i
python modeller_mutate.py mutation_${j} ${a} GLU A > mutate${i}.log
mv mutation_${j}GLU${a}.pdb mutation_${i}.pdb
else
python modeller_mutate.py mutation_${j} ${a} GLU A > mutate${i}.log
mv mutation_${j}GLU${a}.pdb mutation_${i}.pdb
  echo $i
fi
i=`expr $i + 1`
j=`expr $i - 1`
echo $i $a $j
done

echo "checkfile ${j}"
