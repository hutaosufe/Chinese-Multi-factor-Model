import numpy as np
class linearmodel:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        b=np.linalg.solve(x.T@x,x.T@y)
        self.b=b
        e=y-x@b
        self.e=e
        self.vb=e.var()*np.linalg.inv(x.T@x)
        self.se=np.sqrt(np.diagonal(self.vb))
        self.tstat=self.b/self.se
    def vcov_b(self,e):
        x=self.x
        return e.var(*np.linalg.inv(x.T@x))
    class Newey_West(linearmodel):
        def vcov_b(self,e):
            x=self.x
            sigma_one=0
            for k in range(len(e)-1):
                sigma_one+=e[k]*e[k+1]
            sigma_one=sigma_one/len(e)
            errmat=np.diagflat(np.mean(e.values**2))
            for i in range (len(errmat)-1):
                            errmat[i][i+1]=sigma_one
                            errmat[i+1][i]=sigma_one
            flank=np.linalg.inv(x.T@x)@x.T
            West=flank@errmat@flank.T
            return(West)
