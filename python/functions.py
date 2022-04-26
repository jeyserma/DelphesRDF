
import sys, os, glob, shutil, json, math, re, random
import ROOT

def findFiles(basedir, regex = ""):

    rootFiles = ROOT.vector('string')()
    
    if ".root" in basedir: 
    
        rootFiles.push_back(basedir)
        return rootFiles
    
    if regex != "":
    
        if basedir[-1] == "/": basedir = basedir[:-1]
        regex = basedir + "/" + regex

    rootFiles = ROOT.vector('string')()
    for root, directories, filenames in os.walk(basedir):
    
        for f in filenames:
       
            filePath = os.path.join(os.path.abspath(root), f)
            if "failed/" in filePath: continue
            if "log/" in filePath: continue
            if regex == "" or fnmatch.fnmatch(filePath, regex): rootFiles.push_back(filePath)
            
    return rootFiles