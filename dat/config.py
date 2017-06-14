# -*- coding:utf-8 -*-

# used in fetch.py as target hours for each one in current month
hours = '168'

# used in modify_table.py to define the columns to be fetched for each table
column = {'CDT1': [1, 4, 5, 16, 17, 29, 37],
          'CDT2': [1, 4, 5, 16, 17, 28, 36],
          'MUS': [0, 1, 7, 11, 16],
          'FA': [0, 1, 3, 10]}

# used in output.py to define the sheet name of each case
sheetName = {'1010': 'CC UR Top 10',
             '1009': 'CC UR Bottom 10',
             '1008': 'Individual UR top 5 per CC',
             '1007': 'Individual UR Bottom 5 per CC',
             '1006': 'Top 50 individual UR in IT&C',
             '1005': 'Bottom 50 individual UR in IT&C',
             '1003': 'Nightshift data per CC',
             '1004': 'Individual nightshift in IT&C',
             '1002': 'Remote percentage',
             '1001': 'Service delivery to per region',
             '1000': 'Remote percentage to per region'}

# used in output.py to define the sheet Headers of each case
sheetHeader = {'1010': ['Cost_Center', 'Total_Chargable_Hours', 'Headcount', 'Target_Hours', 'UR'],
               '1009': ['Cost_Center', 'Total_Chargable_Hours', 'Headcount', 'Target_Hours', 'UR'],
               '1008': ['Individual_Total_Hours', 'PersonnelNo', 'Name', 'CostCenter', 'LM', 'UR'],
               '1007': ['Individual_Total_Hours', 'PersonnelNo', 'Name', 'CostCenter', 'LM', 'UR'],
               '1006': ['Individual_Total_Hours', 'PersonnelNo', 'Name', 'CostCenter', 'LM', 'UR'],
               '1005': ['Individual_Total_Hours', 'PersonnelNo', 'Name', 'CostCenter', 'LM', 'UR'],
               '1003': ['Total_NS_Hours', 'CostCenter'],
               '1004': ['Total_NS_Hours', 'PersonnelNo', 'Name', 'CostCenter'],
               '1002': ['Total_HC_Hours', 'Total_Hours', 'Remote_Percentage'],
               '1001': ['Region', 'Region_Hours', 'Percentage'],
               '1000': ['Region', 'Region_HC_Hours', 'Region_Hours', 'Region_Remote_Percentage']}

# used in modify_table.py to define the Headers of each table

headers = {'FA': ['Item', 'CostCenter', 'EmployeeGroup', 'Hours'],
           'CDT': ['Region', 'PersonnelNo', 'Name', 'Type', 'CostCenter', 'LM', 'Hours'],
           'MUS': ['Name', 'Date', 'PersonnelNo', 'CostCenter', 'Hours']}
