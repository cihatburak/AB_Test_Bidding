##AB TESTING - Bidding

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# !pip install statsmodels
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)


df_max_bidding = pd.read_excel("Datasets/ab_testing.xlsx" , sheet_name="Control Group")
df_max_bidding.describe().T

df_avg_bidding = pd.read_excel("Datasets/ab_testing.xlsx" , sheet_name="Test Group")
df_avg_bidding.describe().T

df_max_bidding.head()
df_avg_bidding.head()  ##Average seems more successful , let's test!

df_max_bidding["Flag"] = 0
df_avg_bidding["Flag"] = 1

df = pd.concat([df_max_bidding,df_avg_bidding],ignore_index= True,axis=0)

df.head()


df.groupby("Flag").mean()

df.loc[df["Flag"] == 1]

# p-value <  0.05'ten HO REJECTION.
# p-value < NOT 0.05 H0 not rejected.


test_stat, pvalue = shapiro(df.loc[df["Flag"] == 1,"Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue)) # p value >0.05 H0 not rejected Normal distribution

test_stat, pvalue = shapiro(df.loc[df["Flag"] == 0,"Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))## p value >0.05 H0 not rejected Normal distribution

# H0: Variances are homogeneous
# H1: Variances are not homogeneous
test_stat, pvalue = levene(df.loc[df["Flag"] == 1,"Purchase"],
                           df.loc[df["Flag"] == 0,"Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))# H0: Variances are homogeneous

############################
# 1.1 Independent two-sample t-test (parametric test) if assumptions are met
############################

test_stat, pvalue = ttest_ind(df.loc[df["Flag"] == 1,"Purchase"],
                              df.loc[df["Flag"] == 0,"Purchase"],
                              equal_var=True)

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

#Shapiro , levene and ttest were used. There is no difference in average between #MAX BIDDING and AVG BIDDING. SO DON'T DO IT!

