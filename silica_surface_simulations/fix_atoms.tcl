mol delete all
mol new protein_silica_solvated_0M.psf
mol addfile protein_silica_solvated_0M.pdb
set all [atomselect top all]
set fixatom [atomselect top "chain S"]
$all set beta 0
$fixatom set beta 1
$all writepdb constraint.pdb
mol delete all
exit
