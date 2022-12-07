Changelog
===================

Version 0.1.0 (2020-08-09)
------------------------------------------
- initial creation

Version 0.1.1 (2020-08-15)
------------------------------------------
- added sample datasets for documentation
- added support for numpy types in encoder

Version 0.1.2 (2020-08-16)
------------------------------------------
- added a :code:`chart.append` shortcut for :code:`chart.series.append`

Version 0.1.3 (2020-08-20)
------------------------------------------
- added a few additional shortcuts

Version 0.1.4 (2020-08-22)
------------------------------------------
- fixed the regular expression of the tooltip shortcut to allow no prefix
- you can assign a tuple to :code:`chart.tooltip`

Version 0.1.5 (2020-08-23)
------------------------------------------
- refactored rendering
- added config file to inject additional modules and stylesheets
- added themes from `Joshua Kunst <http://jkunst.com/highcharts-themes-collection/>`_

Version 0.1.6 (2020-08-24)
------------------------------------------
- timestamp support for datetime.date
- bugfix in importing config.json

Version 0.1.7 (2020-10-29)
------------------------------------------
- flatted data points when constructing timestamped arearange charts 
- upgraded highcharts javascripts injections to version 8
- added argument aliases in series.append

Version 0.1.8 (2020-10-31)
------------------------------------------
- added simple linear regression

Version 0.1.9 (2020-11-07)
------------------------------------------
- :code:`enabled` and :code:`active` are now aliases for :code:`visible` in :code:`chart.plot`
- refactored the encoders to expose both a function and a class
- dictionary keys, values and items are now serializable
- added aliases

Version 0.1.10 (2020-11-20)
------------------------------------------
- added aliases for datalabels

Version 0.1.11 (2021-03-28)
------------------------------------------
- pd.DataFrame and 2d np.arrays will no longer be interpreted as list of column series to accommodate alternative series types (e.g. boxplots, arearange) 

Version 0.1.12 (2021-04-13)
------------------------------------------
- added support for `datetime.time` in chart xAxis

Version 0.1.13 (2021-10-16)
------------------------------------------
- refactored config object

Version 0.1.14 (2022-02-22)
------------------------------------------
- add errors message if highcharts fails to render in Jupyter notebook
- fixed bug in stacking
- added jinja2 to list of dependencies
- formatted codebase with Black
- refactored plotting with Pandas
- handled serialization for ranges and zips

Version 0.1.15 (2022-12-07)
------------------------------------------
- updated default config values to unpin highcharts versions
- added `chart.annotate` and `chart.draw` convenience methods
- refactored chart dimensions logic
- allow `index=False` when plotting with Pandas to drop index

