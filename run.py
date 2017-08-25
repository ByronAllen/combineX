import os

# Install pandas if it does not exist
# If pip does not exist, please also install pip 
#pip_list = !pip list
#if 'pandas' not in [item.split(' ')[0].lower() for item in pip_list]:
#    !pip install pandas

import pandas as pd

# Establish variables 
directory='./' + raw_input('What directory would you like to read from?: ')
output_directory='./' + raw_input('What directory would you like to write to?: ')
output_file='/' + raw_input('Save output file as?:')
column_name=raw_input('What is the name of the column you want to use?: ')
csvs=[csv for csv in os.listdir(directory) if csv.endswith('.csv') == True]
length_of_dataset=pd.read_csv(directory + '/' + csvs[0]).shape[0]
df=pd.DataFrame(index=range(length_of_dataset))

# Iterate through designated folder and combine the column_name field in each CSV
for csv in csvs:
    file_path = directory + '/' + csv
    new_df=pd.read_csv(file_path, index_col=0)[[column_name]]
    new_df[csv.split('.')[0]]=new_df[column_name]
    new_df.drop(labels=column_name, inplace=True, axis=1)
    df=df.merge(new_df, left_index=True, right_index=True)

# Save 'combineX' table as csv
df.to_csv(output_directory + output_file + '.csv')
