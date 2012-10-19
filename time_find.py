#!/usr/bin/python2.7

"""
Author : Pratyush Nigam

To run, enter the following command -

./time_find.py compile-method filename.c

where compile-method = gcc or llvm

"""


flags=["-falign-arrays", "-falign-functions[=n]", "-falign-jumps[=n]", "-falign-labels[=n]", "-falign-loops[=n]", "-fassociative-math", "-fauto-inc-dec", "-fbranch-probabilities", "-fbranch-target-load-optimize", "-fbranch-target-load-optimize2", "-fbtr-bb-exclusive", "-fcaller-saves", "-fcheck-data-deps", "-fconserve-stack", "-fcprop-registers", "-fcrossjumping", "-fcse-follow-jumps", "-fcse-skip-blocks", "-fcx-fortran-rules", "-fcx-limited-range", "-fdata-sections", "-fdce", "-fdce", "-fdelayed-branch", "-fdelete-null-pointer-checks", "-fdse", "-fdse", "-fearly-inlining", "-fexpensive-optimizations", "-ffast-math", "-ffinite-math-only", "-ffloat-store", "-fforward-propagate", "-ffunction-sections", "-fgcse", "-fgcse-after-reload", "-fgcse-las", "-fgcse-lm", "-fgcse-sm", "-fif-conversion", "-fif-conversion2", "-findirect-inlining", "-finline-functions", "-finline-functions-called-once", "-finline-limit=n", "-finline-small-functions", "-fipa-cp", "-fipa-cp-clone", "-fipa-matrix-reorg", "-fipa-pta", "-fipa-pure-const", "-fipa-reference", "-fipa-struct-reorg", "-fipa-type-escape", "-fira-algorithm=algorithm", "-fira-region=region", "-fira-coalesce", "-fno-ira-share-save-slots", "-fno-ira-share-spill-slots", "-fira-verbose=n", "-fivopts", "-fkeep-inline-functions", "-fkeep-static-consts", "-floop-block", "-floop-interchange", "-floop-strip-mine", "-fmerge-all-constants", "-fmerge-constants", "-fmodulo-sched", "-fmodulo-sched-allow-regmoves", "-fmove-loop-invariants", "-fmudflap", "-fmudflapir", "-fmudflapth", "-fno-branch-count-reg", "-fno-default-inline", "-fno-defer-pop", "-fno-function-cse", "-fno-guess-branch-probability", "-fno-inline", "-fno-math-errno", "-fno-peephole", "-fno-peephole2", "-fno-sched-interblock", "-fno-sched-spec", "-fno-signed-zeros", "-fno-toplevel-reorder", "-fno-trapping-math", "-fno-zero-initialized-in-bss", "-fomit-frame-pointer", "-foptimize-register-move", "-foptimize-sibling-calls", "-fpeel-loops", "-fpredictive-commoning", "-fprefetch-loop-arrays", "-fprofile-correction", "-fprofile-dir=path", "-fprofile-generate", "-fprofile-generate=path", "-fprofile-use", "-fprofile-use=path", "-fprofile-values", "-freciprocal-math", "-fregmove", "-frename-registers", "-freorder-blocks", "-freorder-blocks-and-partition", "-freorder-functions -frerun-cse-after-loop", "-freschedule-modulo-scheduled-loops", "-frounding-math", "-frtl-abstract-sequences", "-fsched2-use-superblocks", "-fsched2-use-traces", "-fsched-spec-load", "-fsched-spec-load-dangerous", "-fsched-stalled-insns-dep[=n]", "-fsched-stalled-insns[=n]", "-fschedule-insns", "-fschedule-insns2", "-fsection-anchors", "-fsee", "-fselective-scheduling", "-fselective-scheduling2", "-fsel-sched-pipelining", "-fsel-sched-pipelining-outer-loops", "-fsignaling-nans", "-fsingle-precision-constant", "-fsplit-ivs-in-unroller", "-fsplit-wide-types", "-fstack-protector", "-fstack-protector-all", "-fstrict-aliasing", "-fstrict-overflow", "-fthread-jumps", "-ftracer", "-ftree-builtin-call-dce", "-ftree-ccp", "-ftree-ch", "-ftree-copy-prop", "-ftree-copyrename", "-ftree-dce", "-ftree-dominator-opts", "-ftree-dse", "-ftree-fre", "-ftree-loop-im", "-ftree-loop-distribution", "-ftree-loop-ivcanon", "-ftree-loop-linear", "-ftree-loop-optimize", "-ftree-parallelize-loops=n", "-ftree-pre", "-ftree-reassoc", "-ftree-sink", "-ftree-sra", "-ftree-switch-conversion", "-ftree-ter", "-ftree-vect-loop-version", "-ftree-vectorize", "-ftree-vrp", "-funit-at-a-time", "-funroll-all-loops", "-funroll-loops", "-funsafe-loop-optimizations", "-funsafe-math-optimizations", "-funswitch-loops", "-fvariable-expansion-in-unroller", "-fvect-cost-model", "-fvpt", "-fweb", "-fwhole-program", "-fuse-ld", "--param name=value"];

