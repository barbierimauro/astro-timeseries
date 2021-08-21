#!/usr/bin/python3

# somewhere you have imported your data in forms of lists
# in these examples the one called `tempo` contains the time, the other contains the values of the data and is called `flusso`
# I am using italian words for time (tempo) and flux (flusso), for avoiding confusion with some keyword of the various call used
# the objet that will be created is named `ts_flusso`
#
# the following examples provide the mimimum needed for working with these packages, obviously for having a more finer control
# you need to read the appropriate documentation of each package

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
# this package is more complicated
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

#
