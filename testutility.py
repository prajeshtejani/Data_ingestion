import os
import yaml
import re
import logging

def read_config_file(filepath):
    with open(filepath, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logging.error(exc)

def remove_special_character(data,config_data):
      data.columns = data.columns.str.lower()
      data.columns = data.columns.str.replace('[^\w]','_',regex=True)
      data.columns = list(map(lambda x: x.strip('_'), list(data.columns)))
      expected_col = list(map(lambda x: x.lower(),  config_data['columns']))
      if len(data.columns) == len(expected_col) and list(expected_col)  == list(data.columns):
        print("column name and column length validation passed")
        return 1
      else:
        print("column name and column length validation failed")
        mismatched_columns_file = list(set(data.columns).difference(expected_col))
        print("Following File columns are not in the YAML file",mismatched_columns_file)
        missing_YAML_file = list(set(expected_col).difference(data.columns))
        print("Following YAML columns are not in the file uploaded",missing_YAML_file)
        logging.info(f'data columns: {data.columns}')
        logging.info(f'expected columns: {expected_col}')
        return 0