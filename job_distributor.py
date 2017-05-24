from mpi4py import MPI
import numpy as np
import sys

class JobDistributor:

  def __init__(self,comm,jobs=np.array([])):
    self.comm = comm
    self.rank = self.comm.Get_rank()
    self.size = self.comm.Get_size()
    self.jobs = jobs
    self.results=np.array([])
    if self.jobs.size > 0: self.Distribute()

  def SendJob(self,child,job):
    '''Sends the object job to the child node'''
    pass

  def GetResult(self,child):
    '''Receives results from child node'''
    pass
    self.results = np.append(self.results,result)

  def Distribute(self,jobs=np.array([])):
    '''This function does the heavy lifting.  Will send jobs to every child as they become free and track the results. If a list of jobs is supplied here, they will be appended to self.jobs'''
    first = True
    if jobs.size == 0 and self.jobs.size == 0:
      sys.stderr.write("Warning: Distributing 0 jobs\n")
      sys.stderr.flush()
    else:
      self.jobs = np.concatenate(self.jobs,jobs)
    while 1:
      if self.jobs.size == 0: return self.results
      if first:
        for i in range(self.size):
          if i != self.rank:
              self.SendJob(i,self.jobs[0])
              self.jobs = self.jobs[1:]
        first = False
      for i in range(self.size):
        if i != self.rank and self.GetResult(i) and self.jobs.size > 0:
          self.SendJob(i,self.jobs[0])
          self.jobs = self.jobs[1:]
