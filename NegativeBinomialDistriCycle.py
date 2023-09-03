import pandas as pd
from patsy import dmatrices
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_excel('D:/desktop/content ML/bicycleDataSet.xlsx', header=0, infer_datetime_format=True, parse_dates=[0], index_col=[0])
#df = pd.read_excel(open('C:/Users/Admin/Desktop/content ML/bicycleDataSet.xlsx', 'rb'))


ds = df.index.to_series()
df['MONTH'] = ds.dt.month
df['DAY_OF_WEEK'] = ds.dt.dayofweek
df['DAY'] = ds.dt.day

mask = np.random.rand(len(df)) < 0.8
df_train = df[mask]
df_test = df[~mask]
print('Training data set length='+str(len(df_train)))
print('Testing data set length='+str(len(df_test)))

df_trainip=df_train.iloc[:,[2,3,5,6,7]]
df_trainop=df_train.iloc[:,4]

df_testip=df_test.iloc[:,[2,3,5,6,7]]
df_testop=df_test.iloc[:,4]
#df_trainip=np.array(df_trainip)
#df_trainop=np.array(df_trainop)
#df_trainop=df_trainop.astype('float')
#df_trainip=df_trainip.astype('float')

poisson_training_results = sm.GLM(df_trainop, df_trainip, family=sm.families.Poisson()).fit()

print(poisson_training_results.summary())

#more concern about lambda value
print(poisson_training_results.mu)
print(len(poisson_training_results.mu))

#will find the value fo alpha using OLS regression

import statsmodels.formula.api as smf

#add lambda value to dataset.
df_train['BB_LAMBDA'] = poisson_training_results.mu

#add a derived column AUX_OLS_DEP
df_train['AUX_OLS_DEP'] = df_train.apply(lambda x: ((x['Brooklyn Bridge'] - x['BB_LAMBDA'])**2 - x['Brooklyn Bridge']) / x['BB_LAMBDA'], axis=1)


ols_expr = """AUX_OLS_DEP ~ BB_LAMBDA - 1"""

aux_olsr_results = smf.ols(ols_expr, df_train).fit()

print(aux_olsr_results.params)

aux_olsr_results.tvalues

nb2_training_results = sm.GLM(df_trainop, df_trainip,family=sm.families.NegativeBinomial(alpha=aux_olsr_results.params[0])).fit()
print(nb2_training_results.summary())


nb2_predictions = nb2_training_results.get_prediction(df_testip)
predictions_summary_frame = nb2_predictions.summary_frame()
print(predictions_summary_frame)

predicted_counts=predictions_summary_frame['mean']
actual_counts = df_testop
fig = plt.figure()
fig.suptitle('Predicted versus actual bicyclist counts on the Brooklyn bridge')
predicted, = plt.plot(df_testip.index, predicted_counts, 'go-', label='Predicted counts')
actual, = plt.plot(df_testip.index, actual_counts, 'ro-', label='Actual counts')
plt.legend(handles=[predicted, actual])
plt.show()
