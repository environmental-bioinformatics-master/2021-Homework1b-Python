#!/usr/bin/env python3
import glob
import sys

def reverse_complement(sequence='AATGCTGACTCCTTCGTG'):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} #complement dictionary
    comp_seq = '' # initiate empty string to be added to
    for base in sequence: #loop over input sequence
        comp_seq += complement[base] #write complement string
    rev_comp_seq = comp_seq[::-1] #reverse string
    return(rev_comp_seq)

def read_in_tables(folder='codon-tables/'):
    #read in all codon tables to EITHER a dictionary of dictionaries OR a pandas dataframes
    return()

def six_frame_changetable(sequence='TAAAGGGCTGACTCCTTCGTGTGATTA'):
    ## FILL IN YOUR CODE HERE
    return()

if __name__ == "__main__":
    ## FILL IN YOUR CODE Here
    pass # <-- This is a place holder. 
