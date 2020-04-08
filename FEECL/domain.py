"""creates the domain class used by expr"""

class Domain():
   def __init__(self,geometric_dim,topogical_dim,basis=None):
       self.geometric_dim=geometric_dim
       self.topogical_dim=topogical_dim
       self.basis=basis