flags_O1=["-falign-loops", "-fargument-alias", "-fasynchronous-unwind-tables", "-fbranch-count-reg", "-fcommon", "-fcprop-registers", "-fdce", "-fdefer-pop", "-fdse", "-fearly-inlining", "-fgcse-lm", "-fguess-branch-probability", "-fif-conversion", "-fif-conversion2", "-finline-functions-called-once", "-fipa-pure-const", "-fipa-reference", "-fivopts", "-fjump-tables", "-fmath-errno", "-fmerge-constants", "-fmove-loop-invariants", "-fomit-frame-pointer", "-fpeephole", "-frename-registers", "-fsched-interblock", "-fsched-spec", "-fsched-stalled-insns-dep", "-fsigned-zeros", "-fsplit-ivs-in-unroller", "-fsplit-wide-types", "-ftoplevel-reorder", "-ftrapping-math", "-ftree-ccp", "-ftree-ch", "-ftree-copy-prop", "-ftree-copyrename", "-ftree-cselim", "-ftree-dce", "-ftree-dominator-opts", "-ftree-dse", "-ftree-fre", "-ftree-loop-im", "-ftree-loop-ivcanon", "-ftree-loop-optimize", "-ftree-reassoc", "-ftree-scev-cprop", "-ftree-sink", "-ftree-sra", "-ftree-ter", "-ftree-vect-loop-version", "-funit-at-a-time", "-fvar-tracking", "-fvect-cost-model", "-fweb"];

flags_O2=["-falign-functions", "-falign-jumps", "-falign-labels", "-fcaller-saves", "-fcrossjumping", "-fcse-follow-jumps", "-fdelete-null-pointer-checks", "-fexpensive-optimizations", "-fgcse", "-fgcse-lm", "-finline-small-functions", "-findirect-inlining", "-foptimize-sibling-calls", "-fpeephole2", "-fregmove", "-freorder-blocks", "-freorder-functions", "-frerun-cse-after-loop", "-fsched-interblock", "-fsched-spec", "-fschedule-insns", "-fschedule-insns2", "-fstrict-aliasing", "-fstrict-overflow", "-ftree-switch-conversion", "-ftree-pre", "-ftree-vrp"];

flags_O3=["-finline-functions-called-once", "-funswitch-loops", "-fpredictive-commoning", "-fgcse-after-reload", "-ftree-vectorize", "-fvect-cost-model", "-ftree-pre-partial-partial", "-fipa-cp-clone", "-fpredictive-commoning"];

flags_llvm=["-adce", "-always-inline", "-argpromotion", "-codegenprepare", "-constmerge", "-constprop", "-correlated-propagation", "-dce", "-deadargelim", "-die", "-dse", "-globaldce", "-globalopt", "-gvn", "-indvars", "-inline", "-instcombine", "-internalize", "-ipconstprop", "-ipsccp", "-jump-threading", "-licm", "-loop-deletion", "-loop-reduce", "-loop-rotate", "-loop-unroll", "-loop-unswitch", "-loops", "-loweratomic", "-lowerinvoke", "-lowerswitch", "-memcpyopt", "-mergefunc", "-mergereturn", "-partial-inliner", "-prune-eh", "-reassociate", "-scalarrepl", "-sccp", "-simplify-libcalls", "-simplifycfg", "-sink", "-tailcallelim", "-no-aa", "-tbaa", "-basicaa", "-basiccg", "-functionattrs", "-domtree", "-lazy-value-info", "-lcssa", "-scalar-evolution", "-memdep", "-strip-dead-prototypes"];

import os
import subprocess
import sys
import random

iteration_count = 5;
sampling_count = 20;

f = open("time_comparison.txt","w+")

