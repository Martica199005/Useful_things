import pandas as pd
import numpy as np


#gives pandas version
#pd.__version__

#show pandas versions, details
#pd.show_versions()

# Replace keyword to read from other data sources like

#pd.read_excel        - For reading from Excel file
#pd.read_gbq          - For reading from Google Bigquery
#pd.read_hdf          - For reading from big data sources
#pd.read_html         - For reading from html files
#pd.read_json         - For reading from JSON files 
#pd.read_sql_query    - For reading from SQL database

#pandas series 1-dim
#a=pd.Series(data,index,datatype)

# a= pd.Series()
# print(a)
#1 case: no index
data=[1,3,5,7,9]
odd_numbers = pd.Series(data)
print(odd_numbers)

#2 case: my own index
fruit=['apple','orange','banana','pear']
rate=[2,2.50,3,3.50]

shop = pd.Series(rate,fruit)
print(shop)

#pandas Dataframes 2-dim
#a=pd.DataFrame(data,index,columns,datatype?)
# empty=pd.DataFrame()
# print(empty)

print('See the difference between Series and Dataframe: index for the columns too')

odd_numbers1=pd.DataFrame(data)
print(odd_numbers1)

print('use 2-dim data')

data1=[[1,2],[3,4],[5,6]]
df_table=pd.DataFrame(data1)
print(df_table)


#Custom columns and index
print('Columns and index')
col=['number1','number2']
idx=[1,2,3]
df_table=pd.DataFrame(data1,index=idx, columns=col)
print(df_table)

#create a DataFrame from a dictionary
dict={'Name':['Marta','Juanda','Dora'],'Marks':[10,9,8]}
df_table=pd.DataFrame(dict)
print(df_table)

print('--------')
#descriptive analytics
df=pd.read_csv('FL_insurance_sample.csv')
print('Shape of DF:', df.shape)
print('Number of rows in DF:', df.shape[0])
print('Number of columns in DF:', df.shape[1])

#Get the list of columns
print(df.columns)

#Gives the statistics of a table but if you put include='all' shows also the non numerical values
print(df.describe(include='all'))
print('\n')
#gives the info of the table
print('Info:')
print(df.info())

#gives the first n rows of the table
print('first n rows')
print('here n=3')
print(df.head(3))

#gives the last n rows of the table
print('last n rows')
print('here n=3')
print(df.tail(3))

#Gives the unique/no unique values of a column: values=df.column_name.unique/nunique()

#two ways to access a column:
#print(df['statecode']) 
#print(df.statecode) it can't be used when the column name has some spaces
print('Mean of the values of the column policyID:')
print(df['policyID'].mean()) 


#isnull() returns a boolean if there are or not null values and sum() gives how many null values there are
print(df.point_granularity.isnull().sum())


#apply and map functions
df['new_column']=df['point_granularity'].apply(lambda x: x*10)
print(df[['new_column','point_granularity']].head(3))
#map can be used in the same way only for series or columns
print('map can be used in the same way only for series or columns')


print('--------')
#np??
df=pd.DataFrame(np.random.randn(5,2),index=[1,5,3,4,2],columns=['a','b'])
print(df)
#df.plot()

#looks for the index which has value 2
print(df.loc[2])

#looks for the index at the position 2
print(df.iloc[2])

#sort
print('sort')
print(df.sort_index())
#f.sort_index(ascending=False)

print('sort values')
print(df.sort_values('a'))

df_slices=df[0:3] #?
print(df)


#df.isnull().sum()

#df.dropna()

#df.dropna(subset=['a'])

#df.dropna(axis='columns) drop the columns with NaN values

#df.fillna(0) fill with zero
#df.fillna(method='ffill') forward fill (previous value)
#df.fillna(method='bfill') before fill

print('Grouping, filtering')
print(df)

#it is not working
#df[['policyID','point_granularity']].groupby(['policyID'],as_index=True).mean()
#from min 30
#df[['policyID'].values_counts()
#df.groupby('policyID').filter(lambda x: len(x)>50)
m=df.groupby('a').filter(lambda x: len(x)<=1)
print(m)


























# def etl_to_srcdata_gme_fa_marta(file, dl_srcdata_path,xpath):
#   spark = SparkSession.builder.getOrCreate()
  
  
#   ETL_source_path="/dbfs"+dl_rawdata_path
#   ETL_target_path="/dbfs"+dl_srcdata_path
#   xml_xpath = xpath
#   downloaded_filelist = file_list(dl_rawdata_path)
#   i=0
#   dbutils.fs.mkdirs(dl_srcdata_path) 

#   doc_creation_date=datetime.strptime(file.split("_")[0], "%Y%m%d%H%M%S").strftime("%Y%m%d %H:%M:%S")
#   df = spark.read.format('xml').options(rowTag=xml_xpath ,rootTag = xml_xpath).load(dl_rawdata_path+file)
#   df = df.toPandas()
#   df['doc_creation'] = doc_creation_date
  
  
#   if xpath=="marketintervaldetail":
#     df.drop('Totale', axis=1, inplace=True)
#   elif xpath=="Fabbisogno":
#     df.drop('Totale', axis=1, inplace=True)#edit
#   else:
#     df.drop('Italia', axis=1, inplace=True)