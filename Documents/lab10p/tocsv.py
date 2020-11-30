import pandas as pd
Boys = pd.read_csv("2000_BoysNames.txt"
                       , header=None)
Boys.columns = ['First Name', 'Count']
Boys.to_csv('2000_BoysNames.csv',
                index=None)
Girls = pd.read_csv("2000_GirlsNames.txt"
                       , header=None)
Girls.columns = ['First Name', 'Count']
Girls.to_csv('2000_GirlsNames.csv',
                index=None)