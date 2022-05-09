#!/usr/bin/python3

# Somewhere you have imported your data in forms of lists
# In these examples the one called `tempo` contains the time, the other contains the values of the data and is called `flusso`
# I am using the words for time (tempo) and flux (flusso), for avoiding confusion with some keyword of the various call used.
# The objet that will be created is named `ts_flusso`.
#
# The following examples provide the mimimum needed for working with these packages, obviously for having a more finer control
# you need to read the appropriate documentation of each package.

#Pandas
import pandas as pd
ts_flusso=pd.Series(data=flusso,index=tempo)

#stumpy
import stumpy
ts_flusso = pd.DataFrame(np.column_stack([tempo,flusso]),columns=['label_tempo','label_flusso'])

#sunpy
#the method for Pandas is the one that allow to build an object compatible with sunpy
import pandas as pd
import sunpy
ts_flusso=pd.Series(data=flusso,index=tempo)

# GWpy
from gwpy.timeseries import TimeSeries
# case 1: data taken continuosly in time withouth gaps
# temporal cadence is the time interval between one point and another
ts_flusso = TimeSeries(flusso, dt=temporal_cadence)
# case 2: data tha could have gaps or are unevenly sampled
# in this case flusso and tempo need to have the same length
# with these kind of data GWpy is not hable to calculate the spectrograms
ts_flusso = TimeSeries(flusso, times=tempo)

#lightkurve
# this package is more .complicated.
# you need to have an additional list that contains the errors on the observations (flusso_errore) 
# and for the asteroseismology part is needed a variable that contains the effective temperature of the star (temperatura)
import lightkurve
ts_flusso = lightkurve.LightCurve(time=tempo,flux=flusso,flux_err=flusso_errore)
ts_flusso.meta["TEFF"] = temperatura
# for creating a Lomb-Scargle periodogram with your own data that could be compatible with these package withouth the need to recalculate it again
# you need to have a list containing the evenly spaced frequencies in microHz, and
# the results of your periodgram need to be in power spectrum density (PSD)
frequenza = original_frequency * your_conversion_factor_to_uHz
potenza   = (original_power / frequenza)
ts_periodLS = lightkurve.periodogram.Periodogram(frequenza,potenza)
ts_periodLS.meta["TEFF"] = teff

#sktime
# import data in nested data frame
# need to define two additional lists
# one with the index: case_id
# the other with a dimensional_id: dim_id (this act like a flag ?!?!?!?)
# this implementation works smoothly, however it does not work with any prediction model because 
# it seems that is necessary a pandas.core.series.Series instead of a pandas.core.frame.DataFrame
# question raised in the sktime forum
import sktime as sk
from sktime.utils.data_processing import from_long_to_nested
# get the length of flusso and create the other two lists
NP=length(flusso)
caso_id=np.arange(NP)
dimensione_id=np.zeros(NP)
# create the data frame in the so called long format (by sktime documentation)
lc = pd.DataFrame(np.column_stack([caso_id,dimensione_id,tempo,flusso]),columns=['case_id','dim_id','time','value'])
# convert the data frame in a nested one
lc_nested = from_long_to_nested(lc,instance_column_name='case_id',dimension_column_name='dim_id',time_column_name='time',value_column_name='value')
print('lc_nested data type:',type(lc_nested))


