#"source script2.tcl"
resetpsf
package require psfgen
readpsf ../silica_flipped.psf
readpsf ../XXXX_24_autopsf.psf
writepsf protein_silica.psf
resetpsf
exit
