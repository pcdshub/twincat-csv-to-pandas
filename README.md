twincat-csv-to-pandas
---------------------

Simple script which loads a TwinCAT-exported scope CSV into a Pandas DataFrame.

This is not an installable package.

Usage
-----

```python
$ ipython -i twincat_csv.py

In [1]: metadata, df = read_beckhoff_csv('../LAMBKB_SAT_SCOPE/Noise_axes_disabled.csv')
row count 16197
elapsed time 32.392
sample time 0:00:00.002000
start time 2020-06-03 10:18:16.635000
end time 2020-06-03 10:18:49.027000

In [2]: df.head()
Out[2]:
                            Axes.M2K4 rY.ActPos  ...  Axes.M3K4 rX.PosDiff
Time                                             ...
2020-06-03T10:18:16.635000         14396.545272  ...                     0
2020-06-03T10:18:16.637000         14396.545272  ...                     0
2020-06-03T10:18:16.639000         14396.545272  ...                     0
2020-06-03T10:18:16.641000         14396.582708  ...                     0
2020-06-03T10:18:16.643000         14396.646884  ...                     0

[5 rows x 6 columns]

In [3]: metadata['Axes.M2K4 rY.ActPos']
Out[3]:
{'Name': 'ActPos(2)',
 'SymbolComment': '',
 'Data-Type': 'REAL64',
 'SampleTime': '2',
 'VariableSize': '8',
 'SymbolBased': 'True',
 'IndexGroup': '16643',
 'IndexOffset': '65538',
 'SymbolName': 'Axes.M2K4 rY.ActPos',
 'NetID': '134.79.82.176.1.1',
 'Port': '501',
 'Offset': '0',
 'ScaleFactor': '1',
 'BitMask': '0xffffffffffffffff',
 'Unit': '(None)',
 'Unit ScaleFactor': '1',
 'Unit Offset': '0'}

```