def find_time_llvm(set_of_flags):
	
	obj = sys.argv[2]
	objf = obj[:-2] + ".o"
	sf = obj[:-2] + ".s"
	
	for i in set_of_flags:
		if(i==set_of_flags[0]):
			stfl = i + " "
		else:
			stfl = stfl + i + " "
	args = "opt " + stfl +objf + " -o " + objf
	arg = args.split(" ")
	a = subprocess.check_call(arg)
	
	args = "llc " + objf + " -o " + sf
	arg = args.split(" ")
	a = subprocess.check_call(arg)
	
	args = "clang " + sf + " -lm"
	arg = args.split(" ")
	a = subprocess.check_call(arg)
		
	b = subprocess.check_output(["time","./a.out"],stderr = subprocess.STDOUT)
	t = float(b[0:4])

	return t

def check_pass(set_of_flags):
	
	obj = sys.argv[2]
	objf = obj[:-2] + ".o"
	sf = obj[:-2] + ".s"
	for i in set_of_flags:
		if(i==set_of_flags[0]):
			stfl = i + " "
		else:
			stfl = stfl + i + " "
	args = "opt " + stfl +objf + " -o " + objf
	arg = args.split(" ")
	a = subprocess.call(arg)
	return a

def find_time_gcc(a):
	args = ["gcc","-lm"]
	for i in a:
		args.append(i)
	args.append(sys.argv[2])
	ai = subprocess.check_call(args)
	b = subprocess.check_output(["time","./a.out"],stderr = subprocess.STDOUT)
	t = float(b[0:4])
	return t

def main():
	if sys.argv[1] == "gcc":
		#Applying Hill Climbing Technique		
		
		iterations = iteration_count;
		sample_count = sampling_count;

		flags_set = flags_O1+flags_O2+flags_O3

		s_flags = random.sample(flags_set,sample_count)
		f.write("----------------------------------------------------------------------------\n")
		print s_flags
		while(iterations):
			flg = 0
			time = find_time_gcc(s_flags)
			for i in xrange(0, sample_count):
				fl = s_flags[0:i]
				fl.append(random.choice(flags_O2+flags_O3))
				fl = fl + s_flags[i+1:sample_count]
				#print fl
				time_new = find_time_gcc(fl)
				#print str(i) + " " + str(time_new)
				f.write(str(fl) + " -> " + str(time_new) + "\n")
				if(time_new < time):
					s_flags_new = fl
					flg = 1

			if(flg==1):
				s_flags = s_flags_new
			else:
				break	

			iterations = iterations - 1
		
		print s_flags
		time = find_time_gcc(s_flags)
		print " -> "+str(time)
		f.write(str(s_flags) + " -> " + str(time) + "\n")
		x = 1
		while x<4:
			if x==1:
				t = find_time_gcc(["-O1"])
				t1 = t
			elif x==2:
				t = find_time_gcc(["-O2"])
				t2 = t
			elif x==3:
				t = find_time_gcc(["-O3"])
				t3 = t
			print "time"+" O"+str(x)+":"+str(t)
			f.write("time"+" O"+str(x)+":"+str(t)+"\n")
			x = x+1
		f.write(str(t2/time) + " " + str(t3/time) + "\n")
		f.write("----------------------------------------------------------------------------\n")
		f.close()
		
	if sys.argv[1] == "llvm":
		#Applying Greedy Algorithm
		
		iterations = iteration_count
		a = []
		f.write("----------------------------------------------------------------------------\n")
		
		args = "clang -O0 -c -flto "
		args = args + sys.argv[2]
		arg = args.split(" ")
		ai = subprocess.check_call(arg)
		obj = sys.argv[2]
		objf = obj[:-2] + ".o"
		sf = obj[:-2] + ".s"
	
		args = 	"opt -scalarrepl " + objf + " -o " + objf
		arg = args.split(" ")
		ai = subprocess.check_call(arg)

		while(iterations):
			time_min = 100.0
			for i in flags_llvm:
				b = a
				b.append(i)
				if(check_pass(b)>0):
					continue;
				time_new = find_time_llvm(b)
				f.write(str(b) + " -> " + str(time_new) + "\n")
				if(time_new < time_min):
					minima = i
			print iterations
			a.append(minima)	
			iterations-=1
		time = find_time_llvm(a)
		print time
		f.write(str(a)+" -> " + str(time) + "\n")
		
		t2 = find_time_llvm(["-O2"])
		f.write("time O2:"+str(t2)+"\n")
		print t2

		t3 = find_time_llvm(["-O3"])
		f.write("time O3:"+str(t3)+"\n")
		print t3
		
		f.write(str(t2/time) + " " + str(t3/time) + "\n")
		#print "time: " + t
		f.write("----------------------------------------------------------------------------\n")
		f.close()
	return

if __name__ == "__main__":
	main()
