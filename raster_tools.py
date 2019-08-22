""" This is a module with tools to work with raster data."""

import os
import sys

import rasterio
import numpy as np


def read_raster(dem_path):
    """
    Read raster to numpy array.

    Read a single raster with rasterio and store raster in memory as a numpy
    array. Also reads and returns DEM metadata.

    Args:
        raster_path (str): path to DEM

    Returns:
        arr (ndarray): array of elevation values
        profile (dict): metadata profile
    Raises:
        Exception: description
    """

    src = rasterio.open(raster_path)
    arr = src.read(1)
    profile = src.profile
    return (arr, profile)


def rasters_to_dict(raster_dir, ext):
    """
    Read all rasters in a directory.

    Read all rasters with rasterio and store values inside an numpy
    array while conserving metadata inside a dictionary.

    Args:
       raster_dir (str): file path to directory containing rasters
       ext (str): wildcar file extension for rasters (e.g. "*.tif")

    Returns:
        arr (ndarray): array of raster values
        profile (dict): metadata profile
    Raises:
        Exception: description
    """

    # Initialize empty dictionary

    rstr_dict = {}

    file_list = glob.glob(str(raster_dir) + ext)

    for f in file_list:

        rstr_dict[f] = {}

        src = rasterio.open(f)
        rstr_dict[f]['arr'] = src.read(1)
        rstr_dict[f]['profile'] = src.profile

    print(len(file_list) + " rasters read to memory."
    return rstr_dict
    

def write_raster(arr, outpath, profile):
    """
    Write raster to disk with correct metadata.

    Write raster from memory (numpy array) to certain disk location with correct    profile (dictionary of metadata).

    Args:
        arr (ndarray): array of raster values
        outpath (str): output filename and path for raster
        profile (dict): metadata for output

    Returns: None
    """
    # Write to a new raster
    with rasterio.open(outpath, 'w', **profile) as dst:
        dst.write(arr, 1)

    print("Raster written to: " + outpath)


def negative_raster_values_to_zero(arr):
    """
    Convert all negative raster values to 0.00 and modified raster to disk.
    
    Useful for plotting and filtering noise or outlying values. Output raster will have 'all_postive' added to end of the filename. 
    """

    # read in the data
    src = rasterio.open(args.raster)
    profile = src.profile
    arr = src.read(1)

    # replace negative values (but not null data) with 0
    arr = src.read(1)
    arr[np.where(np.logical_and(arr != profile['no data'], arr < 0))] = 0

    # Write to a new .tif, using the same profile as the source
    outpath = args.raster.split('.tif')[0] + '_bumped.tif'
    with rasterio.open(output, 'w', **profile) as dst:
        dst.write(arr, 1)

    print("New raster written to: " + outpath)
    print("Minimum value of new raster: )" + np.nanmin(arr)


ii(base) [cparr@localhost utils
