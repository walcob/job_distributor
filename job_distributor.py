from mpi4py import MPI
import numpy as np
import sys

class JobDistributor:

    def __init__(self,comm,jobs=[]):
        self.comm = comm
        self.rank = self.comm.Get_rank()
        self.size = self.comm.Get_size()
        self.jobs = jobs
        if self.jobs != []: self.Distribute()
        self.results=[]

    def SendJob(self,child,job):
        '''Sends the object job to the child node'''
        pass

    def GetResult(self,child):
        '''Receives results from child node'''
        pass

    def Distribute(self,jobs=[]):
        '''This function does the heavy lifting.  Will send jobs to every child as they become free and track the results. If a list of jobs is supplied here, they will be appended to self.jobs'''
        first = True
        if jobs == [] and self.jobs == []:
            sys.stderr.write("Warning: Distributing 0 jobs")
        else:
            self.jobs += jobs
        while 1:
            if jobs == []: return self.results
            if first:
                for i in range(self.size):
                    if i != self.rank: self.SendJob(i,self.jobs.pop())
                first = False
            for i in range(self.size):
                if i != self.rank and self.GetResult(i) and self.jobs != []: self.SendJob(i,self.jobs.pop())
