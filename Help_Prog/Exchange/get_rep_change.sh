#!/usr/bin/python

import os, sys

#Path to repdat.dat
os.system("cp ../../0_310_0_10/repdat.dat .")
#os.system("cp ../../1_340_0_20_reverse_pert/repdat.dat .")

#execute python script rep_ana_mpi.py to extract replica exchange scheme and store it into rep_change.out
#os.system("./gather_replicas.sh")
os.system("./rep_ana_mpi.py repdat.dat")

#find out which frames are needed
f = open("rep_change.out","r")
reading = False

for line in f:
  if line.startswith('#replica exchange'):
    replica = line.strip().split()[-1]
    min, max = 1.0, 0.0
    reading = True
  elif line.startswith('&'):
    walking = max - min
    print 'replica {0} walks {1}'.format(replica,walking)
    reading = False
  elif reading:
    T, lam = line.split()
    if float(lam) < min:
      min = float(lam)
    if float(lam) > max:
      max = float(lam)

f.close()

#print xmgrace RE-scheme
os.system("xmgrace rep_change.out")
