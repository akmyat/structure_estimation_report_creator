import os
import re
import numpy as np
import pandas as pd
from glob import glob

class ShearReport:
    def __init__(self, folder_path, output_name):
        self.folder_path = folder_path
        self.output_name = output_name
    
    def create_report(self):
        files = [os.path.basename(x) for x in glob(self.folder_path + "*.txt")]

        f = open(self.folder_path + files[0], "r")
        content = f.readlines()

        info = "".join(content[1:6])

        column_data = content[7:len(content)-2]
        column_data = [x.strip().split(',') for x in column_data]

        columns_name = [re.findall(r"[a-zA-Z]+\s*[a-zA-Z]*", column_data[0][i])[0].title() for i in range(0, len(column_data[0]), 2)]

        column_data = np.array(column_data)
        column_data = np.delete(column_data, [i for i in range(0, len(column_data[0]), 2)], axis=1)
        column_df = pd.DataFrame(column_data, columns=columns_name)

        df_list_names = list()
        df_lists = list()

        for file in files:
            f = open(self.folder_path + file, "r")
            content = f.readlines()

            name = content[0].strip()

            minimum = content[-1].strip().split(',')
            minimum.pop(0)
            
            maximum = content[-2].strip().split(',')
            maximum.pop(0)

            abs_maximum = [max(abs(float(minimum_)), abs(float(maximum_))) for minimum_, maximum_ in zip(minimum, maximum)]
            
            minmax_df = pd.DataFrame(np.array([minimum, maximum, abs_maximum]).T, columns=["Maximum", "Minimum", "Absolute Maximum"])

            df_list_names.append(name)
            df_lists.append(minmax_df)

        df_columns = [info] + df_list_names
        dfs = [column_df] + df_lists

        all_df = pd.concat(dfs, axis=1, keys=df_columns)

        all_df.to_excel(self.folder_path + self.output_name + ".xlsx")
        all_df.to_csv(self.folder_path + self.output_name + ".csv", index=False)

        return self.folder_path + self.output_name + ".xlsx/.csv"
