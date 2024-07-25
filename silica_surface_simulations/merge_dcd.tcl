mol new protein_silica_solvated_0M.psf
mol addfile nvt1.dcd waitfor all
mol addfile nvt2.dcd waitfor all
mol addfile nvt3.dcd waitfor all
mol addfile nvt4.dcd waitfor all
mol addfile nvt5.dcd waitfor all
mol addfile nvt6.dcd waitfor all
mol addfile nvt7.dcd waitfor all
mol addfile nvt8.dcd waitfor all
mol addfile nvt9.dcd waitfor all
mol addfile nvt10.dcd waitfor all
mol addfile nvt11.dcd waitfor all
mol addfile nvt12.dcd waitfor all
mol addfile nvt13.dcd waitfor all
animate write dcd nvt.dcd
exit
