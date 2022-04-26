#!/bin/bash

# get ROOT
source /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.24.02/x86_64-centos7-gcc48-opt/bin/thisroot.sh


export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:Delphes-3.5.0/
export ROOT_INCLUDE_PATH=Delphes-3.5.0/external/:$ROOT_INCLUDE_PATH
export PYTHONPATH=$PYTHONPATH:$ROOT_INCLUDE_PATH