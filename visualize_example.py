# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 17:30:07 2016

@author: Fish_user
"""


import pandas as pd
from sqlalchemy import create_engine
import psycopg2


engine = create_engine('postgresql+psycopg2://postgres:123456@localhost:5432/%s' % 'ashare')
print "go..."

def test_run():
    usecols =['school_state', 'resource_type','poverty_level', 'date_posted' ,'total_donations']
    
    df = pd.read_csv("opendata_projects.csv",usecols = usecols)
    print df.head()
   # df.to_sql("donation",engine)
    print "done"


if __name__== '__main__':
    #test_run()
    pass