""" This is a module with tools to work with raster data."""

import os
import sys

import rasterio
import numpy as np


def read_raster(dem_path):
    """
    Read raster to numpy array.

    Read a single raster with rasterio and store raster in memory as a numpy array. Also reads and returns DEM metadata.

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


def rasters_to_dict(dir):
    """
    Read all rasters in a certain directory and store arrays and
    metadata in a dicitonary.

    Read all GeoTIFFs with rasterio and store values inside an numpy
    array while conserving some metadata inside a dictionary.

    Args:
        dem_path (str): file path to directory containing rasters

    Returns:
        arr (ndarray): array of elevation values
        pixel_size (float): pixel size aka grid/spatial resolution
        profile (dict): metadata profile
    Raises:
        Exception: description
    """

    # Initialize empty dictionary

    rstr_dict = {}

    file_list = glob.glob(str(dir) + '*.tif')

    for f in file_list:

        rstr_dict[f] = {}

        src = rasterio.open(f)
        rstr_dict[f]['arr'] = src.read(1)
        rstr_dict[f]['profile'] = src.profile

        rstr_dict[f]['year'] = re.findall('(\d{4})', f)
    return rstr_dict
