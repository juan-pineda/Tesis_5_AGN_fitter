# Tesis_5_AGN_fitter
---------------------

In this repository it is available the information associated with my undergraduate thesis: objectives, schedule, data, codes and documents. This thesis is a part of the project [AGNfitter](https://github.com/GabrielaCR/AGNfitter) which consist of a Python algorithm implementing a fully Bayesian MCMC method to fit the spectral energy distributions (SEDs) of active galactic nuclei (AGN) and galaxies from the sub-mm to the UV. The main purpose is robustly disentangle the physical processes responsible for the emission of the sources.

# Participants:

  * Juan Carlos Basto Pineda (juan.basto.pineda@gmail.com)
  * Luis A. Nuñez (lnunez@uis.edu.co)
  * Gabriela Calistro (gabriela.calistrorivera@eso.org)
  * Laura Natalia Martínez Ramírez (laura.martinez13@correo.uis.edu.co)
  
# Repository content

  * /Latex : This folder contains the documents in latex format created for this project and its pdf version.
  * /Tests : This folder contains the test codes with the changes made to AGNfitter.
  * /Bibliography : This foldes contains all the papers and books needed to do the bibliographic review for my thesis.
  
# Project management

To monitor and manage the thesis progress please go to the project board.


# Problem Statement

In this thesis we propose to investigate how the physical parameters inferred from data that comes from nearby AGN change using differents models used for accretion disk, cold dust and torus as inputs for the bayesian MCMC code AGNfitter used to reproduce the spectral energy distribution of AGNs. 


# Objectives

## General objetive:
 * Determine the relation between physical characteristics inferred from data of nearby AGN and differents models used for accretion disk, cold dust and torus as inputs for the bayesian MCMC code AGNfitter (the most recent version) to reproduce the observed spectral energy distribution. 

## Specific objetives:
 * Define the suitable set of physical models for the torus, accretion disk and cold dust for nearby AGNs to be implemented in AGNfitter to fit the spectral energy distribution.
 
 * Modelling the spectral energy distribution of a sample of 48 nearby AGNs for which very high-quality data is available over the wavelength range from radio to far UV using the bayesian MCMC code AGNfitter and the chosen physical models for the torus, accretion disk and cold dust as inputs.
 
  * Evaluate the photometric data sets of the nearby AGN to chose the filter curves required to calculate the actual fluxes of each spectral band in each AGN.
 
  * Generate a catalogue of parameters for each physical model in each of the three emission processes studied from the results obtained when applying AGNfitter to the data set.
  
  * Evaluate the set of models leading to the best fit of the spectral energy distribution of the data set and its physical implications.
  
  
# First draft of the schedule
 * Run AGNfitter in python2 [2nd week February]
 * Test AGNfitter in python3 [2nd-3rd weeks February]
 * Define the tittle of the thesis [February]
 * Write thesis proposal [February-1sr week march]
 * Prepare presentation of thesis proposal [March]
 * (1) Study physical models (theoretical and empirical) and geometries for: [February (proposal)-April-May(deeper)]
    * a) Torus
    * b) Accretion disk
    * c) Cold dust (Distribution of temperatures and grain sizes)
 * (1) Stablish assumptions of code (IMF, model of stellar population and evolution) [April-May]
 * (1) Define the test models [February]
 * (1) Write the code for the new physical models and test [May]
 * (2) Search on photometry, photometric filters and how to apply them. [February]
 * (2) Evaluate data, wavelenght, type of telescope and bandwidth [June]
 * (2) Check filters in AGNfitter libraries. Add new filter if there is necessary [June]
 * (2) Calculate real fluxes of each component. Prepare data to be input of AGNfitter [July]
 * (3) Probe and establish # walkers, #chains and #steps in the method. [July]
 * (3) Chose methodology to change the models and first tests [July]
 * (3) Apply AGNfitter to each AGNs, get the parameters, effiency and completeness [August-September]
 * (4) Analyze results for each component. Determine which parameters change more that other and the physical meaning. [October]
    * a) Torus
    * b) Accretion disk
    * c) Cold dust
 * Write the thesis [March-October]
 * Final presentation [November]
 * Paper of last version of AGNfitter [to be defined]

# Associated repositories
 
 * [AGNfitter](https://github.com/GabrielaCR/AGNfitter)


## Documentation
----------------

The bibliography used to understand the active galactic nuclei (AGN) as a first approximation is:

`Schneider, P. (2014). Extragalactic astronomy and cosmology: an introduction. Springer.`

and a important [document](https://arxiv.org/abs/1606.05648#) that explain AGNfitter:

`Calistro Rivera, Gabriela et al. “AGNfitter: A BAYESIAN MCMC APPROACH TO FITTING SPECTRAL ENERGY DISTRIBUTIONS OF AGNs.” The Astrophysical Journal 833.1 (2016): 98. Crossref. Web.`
