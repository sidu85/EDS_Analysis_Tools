#!/BIn/bash

TEMP=310
STATES=5

for THISSYSTEM in 1 # s0_1 s0_05 s0_01 s0_005   # optimal # s1 s0_1 s0_05 s0_01 s0_005 # 0_310_1_2 0_310_1_5 0_310_1_10 0_310_1_20 
do
	for s in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
	do

		# ene_ana @topo ../../spc_2.top @library ene_ana_proteinLigand.md++.lib @en_files ../${THISSYSTEM}/otestsystem_tre_1_$f.dat.gz @prop e1 e2 eR diff21  # > ene-ana-${THISSYSTEM}-$f.out
		ene_ana @topo ../../Water_2_Methanol_Sys/run/3H2O_2CH3OH_eds.top @library ene_ana_REEDS.md++.lib  @en_files ../../Water_2_Methanol_Sys/run/long_21s/3H2O_2CH3OH_eds_${s}.tre.gz @prop e1 e2 e3 e4 e5 eR diff21 diff31 diff41 diff51 diff32 diff42 diff52 diff43 diff53 diff54 # > ene-ana-${THISSYSTEM}-$f.out
		#ene_ana @topo ../../spc_2.top @library ene_ana_proteinLigand.md++.lib @en_files ../../run_no_rep/workdir/otestsystem_tre_1.dat @prop e1 e2 eR diff21 > ene-ana-${THISSYSTEM}-$f.out



		#dfmult @stateR eR.dat @endstates e1.dat e2.dat @temp ${TEMP}  > dfmult-${THISSYSTEM}-$s.out
		echo $s >> dfmult_all_diff_all_s.out	
		dfmult @stateR eR.dat @endstates e1.dat e2.dat @temp ${TEMP} > dfmult_all_diff_s_${s}.out
		i=3
		while [ $i -le ${STATES} ]
		do
			j=1 
			while [ $j -lt $i ]
			do
				echo "start dF calc"
				dfmult @stateR eR.dat @endstates e${j}.dat e${i}.dat @temp ${TEMP}  > dfmult_temp.out	
				paste dfmult_all_diff_s_${s}.out dfmult_temp.out > dfmult_paste.out
				mv dfmult_paste.out dfmult_all_diff_s_${s}.out
				#join dfmult_all_diff_s_${s}.out dfmult_temp.out > dfmult_all_diff_s_${s}.out
				(( j++ ))
			done
			(( i++ ))
		done
		cat dfmult_all_diff_s_${s}.out >> dfmult_all_diff_all_s.out

		#  reweight @vr eR.dat @vy e1.dat e2.dat eR.dat @x diff21.dat @temp ${TEMP}

			#reweight @vr eR.dat @vy e1.dat @x diff21.dat @temp ${TEMP} @bounds -800 800 100 > reweight_e1-${THISSYSTEM}-$f.out
			#reweight @vr eR.dat @vy e2.dat @x diff21.dat @temp ${TEMP} @bounds -800 800 100 > reweight_e2-${THISSYSTEM}-$f.out
		#for df in diff21 diff31 diff41 diff51 diff32 diff42 diff52 diff43 diff53 diff54
		#do
			#reweight @vr eR.dat @vy eR.dat @x ${df}.dat @temp ${TEMP} @bounds -800 800 100 > rewei${s}_${df}.out
		#done		
		# xmgrace reweight_e1.out reweight_e2.out
		# xmgrace rw${s}_diff21.out rw${s}_diff31.out rw${s}_diff41.out rw${s}_diff51.out rw${s}_diff32.out rw${s}_diff42.out rw${s}_diff52.out rw{s}_diff43.out rw${s}_diff53.out rw${s}_diff54.out 

		# mv ene-ana-${THISSYSTEM}-$f.out results/res_ene_ana
		# mv dfmult-${THISSYSTEM}-$f.out results/res_dfmult
		#mv reweight_e1-${THISSYSTEM}-$f.out results/res_reweight/t800
		#mv reweight_e2-${THISSYSTEM}-$f.out results/res_reweight/t800
		#mv reweight_eR-${THISSYSTEM}-$f.out results/res_reweight/t800
	done
done
