"""creates the domain class used by expr"""

class domain():
   def __init__(self,geometric_dim,topogical_dim,basis=None):
       self.geometric_dim=geometric_dim
       self.topogical_dim=topogical_dim
       self.basis=basis
       return
