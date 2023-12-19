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
    df = pd.read_csv(r"C:\Users\phna007\Downloads\compliancecheckreport.csv", encoding='latin-1')
    
    return df

