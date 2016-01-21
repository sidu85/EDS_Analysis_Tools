#/bin/bash

head -6 ../../run1/repdat_HXE.dat | awk ' BEGIN {OFS="\t"} { print }' > replica_all.dat
tail -n +7 ../../run1/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+0; print } '  >> replica_all.dat
tail -n +7 ../../run2/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+1000; print }' >> replica_all.dat
tail -n +7 ../../run3/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+2000; print }' >> replica_all.dat
tail -n +7 ../../run4/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+3000; print }' >> replica_all.dat
tail -n +7 ../../run5/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+4000; print }' >> replica_all.dat
tail -n +7 ../../run6/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+5000; print }' >> replica_all.dat
tail -n +7 ../../run7/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+6000; print }' >> replica_all.dat
tail -n +7 ../../run8/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+7000; print }' >> replica_all.dat
tail -n +7 ../../run9/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+8000; print }' >> replica_all.dat
tail -n +7 ../../run10/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+9000; print }' >> replica_all.dat
tail -n +7 ../../run11/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+10000; print }' >> replica_all.dat
tail -n +7 ../../run12/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+11000; print }' >> replica_all.dat
tail -n +7 ../../run13/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+12000; print }' >> replica_all.dat
tail -n +7 ../../run14/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+13000; print }' >> replica_all.dat
tail -n +7 ../../run15/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+14000; print }' >> replica_all.dat
tail -n +7 ../../run16/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+15000; print }' >> replica_all.dat
tail -n +7 ../../run17/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+16000; print }' >> replica_all.dat
tail -n +7 ../../run18/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+17000; print }' >> replica_all.dat
tail -n +7 ../../run19/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+18000; print }' >> replica_all.dat
tail -n +7 ../../run20/repdat_HXE.dat |awk ' BEGIN {OFS="\t"} { $3=$3+19000; print }' >> replica_all.dat
