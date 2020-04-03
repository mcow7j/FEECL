from distutils.core import setup
from glob import glob

setup(name='FEECL',
      version=2020.0,
      description="""FEEC Language""",
      author="Matthew Cowley",
      author_email="mc7315@imperial.ac.uk",
      packages=["FEECL"],
      scripts=glob('scripts/*'))
