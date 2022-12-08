# Equus directory set-up script
import os

os.system('! mkdir outputs')
os.system('! mkdir inputs')
os.system('! mkdir inputs/bris')
os.system('! mkdir inputs/bris/pp')
os.system('! mkdir inputs/bris/res')

years = range(2020,2023)
for year in years:
    os.system('! mkdir inputs/bris/pp/' + str(year) + '/')
    os.system('! mkdir inputs/bris/res/' + str(year) + '/')
