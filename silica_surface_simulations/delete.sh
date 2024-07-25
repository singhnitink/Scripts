#!/bin/bash
for a in K1L1 K2L2 K3L3 K4L4 K6L6 K12L12
do

cd ./${a}
rm nvt1.dcd nvt2.dcd nvt3.dcd nvt4.dcd nvt5.dcd nvt6.dcd nvt7.dcd nvt8.dcd nvt9.dcd nvt10.dcd nvt11.dcd nvt12.dcd nvt13.dcd

cd ../
done
