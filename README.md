# Data Engineering Capstone

## Problem Statement

Ridesharing (Uber, Lyft, and the like) has significantly altered urban travel habits during the 2010s, but the effects are not always well-understood. 

* How has the use of ridesharing in the City of Chicago affected traffic congestion since the end of 2018?
* The addition of dockless scooter sharing provides another layer to the transportation network. What effect (if any) did Chicago’s 2019 scooter pilot (and, if data is available, 2020 pilot) have on traffic congestion? Was there an effect on automotive rideshare (i.e. mode shifting)?
* How is the usage of ridesharing and scooter sharing -- and the effects of that usage on traffic congestion -- affected by weather?

## Proposed Dataset(s)

The City of Chicago provides several datasets that allow us to explore these questions:

* **[Historical Congestion Estimates by Segment - 2018-Current](https://data.cityofchicago.org/Transportation/Chicago-Traffic-Tracker-Historical-Congestion-Esti/sxs8-h27x)**; 131M rows. This set includes a selection of Chicago arterial street segments, totaling around 300 miles of roadway, along with estimates of how congested each segment is within a given time slice. Segments are geolocated by latitude/longitude of segment ends.
* **[Transportation Network Providers - Trips](https://data.cityofchicago.org/Transportation/Transportation-Network-Providers-Trips/m6dm-c72p)**; 159M rows. This set includes every trip taken on a Transportation Network Provider (rideshare operator), either starting or ending within Chicago city limits since November 2018. Trips are geolocated by census block of trip start/end.
* **[E-Scooter Trips - 2019 Pilot](https://data.cityofchicago.org/Transportation/E-Scooter-Trips-2019-Pilot/2kfw-zvte)**; 711K rows. This set includes every trip taken on an e-scooter (maintained by a scooter share provider), either starting or ending within Chicago city limits, during Chicago’s 2019 scooter pilot program. Trips are geolocated by census block of trip start/end.

As these datasets are not consistently geolocated, we will also need to transform the congestion data with the **[Boundaries - Census Tracts - 2010](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Census-Tracts-2010/5jrd-6zik)** dataset also provided by the City.

A specific source for weather data is yet to be determined. The City's site offers daily records, which are not sufficiently granular compared to the other data

## Problem Considerations

* _Is the dataset large enough to necessitate distributed computing?_ \
This is to be determined -- individual datasets appear to be 1-2 gigabytes in size, although joins and other transformations may increase the data size.
* _Is the dataset static and complete, or does it undergo incremental updates?_
    * The congestion estimates dataset updates approximately every 15 minutes. Data extraction processes could be made more efficient by making an initial pull to this historical set, then making future calls to the **[live set](https://data.cityofchicago.org/Transportation/Chicago-Traffic-Tracker-Congestion-Estimates-by-Se/n4j6-wkkf)** which updates on the same schedule.
    * The rideshare data does not appear to have been updated since the end of July; this may reflect delays in the rideshare providers sharing data with the City. This dataset may update in the future.
    * The e-scooter data explicitly only covers the period of the 2019 pilot program, and is therefore static. The City is currently running a second pilot, so newer data may become available in the future.
* _Can you combine your primary dataset with another dataset in order to derive more value?_ \
Potentially. Possible expansions include weather data, where effects could potentially be most significant for scooter use.
