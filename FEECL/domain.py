"""creates the domain class used by expr"""

class Domain():
    def __init__(self,geometric_dim,topogical_dim):
        self.geometric_dim=geometric_dim
        self.topogical_dim=topogical_dim
        self.basis={}
        for i in range(self.geometric_dim):
            self.basis[i]="dx{}".format(i)
