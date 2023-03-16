


# source: https://www.tutorialspoint.com/How-are-files-extracted-from-a-tar-file-using-Python  
import tarfile

tar = tarfile.open('/Users/tactlabs5/Documents/dev/tact/py-etl-csv-pg/source/CsvSamples.tar.gz')
tar.extractall('/Users/tactlabs5/Documents/dev/tact/py-etl-csv-pg/destination')
tar.close()
