"""creates the domain class used by expr"""

class Domain():
    def __init__(self,geometric_dim,topological_dim):
        self.geometric_dim=geometric_dim
        self.topological_dim=topological_dim
        self.basis={}
        for i in range(self.topological_dim):
            self.basis[i]="dx{}".format(i)

    def __str__(self):
      return "Domain"

    def __repr__(self):
      return "{}({},{})".format(__class__.__name__,self.geometric_dim,self.topological_dim)
