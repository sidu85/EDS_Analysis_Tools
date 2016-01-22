# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 10:20:04 2015

@author: dsidler
Read in dfmult_all_diff_s_replicaID.out files created with ene_eds.sh
Plot corresponding free energy differences
"""
#%%
import os
import matplotlib.pyplot as plt
import numpy
from scipy.special import comb
from collections import defaultdict
from pathlib import Path

workdir = os.getcwd()
print("cwd =", workdir)
#set parameters to plot delta F
REPNUM=19
STATENUM=5
Sysname="PNMT"
Statename=["lig1","lig4","lig6","lig7","lig10"]

#set paths

#syspath="pnmt/run_epot_offset_opts_no_RF/" #defines which system i.e. where to read and write data.
#syspath="pnmt/run_e_offset_sereina_no_RF/"
syspath="pnmt/run_no_offset_opts_no_RF/"

in_file_dir='/Users/dsidler/Documents/PhD/EDS/Input_Analysis_Tools/Ana_Prog/'+syspath
in_file_name='dfmult_all_diff_all_s.out' 

out_file_dir='/Users/dsidler/Documents/PhD/EDS/Output_Analysis_Tools/Ana_Prog/'+syspath

file_path=os.path.join(in_file_dir,in_file_name)


#output from dfmult program which calculates Free Energy Differences from EDS Simulation

#Read in data from ene_ana_rep_error.dat file for further analysis and plotting
print('Start with reading '+ file_path)

dictinfile={}
try:
    dictinfile[in_file_name] = open(file_path,'r+')
    #in_file=open(in_file_name,'r+') 
except IOError:
    print ("cannot open file",file_path)

#%%
#Idea: store values in list of dictionaries as key value pair with the following keys: "av", "rmsd", "errest"
dFnum=comb(STATENUM, 2, exact=True)#n tief k
dF_ij=numpy.zeros((REPNUM, dFnum))
dF_ij_err=numpy.zeros((REPNUM, dFnum))
ij_comb=defaultdict(list)

#toteneAv=defaultdict(list)
#totene=defaultdict(numpy.array)
for key,file in dictinfile.items():
    s=0
    for line in file:
        line2 = line.strip().strip('\n')
        print(line2)
        line3 = line2.split()
        if (line3[0]=="DF_2_1"):
            statecounter=0
            for i in range(2, (STATENUM+1)):
                for j in range(1, i):
                    dF_ij[s][statecounter]=float(line3[(1+3*statecounter)])
                    dF_ij_err[s][statecounter]=float(line3[(2+3*statecounter)])
                    ij_comb[s].append(str(j)+str(i))
                    statecounter=statecounter+1
            s=s+1
        else:
            pass

#%%
#Plot Figures
#Define some general Img Properties (fontsize etc)
#repID_plot=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
plot_color=["black","blue","green","red","magenta","cyan"]
repID_plot_adjusted=[1]#,5,7,8,9,10]
svalues=[1.0]#,0.18,0.089,0.063,0.044, 0.031]

transition=[14, 16, 46, 17, 47, 67, 110, 410, 610, 710]
#xpos=numpy.arange(len(transition))
xpos=numpy.arange(0.5,10,1)
print("xpos ", xpos)
print(repID_plot_adjusted)


#Plot figure of Free Energy
fig1=plt.figure(figsize=(10,6),dpi=300)

cID=0
for rID in repID_plot_adjusted:
    plt.bar(xpos,dF_ij[rID],yerr=dF_ij_err[rID],ecolor='r',tick_label=transition)#plot(dF_ij[rID], color=plot_color[cID], linewidth=1, linestyle="-",marker="+",markersize=10,mew=9,label=("s="+str(svalues[cID])))
    cID=cID+1
    plt.show()
#print(dF_ij)
#print(dF_ij_err)
#print(ij_comb)
#plt.ylim(dF_ij[svalues].min(),dF_ij[svalues].max())
#plt.legend(loc="upper left")
#plt.ylabel("$\Delta F_{ij} $", fontsize=16)
#plt.xlabel("State ij", fontsize=16)
#plt.title("Free Energy Difference for 5 different pnmt inhibitors\n ", fontsize=20)
out_file_path1=os.path.join(out_file_dir,"pmnt.eps")
fig1.savefig(out_file_path1)

##%%
##Plot figure of Free Energy error
#fig2=plt.figure(figsize=(10,6),dpi=300)
#cID=0
#for rID in repID_plot_adjusted:
#    plt.plot(dF_ij_err[rID], color=plot_color[cID], linewidth=1, linestyle="-",marker="+",markersize=10,mew=9,label=("s="+str(svalues[cID])))
#    cID=cID+1
#    plt.show
##print(dF_ij)
##print(dF_ij_err)
##print(ij_comb)
#plt.ylim(dF_ij_err.min(),dF_ij_err.max()*1.2)
#plt.legend(loc="upper left")
#plt.ylabel("Error $\Delta F_{ij} $", fontsize=16)
#plt.xlabel("Endstate Transition ij", fontsize=16)
#plt.title("Free Energy Difference Errors for all Endstate Transitions \n for changing smoothing Parameter s", fontsize=20)
#out_file_path2=os.path.join(out_file_dir,"dF_s_ID_err.eps")
#fig2.savefig(out_file_path2)

#%%




