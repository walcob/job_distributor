from mpi4py import MPI
import numpy as np

class JobDistributor:

    def __init__(self,comm,jobs=[]):
        self.comm = comm
        self.rank = self.comm.Get_rank()
        self.size = self.comm.Get_size()
        self.jobs = jobs

    def SendJob(self,child,job):
        '''Sends the object job to the child node'''
        pass

    def GetResult(self,child):
        '''Receives results from child node'''
        pass

    def Distribute(self,jobs=[]):
        '''This function does the heavy lifting.  Will send jobs to every child as they become free and track the results.'''
        pass
