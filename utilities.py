import pandas as pd
import numpy as np
import geopandas as gpd


# Arapahoe County Border
def get_Arap_Outline():
    Arap_outline = gpd.read_file(r'C:\Users\phna007\OneDrive - Arapahoe County Government\Data\Shapefiles\us-county-boundaries')

    return Arap_outline

def get_schools():
    df = pd.read_csv(r"C:\Users\phna007\OneDrive - Arapahoe County Government\Desktop\EH_map_app\Env_Health\assets\data\CDPHE_CDOE_School_Locations_and_District_Office_Locations.csv")
    df = df.loc[df['COUNTY'] == 'ARAPAHOE']
 
    df = df.rename(columns={'LONGITUDE': 'lon', 'LATITUDE': 'lat', 'School_Name': 'Name'})
  
    return df

def get_Tobacco_Retailers():
    df = pd.read_csv(r"C:\Users\phna007\OneDrive - Arapahoe County Government\Documents 1\ArcGIS\Projects\MyProject22\GC_tobacco_retailers.csv")

    return df

def get_compliance_records():
    df = pd.read_csv(r"C:\Users\phna007\Downloads\Tobacco_Licenses_12.08.2023.csv", encoding='latin1')
    # print(df)
    return df

# def get_combo():
#     df = pd.read_csv(r"C:\Users\phna007\OneDrive - Arapahoe County Government\Desktop\Tobacco_Map\Tobacco_Map\tobacco_combo.csv")
#     print(df.columns)
#     print(df.iloc[:, 1].sort_values())
#     df = df[~df['Count'].isna()]
#     df['occur'] = df.groupby('ID')['ID'].transform('size')

#     return df

def get_combo():
    df = pd.read_csv(r"C:\Users\phna007\OneDrive - Arapahoe County Government\Desktop\Tobacco_Map\Tobacco_Map\tobacco_combo_3.csv")
    print(df.columns)
    print(df.iloc[:, 1].sort_values())
    df = df[~df['count'].isna()]
    print(df)
    df = df[df['County'] == 'Arapahoe']
    print(df)
    
    # df['occur'] = df.groupby('ID')['ID'].transform('size')

    return df



