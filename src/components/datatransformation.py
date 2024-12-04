import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute SimpleImputer
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import logging

 @dataclass
 class DataTransformationConfig:
     preprocessor_obj_file_path=os.path.join('articrafts','preprocessor.pkl')
     
class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
        
    def get_data_transformer_object(self):
        '''
        tHis function returns transformed data
        '''
        try:
            numerical_columns=[]
            cat_columns=[]
            num_pipeline = pipeline(
                steps = [
                    ('imputer',SimpleImputer(Strategy='median'))
                    ('scaler',StandardScaler)
                         
                
            ])
            
            cat_pipeline = Pipeline(
                steps = [('imputer',SimpleImputer(strategy='most_frequent')),
                         ('one_hot_encoder',OneHotEncoder()),
                         ('scaler',StandardScaler())
                         ]
            )
            
            logging.info("Numerical columns scaling completed")
            logging.info("categorical columns encoding completed")
            
            preprocessor=ColumnTransformer([
                ('num_pipeline',num_pipeline,num_features),
                ('cat_pipeline',cat_pipeline,cat_columns)
            
            ])
            
            return preprocessor
            
            
        except Exception as e:
            raise CustomException(e,sys)
        
        
        
def initiate_data_transformation(self,train_path,test_path):
    try:
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)
        
        logging.info("read train and test data completed")
        logging.info("obtaining preprocessing object")
        
        pre