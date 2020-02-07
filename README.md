# Tesis_5_AGN_fitter
# Estudio de relación entre las características de AGN cercanos y los modelos de disco de acreción, polvo frío y toro usados para reproducir la distribución espectral de energía.

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
 * To determine the relationship between the physical characteristics of nearby AGNs inferred from high-quality data and the differents models used for accretion disk, cold dust and torus as inputs for the bayesian MCMC code AGNfitter to reproduce the observed spectral energy distribution. This will be important to analyse the current model of AGNs, their components and properties.

## Specific objetives:
 * To identify and choose the set of most relevant physical models for the torus, accretion disk and cold dust for nearby AGNs to be implemented in the bayesian MCMC code AGNfitter to fit the spectral energy distribution.
 
 * To model the spectral energy distribution of a sample of nearby AGNs for which very high-quality data is available over the wavelength range from radio to far UV using the bayesian MCMC code AGNfitter. This will be done using different combinations of the set of chosen physical models for each component as inputs.
 
  * To interpret the physical meaning, uncertainties and limitations of the inferred physical parameters as a plausible description of each host galaxies and its AGNs.
  
  * To determine the global differences in the inferred physical parameters as a function of the underlying models assumed 
  during the fits and its implications they have for the current view of AGNs, their structure and properties.
  
# First draft of the schedule
* (1) Formulation of the proposal [February]
  * Define the tittle of the thesis [1st week February]
  * Search on photometry, photometric filters and how to apply them. [February]
  * Define the test models [February]
  * Write thesis proposal [February]
  * Prepare presentation of thesis proposal [1st-2nd week March]
* (2) Get familiar with the code [March]
  * Run AGNfitter in python2 [March]
  * Test AGNfitter in python3 [March]
  * Necessary math [March]
* (3) Study physical models (theoretical and empirical) and geometries for: [February (proposal)-April-May(deeper)]
  * a) Torus
  * b) Accretion disk
  * c) Cold dust (Distribution of temperatures and grain sizes)
* (4) Get familiar with the data and define specific experiments [May]
  * Stablish assumptions of code (IMF, model of stellar population and evolution) [May]
  * Probe and establish # walkers, #chains and #steps in the method. [May]
  * Write the code for the new physical models and test [May]
  * Check filters in AGNfitter libraries. Add new filter if there is necessary [May]
  * Calculate real fluxes of each component. Prepare data to be input of AGNfitter [May]
* (5) Running experiments [May-June-July]
  * Chose methodology to change the models and first tests [May]
  * Apply AGNfitter to each AGNs, get the parameters, effiency and completeness [June-July]
* (6) Quantifying and analysing the outputs [June-July]
  * Analyse results for each AGN, the characteristics of the host galaxy and AGN components. [June-July]
  * Analyze global results for each component. Determine which parameters change more that other and the physical meaning. [August]
* (7) Manuscript writing [March-September]
  * Final presentation [November]

# Associated repositories
 
 * [AGNfitter](https://github.com/GabrielaCR/AGNfitter)


## Documentation
----------------

The bibliography used to understand the active galactic nuclei (AGN) as a first approximation is:

`Schneider, P. (2014). Extragalactic astronomy and cosmology: an introduction. Springer.`

and a important [document](https://arxiv.org/abs/1606.05648#) that explain AGNfitter:

`Calistro Rivera, Gabriela et al. “AGNfitter: A BAYESIAN MCMC APPROACH TO FITTING SPECTRAL ENERGY DISTRIBUTIONS OF AGNs.” The Astrophysical Journal 833.1 (2016): 98. Crossref. Web.`
