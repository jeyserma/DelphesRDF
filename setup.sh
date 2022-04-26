#!/bin/bash

# get ROOT
source /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.24.02/x86_64-centos7-gcc48-opt/bin/thisroot.sh


# get Pythia and compile 
wget https://pythia.org/download/pythia82/pythia8235.tgz
tar xzvf pythia8235.tgz
cd pythia8235
./configure --prefix=$(pwd)
export PYTHIA8=$(pwd)
make -j 4
make install
cd ../
rm pythia8235.tgz

# get Delphes and compile
wget http://cp3.irmp.ucl.ac.be/downloads/Delphes-3.5.0.tar.gz
tar -zxf Delphes-3.5.0.tar.gz
cd Delphes-3.5.0
make -j 4
make HAS_PYTHIA8=true
cd ../
rm Delphes-3.5.0.tar.gz

