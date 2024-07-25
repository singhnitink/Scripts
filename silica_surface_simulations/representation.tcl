mol new protein_silica.psf
mol addfile protein_silica.pdb
set molid [molinfo top get id]
rotate x by -90
color Display Background white
display projection Orthographic
axes location Off
mol modselect 0 $molid resname LEU
mol modstyle 0 $molid NewCartoon 0.300000 10.000000 4.100000 0
mol modcolor 0 $molid ColorID 1
mol addrep $molid
mol modselect 0 $molid resname LYS
mol modstyle 0 $molid NewCartoon 0.300000 10.000000 4.100000 0
mol modcolor 0 $molid ColorID 7
mol addrep $molid
mol modselect 1 $molid all not(protein or water or ion)
mol modstyle 1 $molid VDW 1.000000 12.000000
mol modcolor 1 $molid Name
render Tachyon vmdscene.dat "/usr/local/lib/vmd/tachyon_LINUXAMD64" -aasamples 12 %s -format bmp -o %s.bmp
