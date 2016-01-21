# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 10:20:04 2015

@author: dsidler
Read in dfmult_all_diff_s_replicaID.out files created with ene_eds.sh
Plot corresponding free energy differences
"""

import os
import matplotlib.pyplot as plt
import numpy
from scipy.special import comb
from collections import defaultdict

workdir = os.getcwd()

#set parameters to plot delta F
REPNUM=21
STATENUM=5
in_file_name='dfmult_all_diff_all_s.out'

#Read in data from ene_ana_rep_error.dat file for further analysis and plotting
print('Start with reading '+in_file_name)

dictinfile={}
try:
    dictinfile[in_file_name] = open(in_file_name,'r+')
    #in_file=open(in_file_name,'r+') 
except IOError:
    print ("cannot open file",in_file_name)


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


#Plot Figures
#Define some general Img Properties (fontsize etc)
repID_plot=[1,6,8,9,10,11]
plot_color=["black","blue","green","red","magenta","cyan"]
repID_plot_adjusted=[0,5,7,8,9,10]
svalues=[1.0,0.18,0.089,0.063,0.044, 0.031]
print(repID_plot_adjusted)


#Plot figure of Free Energy
fig1=plt.figure(figsize=(10,6),dpi=300)
cID=0
for rID in repID_plot_adjusted:
    plt.plot(dF_ij[rID], color=plot_color[cID], linewidth=1, linestyle="-",marker="+",markersize=10,mew=9,label=("s="+str(svalues[cID])))
    cID=cID+1
    plt.show
#print(dF_ij)
#print(dF_ij_err)
#print(ij_comb)
plt.ylim(-50,30)
plt.legend(loc="upper left")
plt.ylabel("$\Delta F_{ij} $", fontsize=16)
plt.xlabel("Endstate Transition ij", fontsize=16)
plt.title("Free Energy Difference for all Endstate Transitions \n for changing smoothing Parameter s", fontsize=20)
fig1.savefig("dF_s_ID.eps")

#Plot figure of Free Energy error
fig2=plt.figure(figsize=(10,6),dpi=300)
cID=0
for rID in repID_plot_adjusted:
    plt.plot(dF_ij_err[rID], color=plot_color[cID], linewidth=1, linestyle="-",marker="+",markersize=10,mew=9,label=("s="+str(svalues[cID])))
    cID=cID+1
    plt.show
print(dF_ij)
print(dF_ij_err)
#print(ij_comb)
plt.ylim(dF_ij_err.min(),dF_ij_err.max()*1.2)
plt.legend(loc="upper left")
plt.ylabel("Error $\Delta F_{ij} $", fontsize=16)
plt.xlabel("Endstate Transition ij", fontsize=16)
plt.title("Free Energy Difference Errors for all Endstate Transitions \n for changing smoothing Parameter s", fontsize=20)
fig2.savefig("dF_s_ID_err.eps")

##Calc Err(f2) from dvdl and totene
#errf2calc=numpy.sqrt(numpy.power(Tmin*1/Ttr*dvdl["tn"][:][2],2)+numpy.power(Tmin/(numpy.power(Ttr,2))*totene["tn"][:][2]*dTtr,2)) 
#print("error of f2calc: "+str(errf2calc))
#print("Correlation between errf2calc and errf2measure :" + str(numpy.corrcoef(errf2calc,dfnew["tn"][:][2])))
##Plot fig of Free Energy Errors
#fig2=plt.figure(figsize=(10,6),dpi=300)
#plt.plot(l,dfnew["tn"][:][2], color="red", linewidth=2.5, linestyle="-", label="$\mathrm{Err}(\\langle f_2\\rangle(\\tau_{\mathrm{run}}=1\mathrm{ns}))_{\mathrm{measure}}$")
#plt.plot(l,errf2calc, color="black", linewidth=2.5, linestyle="-", label="$\mathrm{Err}(\\langle f_2\\rangle(\\tau_{\mathrm{run}}=1\mathrm{ns}))_{\mathrm{calc}}$")
#plt.plot(l,dvdl["tn"][:][2], color="blue", linewidth=2.5, linestyle="-", label="$\mathrm{Err} (\\langle \partial H/\partial \lambda\\rangle(\\tau_{\mathrm{run}}=1\mathrm{ns}))_{\mathrm{measure}}$")
#plt.plot(l,totene["tn"][:][2], color="green", linewidth=2.5, linestyle="-", label="$\mathrm{Err} (\\langle H\\rangle(\\tau_{\mathrm{run}}=1\mathrm{ns}))_{\mathrm{measure}}$")
#plt.plot(l,dfnew["tl"][:][2], color="red", linewidth=2.5, linestyle="-.", label="$\mathrm{Err}(\\langle f_2\\rangle(\\tau_{\mathrm{run}}=2\mathrm{ns}))_{\mathrm{measure}}$")
##plt.plot(l,errf2calc, color="black", linewidth=2.5, linestyle="-", label="$\mathrm{Err}(f_2(\wedge ))_{\mathrm{calc}}$")
#plt.plot(l,dvdl["tl"][:][2], color="blue", linewidth=2.5, linestyle="-.", label="$\mathrm{Err} (\\langle \partial H/\partial \lambda\\rangle(\\tau_{\mathrm{run}}=2\mathrm{ns}))_{\mathrm{measure}}$")
#plt.plot(l,totene["tl"][:][2], color="green", linewidth=2.5, linestyle="-.", label="$\mathrm{Err} (\\langle H\\rangle(\\tau_{\mathrm{run}}=2\mathrm{ns}))_{\mathrm{measure}}$")
##plt.plot(l,dvdl["cn"][:][2], color="orange", linewidth=2.5, linestyle="-", label="$\mathrm{Err} (\partial H/\partial \lambda)(-)_{\mathrm{measure}}$")
##plt.plot(l,dvdl["cl"][:][2], color="orange", linewidth=2.5, linestyle="-.", label="$\mathrm{Err} (\partial H/\partial \lambda)(-)_{\mathrm{measure}}$")
#plt.xlim(l.min(),l.max())
#plt.ylim(0,max([dfnew["tn"][:][2].max(),dvdl["tn"][:][2].max(),totene["tn"][:][2].max()])*1.6)
#plt.legend(loc="upper left",ncol=2)
#plt.xlabel("$\lambda $", fontsize=16)
#plt.ylabel("Error [kJ/mol]", fontsize=16)
#plt.title("Error of Free Energy Integration Points for Different $\lambda$ Values and Triangular Path", fontsize=14)
#plt
#fig2.savefig("Err_fren.eps")
#
##Some error Analysis
#dl=0.05
#interrorf2measure=numpy.sqrt(sum(dl*numpy.power(dfnew["tn"][:][2],2)))
##interrorf2test=numpy.sqrt(sum(dl/2.0*numpy.power(numpy.append(dfnew[:][2],dfnew[:][2]),2)))
#interrorf2calc=numpy.sqrt(sum(dl*numpy.power(errf2calc,2)))
#interrorf1tri=numpy.sqrt(sum(dl*numpy.power(dvdl["tn"][:][2],2)))
#print(dfnew["tn"][:][2])
#print(numpy.append(dfnew["tn"][:][2],dfnew["tn"][:][2]))
#print("Error of Int(f2measure): "+str(interrorf2measure))
#print("Error of Int(f2calc): "+str(interrorf2calc))
#print("Error of Int(dvdl): "+str(interrorf1tri))
#
#
##mean error with respect to trun
#fig4=plt.figure(figsize=(10,6),dpi=300)
#trun=numpy.array([250,500,1000,2000])
#print("trun: " + str(trun))
#merdfnew=[numpy.nanmean(dfnew["tvs"][:][2]),numpy.nanmean(dfnew["ts"][:][2]),numpy.nanmean(dfnew["tn"][:][2]),numpy.nanmean(dfnew["tl"][:][2])]
#merdvdl=[numpy.nanmean(dvdl["tvs"][:][2]),numpy.nanmean(dvdl["ts"][:][2]),numpy.nanmean(dvdl["tn"][:][2]),numpy.nanmean(dvdl["tl"][:][2])]
#mertotene=[numpy.nanmean(totene["tvs"][:][2]),numpy.nanmean(totene["ts"][:][2]),numpy.nanmean(totene["tn"][:][2]),numpy.nanmean(totene["tl"][:][2])]
#merdvdlconst=[numpy.nanmean(dvdl["cvs"][:][2]),numpy.nanmean(dvdl["cs"][:][2]),numpy.nanmean(dvdl["cn"][:][2]),numpy.nanmean(dvdl["cl"][:][2])]
#
#serdfnew=[numpy.nanstd(dfnew["tvs"][:][2]),numpy.nanstd(dfnew["ts"][:][2]),numpy.nanstd(dfnew["tn"][:][2]),numpy.nanstd(dfnew["tl"][:][2])]
#serdvdl=[numpy.nanstd(dvdl["tvs"][:][2]),numpy.nanstd(dvdl["ts"][:][2]),numpy.nanstd(dvdl["tn"][:][2]),numpy.nanstd(dvdl["tl"][:][2])]
#sertotene=[numpy.nanstd(totene["tvs"][:][2]),numpy.nanstd(totene["ts"][:][2]),numpy.nanstd(totene["tn"][:][2]),numpy.nanstd(totene["tl"][:][2])]
#serdvdlconst=[numpy.nanstd(dvdl["cvs"][:][2]),numpy.nanstd(dvdl["cs"][:][2]),numpy.nanstd(dvdl["cn"][:][2]),numpy.nanstd(dvdl["cl"][:][2])]
#print(merdfnew)
#print(numpy.isfinite(merdfnew))
#print(merdvdl)
#print(mertotene)
#print(dfnew["tvs"][:][2])
#plt.plot(trun,merdfnew, color="red", linewidth=2.5, linestyle="-", label="$\overline{\mathrm{Err}}(f_2(\wedge ))_{\mathrm{measure}}(\\tau_{\mathrm{run}})$")
#plt.plot(trun,merdvdl, color="blue", linewidth=2.5, linestyle="-", label="$\overline{\mathrm{Err}}(\partial H/\partial \lambda(\wedge ))_{\mathrm{measure}}(\\tau_{\mathrm{run}})$")
#plt.plot(trun,mertotene, color="green", linewidth=2.5, linestyle="-", label="$\overline{\mathrm{Err}}(H(\wedge ))_{\mathrm{measure}}(\\tau_{\mathrm{run}})$")
#plt.plot(trun,merdvdlconst, color="orange", linewidth=2.5, linestyle="-", label="$\overline{\mathrm{Err}}(\partial H/\partial \lambda(-))_{\mathrm{measure}}(\\tau_{\mathrm{run}})$")
#plt.errorbar(trun,merdfnew,yerr=serdfnew,color="red")
#plt.errorbar(trun,merdvdl,yerr=serdvdl,color="blue")
#plt.errorbar(trun,mertotene,yerr=sertotene,color="green")
#plt.errorbar(trun,merdvdlconst,yerr=serdvdlconst,color="orange")
#plt.xlim(0,trun.max()*1.1)
#plt.ylim(0,max(mertotene)*1.1)
#plt.legend(loc="upper right")
#plt.xlabel("$ \\tau_{\mathrm{run}}$[ps]", fontsize=16)
#plt.ylabel("Error [kJ/mol]", fontsize=16)
#plt.title("Mean Error of Free Energy Points for Different $\\tau_{\mathrm{run}}$ Values", fontsize=14)
#plt
#fig4.savefig("Mean_Err_Trun.eps")
#
##error with respecet to temperature (vorsicht: an unterschiedlichen lambda punkten gemessen.)
#fig5=plt.figure(figsize=(10,6),dpi=300)
#
##plt.plot(Ttr,dvdl["tl"][:][2], color="red", linewidth=2.5, linestyle="-", label="$\mathrm{Mean_Err}(f_2(\wedge ))_{\mathrm{measure}}(\tau_{run})$")
###plt.plot(trun,merdvdl, color="blue", linewidth=2.5, linestyle="-", label="$\mathrm{Mean_Err}(\partial H/\partial \lambda(\wedge ))_{\mathrm{measure}}(\tau_{run})$")
###plt.plot(trun,mertotene, color="green", linewidth=2.5, linestyle="-", label="$\mathrm{Mean_Err}(H(\wedge ))_{\mathrm{measure}}(\tau_{run})$")
###plt.plot(trun,merdvdlconst, color="orange", linewidth=2.5, linestyle="-", label="$\mathrm{Mean_Err}(\partial H/\partial \lambda(-))_{\mathrm{measure}}(\tau_{run})$")
###plt.errorbar(trun,merdfnew,yerr=serdfnew,color="red")
###plt.errorbar(trun,merdvdl,yerr=serdvdl,color="blue")
###plt.errorbar(trun,mertotene,yerr=sertotene,color="green")
###plt.errorbar(trun,merdvdlconst,yerr=serdvdlconst,color="orange")
##plt.xlim(Ttr.min()*0.8,Ttr.max()*1.2)
##plt.ylim(0,max(dvdl["tl"][:][2])*1.1)
##plt.legend(loc="upper right")
##plt.xlabel("$T $", fontsize=16)
##plt.ylabel("Error", fontsize=16)
##plt.title("Mean Error of $\partial H/\partial \lambda$ for Different Temperatures T (attention: measured at different ", fontsize=14)
##plt
##fig5.savefig("Err_Temp.eps")
##plt.plot()
#
##Free Energy
#fig3=plt.figure(figsize=(10,6),dpi=300)
#plt.plot(l,dfnew["tn"][:][0], color="red", linewidth=2.5, linestyle="-", label="$\mu (f_2(\wedge ))_{\mathrm{measure}}$")
#plt.xlim(l.min(),l.max())
#plt.ylim(dfnew["tn"][:][0].min()*1.1,dfnew["tn"][:][0].max()*1.1)
#plt.legend(loc="upper left")
#plt.xlabel("$\lambda $", fontsize=16)
#plt.ylabel("Mean Free Energy", fontsize=16)
#ax = plt.gca()  # gca stands for 'get current axis'
##ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.spines['bottom'].set_position(('data',0))
#plt.title("Free Energy Average for Different $\lambda$ Values", fontsize=14)
#fig3.savefig("Mu_fren.eps")
#
##estimate if it might make sense to estimate dvdl(T)=dvdl(Tdiff)*deltaT + const
#fig6=plt.figure(figsize=(10,6),dpi=300)
#plt.plot(l,dvdl["tn"][:][0], color="blue", linewidth=3, linestyle="-", label="$\\langle\partial H/\partial \lambda(\wedge )\\rangle$")
#plt.plot(l,dvdl["cn"][:][0], color="orange", linewidth=3, linestyle="-", label="$\\langle\partial H/\partial \lambda(-)\\rangle$")
#plt.plot(l,dvdlextrapol["tn"][:][0], color="black", linewidth=3, linestyle="-", label="$\\langle\partial H/\partial \lambda(-)\\rangle$")
#plt.errorbar(l,dvdl["cn"][:][0],yerr=dvdl["cn"][:][2], color="orange")
#plt.errorbar(l,dvdl["tn"][:][0],yerr=dvdl["tn"][:][2], color="blue")
#plt.errorbar(l,dvdl["cn"][:][0],yerr=dfnew["tn"][:][2], color="red")
#plt.xlim(0,1)
#plt.legend(loc="upper right")
#plt.xlabel("$\lambda $", fontsize=16)
#plt.ylabel("$\\langle\partial H/\partial \lambda\\rangle$ [kJ/mol]", fontsize=16)
#plt.title("Comparison of $\partial H/\partial \lambda$ between triangular and const temperature path ", fontsize=14)
#plt
#fig6.savefig("dvdl_const_vs_tri.eps")
