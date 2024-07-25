#!/bin/bash
#K1L1 K2L2 K3L3 K4L4 K6L6 K12L12
for a in K2L2 K3L3 K4L4 K6L6 K12L12
do
  mkdir ${a}
  cd ./${a}
  cp ../packmol.inp .
  cp ../*.tcl .
  sed -i "s/XXXX/${a}/g" packmol.inp
  packmol < packmol.inp
  sed -i "s/XXXX/${a}/g" merging_psf.tcl
  vmd -dispdev text -e merging_psf.tcl
  vmd -dispdev text -e solvation.tcl
  vmd -dispdev text -e fix_atoms.tcl
  cp ../*.namd .
  cd ..
done
