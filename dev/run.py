import os
import pandas as pd

directory='./' + raw_input('What directory would you like to read from?: ')
output_directory='./' + raw_input('What directory would you like to write to?: ')
output_file='/' + raw_input('Save output file as?:')
csvs=[csv for csv in os.listdir(directory) if csv.endswith('.csv') == True]
length_of_dataset=pd.read_csv(directory + '/' + csvs[0]).shape[0]
df=pd.DataFrame(index=range(length_of_dataset))

for csv in csvs:
    file_path = directory + '/' + csv
    new_df=pd.read_csv(file_path, index_col=0)[['x']]
    new_df[csv.split('.')[0]]=new_df.x
    new_df.drop(labels='x', inplace=True, axis=1)
    df=df.merge(new_df, left_index=True, right_index=True)

df.to_csv(output_directory + output_file + '.csv')
