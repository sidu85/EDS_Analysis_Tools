# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:32:35 2015

@author: dsidler
"""
import os
import sys
import time
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from collections import defaultdict


class main:
#run simulation + set all all RE_EDS Sim parameters and the 
# necessary analyses.
    


class Algo:
#   stores different multidimensional RE_EDS parameter update schemes
  
    
    def __init__(Num_Rmax,N,in_root_path,qstart_path):
        #global variables    
        E_start  #assume equal for all s values. not clear if it works  
        s_vec=[]
        N_States=N
        #ref_init_param #contains initial conditions which are similar for each s i.e. definis Reference State Hamiltonian(s,Ei) 
        Rep_sim_list=[Gromos_Sim] #contains Simulations
        Rep_data_list=[Step_Data] #contains Sim Data i.e. all Results for each Replica
               
        
        #guess E_start q_start for different states
        E_start=np.zeros(shape(N_states),double)
        Sim_E_init_vec=[]#contains simulations for initialisation
        running_sim_id=[]#contains id of still running simulations
        for E_id in xrange(0,N_states-1):
            Sim_E_init_vec.append(Gromos_Sim_oneState(qstart_path,in_root_path+"/E_init/")) #Gromos_Sim_oneState derived from Gromos_Sim class
            running_sim_id.append(E_id)            
            try: 
                Sim_E_init_vec.start_sim()
                break
            except 
            { 
                print("Couldn't start Sim_E_init with E_id= "+E_id)   
                abort()
            }
        while !running_sim_id.empty():
            for E_id in running_sim_id:
                if (Sim_E_init[E_id].finished()):
                    running_sim_id.pop(E_id) #remove finished sim from queue
                    E_start[E_id]=Sim_E_init[E_id].get_E_av()   
                    print("E_start= " E_start[E_id]" successfully found for E_id= "+E_id)
            time.sleep(5) #sleep time that I don't constatly loop
        print("all E_start successfully found")
        
        #set up initial cond for different s     
        init=0
        while init <= 1:
            din=1.0/(Num_Rmax+1)
            init=init + din
            s=ln(init)
            s_vec.append(s)
            init_path=in_root_path +"/s_"+ str(s)           
            Tot_data_matrix.append(Step_data(s,E_start))#initialize data in a list
            Tot_sim_matrix.append(Gromos_Sim(s,q_start,E_start,init_path))#set_up simulation with proper starting configurations
        print("s_vec="+s_vec)
        
        
    def noit_alg(ref_init_param):
        #use only initial guess for E_start (no itteration) -> show that <V1>!=<VR(q1)> so it is better to use itteration
        
    def para_alg(ref_init_param,dE,lim,E_R_target):
        #Parallel initialisation of replicas (i.e. now information of other replicas used)
        #faster but not clear if it works for complex potential landscapes
        
        #start initial simulations with coordinates q_start
        rep_id=0        
        #running_rep=[s_vec.size()][N_states] 
        for s_id in xrange(0,s_vec.size()-1):
            for q_id in xrange(0,N_states-1):
                Tot_sim_matrix[s_id][q_id]=Rep_sim_list[s_id].start(q_id,E_start)
                Tot_sim_matrix[s_id][q_id].new_result=true #have to distinguish between pausing simulation, where I've to update results or not
                #running_rep[s_id][q_id]= true
        
        num_run_sim=np.ones(s_vec.size(),dtype=int)*N_states       
        print("N_states * num_repl Simulations started i.e. "+num_run_sim+" simulations started")
  
        while np.array_equal(np.greater(num_run_sim,0),np.ones(s_vec.size(),dtype=bool)):#loop until no running sim
            for s_id in xrange(0,s_vec.size()-1): #loop over s
                for q_id in xrange(0,N_states-1): #loop over start coord.-> posibility to reduce #sim for one s value
                    if(Tot_sim_matrix[s_id][q_id].finished() && Tot_sim_matrix[s_id][q_id].new_result)
                       #update results if one sim newly terminated
                        Tot_sim_matrix[s_id][q_id].new_result= false
                        E_r_old[s_id][q_id]=Tot_data_matrix[s_id].E_R[q_id] 
                        E_r_res[s_id][q_id]=Tot_sim_matrix[s_id][q_id].get_E_av(q_id,lim)#only consider values in state q_id and in lim specified proportion...!
                        Tot_sim_matrix[s_id][q_id].update_step(Tot_data_matrix[s_id]) #adds simulation results to step_data in tot_data_ve
                        num_run_sim[s_id]=num_run_sim[s_id]-1
                        print("Simulation terminated. s_id= "+s_id+" q_id= "+q_id )  
                conv_vec_bool=np.array_equal(np.absolute(E_r_res-E_R_target)<dE,np.ones(N_states,dtype=bool))
                if(conv_vec_bool): #
                #check if E_R found for one given s value. finished...
                    print("Simulation with for s_id="s_id" terminated. Alle E_R found")
                    print("E_R_res: " E_r_res[s_id])
                    ugly if replicas do not terminate at the same time
                else:
                #restart sim with updated E_R
                    if(num_run_sim[s_id]==0):
                    #all new E_r found restart
                       for q_id in xrange(0,N_states-1):
                           E_r_new=E_r_old[s_id]*conv_vec_bool+E_r_res[s_id]*np.logical_not(conv_vec_bool) #use old E values as input if within errorbars -> only update values outside errorbars
                           Tot_sim_matrix[s_id][q_id]=Tot_sim_matrix[s_id].start(q_id,E_r_new)
                           Tot_sim_matrix[s_id][q_id].new_result= true
                           num_run_sim[s_id]++
                    else:
                    #wait
            time.sleep(5)
       return {s, E_r_res}
                
        
        

        
    
#        
#        #check until all simulations have terminated
#        num_run_sim=np.ones(shape=(s_vec.size()),int)*N_states
#        print("N_states * num_repl Simulations started to identify bad states i.e. "+num_run_sim+" simulations started")
#        while num_run_sim??? > 0:
#            for s_id in xrange(0,s_vec.size()-1):
#                Tot_data_vec[s_id].append(Step_data(...))
#                for q_id in xrange(0,N_states-1):
#                    if(Tot_sim_matrix[s_id][q_id].finished())
#                        #assume measure transition probabilties only starting from q_id !!!!
#                        Tot_sim_matrix[s_id][q_id].update_step(Tot_data_vec[s_id]) #adds in simulation results to step_data in tot_data_vec
#                        num_run_sim[s_id]--
#                        print("Simulation terminated. s_id= "+s_id+" q_id= "+q_id )      
#            time.sleep(5)
#        
#        #find orthogonal simulation setup i.e. remove bad states...(assume optimal choice of Ei has no influence on bad states!)
#        #i.e. find q_id_basis_vec    ?????????????????
#        q_basis=[]
#        for item in xrange(0,s_vec.size()-1):
#            q_basis.append([1:N_states])
#        
#        #symmetrize bad(s)_ij because wrong energy offsets, one cannot assume that bad(s)_ij=bad(s)_ji
#        # However (to be proved) ?????????????
#        
#        for s_id in xrange(0,s_vec.size()-1): #for each replica
#            for q_id in xrange(0,N_states-1): #for each state
#                for j in xrange(q_id+1,N_states-1): #assume symmetric bad_ij for / not efficient algorithm...
#                    if(Tot_data_vec[s_id].bad[q_id][j]) #vorsicht some strong assumptions contained i.e. only form q_id (symmetrical bad matrix etc. think about it!!)
#                        q_basis[s_id].remove(j) #fix me: vorsicht multiple removals moeglich....
#                        print("remove bad stat: s_id="+s_id+" q_id="+q_id+"j="j)
#                        
#         print("all bad states removed")              
#        
#        #start algorithm on orthogonal setup
#        
#        for s_id in xrange(0,s_vec.size()-1):
#            for q_id in q_basis[s_id]:
#                Tot_sim_matrix[s_id][q_id].start(q_id,Tot_data_vec[s_id].E_R)
#                
#        #1)wait until all sim for one s have found E_i
#        #2)start new sim for one s ->1 or 3)if E_i(n+1)-E_i(n)<Delta
#        #3)start config found
#                
#        # loop until all Ei found 
#        for s_id in xrang(0,s_Vec.siz()-1):
#            
#        
#        
#        
#        
#        
#            for q in  
#            while !running_rep.empty     
#                s_id=get_next_fin_sim(Rep_sim_list)
#                for rep in Rep_list:
                
                
    def get_next_fin_sim(sim_vec):
        
        
        
    def ser_alg_bottom_up():
        #serial initialisation of replicas (beginning with a low s_start value)
    
    def ser_alg_top_down():
        #serial initialisation of replicas (beginning with a high s_start=1? value)
    
    
    
class Rep_data:

#    Stores all relevant values for a given yet to be specified 
#    s value i.e. one replica for later analysis
       
    def __init__(s_actual,N_states,init_path,):
        Gromos_com(N_states,init_path) G_com # necessary to set up communication...
        G_com.      
        s=s_actual
        sl=defaultdict(Step_data(N_states)) #step list containig all itteration steps
        
    
    

class Step_data:

#    Stores all relevant values of one itteration step for a 
#    specific replica for later analysis
    def __init__(N): 
        E_R=np.zeros(shape=(N),double)
        Ntrans_ij=np.zeros(shape=(N,N),double)#messe wie viele uebergaenge von i->j auftretten waehrend sim
        V_ij_equal=np.zeros(shape=(N,N),double)#messe ob Vi und Vj gleich sind bei gleichen Koordinaten, wenn ja i_j in bad_ij
        bad_ij=np.zeros(shape=(N,N),double) #tree means minimum spanning tree is stored in NxN Matrix
        good_ij=np.zeros(shape=(N,N),double)
        no_ij=np.zeros(shape=(N,N),double)
        itter= ittern_in   
        bad_tree=np.ones(shape=(N,N)) #probably not symmetric if Eij wrongly set!
        good_tree=np.zeros(shape=(N,N))# not symmetric if Eij wrongly set (during itteration)!
        no_vec=np.zeros(shape=(N))
        E_R=np.zeros(shape=(N,N))
        deltaV_ji=np.zeros(shape=(N,N)) #evtl. nicht notwendig?
        r_start=r_old # idea: alias for start coordinates (correct mapping in Gromos_com implementiert)
        N_i=np.zeros(shape=(N)) #count how often state i was visited
        N_trans_ij=np.zeros(shape=(N,N)) #count how often transition from i to j occured and visa versa (not symmetric!!!)-> necessary to calculate minimum spanning tree!
        MV_ij = np.zeros(shape=(N)) # measure how good coord i matches to j -> bad!                                  
    
    def find_min_tree():
        
    
 class Run_time_Prediction:
#   using a model of the transition probabilities based on measurements during the initialisation of all replicas,
#   one tries to predict the necessary run time       
        
    

class Gromos_Sim:
#    offers tools to communicate with gromos i.e. shell (set up sim,
#    run and read in values for further use for parameter update )

    def __init__(N,path,set_thresholds):
        #set_thresholds contains cutoffs, e.g. how to distinguish between state i and j
        
    def start_sim(param_vec):
        
    def finished(): #returns true if sim terminated
    
    def get_E_av(state=N_states, limit={0.0,1.0}):
    #returns ensemble average, where state defines which states should only be considered for the average calculation.
    #default: state=N_states means all reached states are considered for average
    #for the average calculation all values within the limit are considered
    #default:means all values are considered, wheras {0,0.1} means only the 10% lowest energy values are considerd
    #limit="ln" means exp(<ln(V)>) is returned
            
    def data_2_gromos():
        
    def goromos_2_data():
        
    def update_step(Step_data): #adds in simulation results to step_data (simulation(s,qi) can update all transition information i->j)

class Result_analysis:
#    offers methods to analyse RE_EDS algorithm specific results