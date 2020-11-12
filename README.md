# Data Engineering Capstone

## Problem Statement

Ridesharing (Uber, Lyft, and the like) has significantly altered urban travel habits during the 2010s, but the effects are not always well-understood. 

* How has the use of ridesharing (Transportation Network Providers / TNP) in the City of Chicago affected traffic congestion since the end of 2018?
* The addition of dockless scooter sharing provides another layer to the transportation network. What effect (if any) did Chicago’s 2019 scooter pilot (and, if data is available, 2020 pilot) have on traffic congestion? Was there an effect on automotive rideshare (i.e. mode shifting)?
* How is the usage of ridesharing and scooter sharing -- and the effects of that usage on traffic congestion -- affected by weather?

## KPIs

* Time-sliced congestion by census block over time (i.e. how traffic-congested was census block X from 8-8:30 AM each day of 2019?)
* Time-sliced TNP usage by census block over time
* Time-sliced E-scooter usage by census block over time
* Weather-sliced congestion by census block over time (i.e. how traffic-congested was census block X when it was sunny during 2019?)
* Weather-sliced TNP usage usage by census block over time
* Weather-sliced E-scooter usage by census block over time
* Aggregate congestion by census block by time slice
* Aggregate TNP usage by census block by time slice
* Aggregate E-scooter usage by census block by time slice
* Congestion vs. TNP usage by census block
* Congestion vs. TNP usage by weather condition
* Congestion vs. E-scooter usage by census block
* Congestion vs. E-scooter usage by weather condition

E-scooter KPIs broken down by weather may or may not be possible, depending on the availability of historical weather data.

## Proposed Dataset(s)

The City of Chicago provides several datasets that allow us to explore these questions:

* **[Historical Congestion Estimates by Segment - 2018-Current](https://data.cityofchicago.org/Transportation/Chicago-Traffic-Tracker-Historical-Congestion-Esti/sxs8-h27x)**; 137M rows. This set includes a selection of Chicago arterial street segments, totaling around 300 miles of roadway, along with estimates of how congested each segment is within a given time slice. Segments are geolocated by latitude/longitude of segment ends.
* **[Transportation Network Providers - Trips](https://data.cityofchicago.org/Transportation/Transportation-Network-Providers-Trips/m6dm-c72p)**; 169M rows. This set includes every trip taken on a Transportation Network Provider (rideshare operator), either starting or ending within Chicago city limits since November 2018. Trips are geolocated by census block of trip start/end.
* **[E-Scooter Trips - 2019 Pilot](https://data.cityofchicago.org/Transportation/E-Scooter-Trips-2019-Pilot/2kfw-zvte)**; 711K rows. This set includes every trip taken on an e-scooter (maintained by a scooter share provider), either starting or ending within Chicago city limits, during Chicago’s 2019 scooter pilot program. Trips are geolocated by census block of trip start/end.

A specific source for weather data is yet to be determined. The City's site offers daily records, which are not sufficiently granular compared to the other data. Weather APIs are still being evaluated, as historical data is proving difficult to find.

## Technical Considerations

### Extract

Initial extract will pull historical congestion data along with 2019 e-scooter pilot data. Ongoing extracts will pull the following:

* **[Live congestion estimates](https://data.cityofchicago.org/Transportation/Chicago-Traffic-Tracker-Congestion-Estimates-by-Se/n4j6-wkkf)**, which update every 15 minutes
* TNP trips, which update either monthly or quarterly; these will need to have a diff applied as there is no "live set" offered
* Weather data, which updates in real time but in practice will be pulled every 15 minutes to match live congestion estimates

### Transform

The datasets in question are not consistently geolocated. TNP and e-scooter trips are located by census block, while congestion estimates and weather measurements are located by latitude/longitude. Therefore we will need to generalize the congestion and weather data from lat/long to census block according to the **[Boundaries - Census Tracts - 2010](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Census-Tracts-2010/5jrd-6zik)** dataset also provided by the City.

### Load

TBD
