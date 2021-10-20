# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 19:46:51 2021

@author: Richards Paul
"""

import pandas as pd
import pandasql as ps

df_purchase = pd.read_excel("SQL_sample_purchase_history.xlsx")
df_master = pd.read_excel("SQL_sample_product_master.xlsx")

# print(ps.sqldf("select * from df"))

query_1 = """
        select * from df_purchase 
        inner join df_master 
        on df_purchase.Product_Id = df_master.Product_Id
        """

# where df_purchase.Product_Id = 100

output = ps.sqldf(query_1)

# print(output)

df_output = pd.DataFrame(output)

df_output.to_excel("output_outer_join.xlsx", index=False)



