from adcircpy.lib.gdal_tools import gdal_tools
__all__ = ['gdal_tools']


# import os
# import wget
# import tarfile

# def __init_TPXO_cache():
#     cachedir = get_cache_dir()
#     tpxo_path = cachedir + "/h_tpxo9.v1.nc"
#     os.makedirs(cachedir, exist_ok=True)
#     if os.path.isfile(cachedir+"/h_tpxo9.v1.nc") is False:
#         print('Building TPXO database cache on {},'.format(tpxo_path)
#               + ' please wait... (This will only happen the first time you run'
#               + ' this software)')
#         url = 'ftp://ftp.oce.orst.edu/dist/tides/Global/tpxo9_netcdf.tar.gz'
#         if os.path.isfile(cachedir+"/tpxo9_netcdf.tar.gz") is False:
#             wget.download(url, out=cachedir+"/tpxo9_netcdf.tar.gz")
#         tpxo = tarfile.open(cachedir+"/tpxo9_netcdf.tar.gz")
#         tpxo.extract('h_tpxo9.v1.nc', path=cachedir)
#         tpxo.close()
#         os.remove(cachedir+"/tpxo9_netcdf.tar.gz")
#     return tpxo_path