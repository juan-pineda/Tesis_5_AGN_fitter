# Tesis_5_AGN_fitter

## Comparación de modelos físicos de emisión multi-onda de núcleos activos de galaxias a partir de su distribución espectral de energía
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

To monitor and manage the thesis progress please go to the [project board](https://github.com/users/juan-pineda/projects/5).


# Problem Statement

In this thesis we propose to investigate how the physical parameters inferred from data that comes from nearby AGN change using differents models used for accretion disk, cold dust and torus as inputs for the bayesian MCMC code AGNfitter used to reproduce the spectral energy distribution of AGNs. 


# Objectives

## General objetive:
 * Comparing the physical properties of a sample of AGNs in z < 0.7 from modeling their spectral energy distributions by varying the physical emission models

## Specific objetives:
 * To identify the most relevant set of physical models for the torus, accretion disk and cold dust to be implemented in the fit of the spectral energy distributions
 
 * To model the observed spectral energy distribution of a sample of AGNs in z < 0.7 from radio wavelengths to X-rays using the Bayesian AGNfitter code.
 
  * To analyze the probability distributions of the physical parameters associated with each of the models with emphasis on their physical interpretation
  
  * To quantify the overall differences in the results of the fits made for the entire AGN sample
  
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

# Table of contents of the proposal 
  * 1) Abstract
  * 2) Introduction
  * 3) Theoretical framework
    * 3.1) Active galaxy nuclei
      * 3.1.1) Accretion disk
      * 3.1.2) Torus
      * 3.1.3) Host galaxy
    * 3.2) Spectral energy distribution
      * 3.2.1) AGN spectral energy distribution (Big blue bump, Infrarred bump)
    * 3.3) AGNfitter
      * 3.3.1) Physical models for four emission components
      * 3.3.2) Outputs: physical and amplitude parameters
    * 3.4) Bayesian MCMC
  * 4) Problem statement
  * 5) Objectives
     * 5.1) General objective
     * 5.2) Specific objectives
  * 6) Methodology
     * 6.1) Schedule
  * 7) Bibliography



# Associated repositories
 
 * [AGNfitter](https://github.com/GabrielaCR/AGNfitter)


## Documentation
----------------

The bibliography used to understand the active galactic nuclei (AGN) as a first approximation is:

`Schneider, P. (2014). Extragalactic astronomy and cosmology: an introduction. Springer.`

and an important [document](https://arxiv.org/abs/1606.05648#) that explain AGNfitter:

`Calistro Rivera, Gabriela et al. “AGNfitter: A BAYESIAN MCMC APPROACH TO FITTING SPECTRAL ENERGY DISTRIBUTIONS OF AGNs.” The Astrophysical Journal 833.1 (2016): 98. Crossref. Web.`

Data is available on: 

https://archive.stsci.edu/hlsp/agnsedatlas#section-2e53544e-eae6-4a7a-bf4c-45df17de56d4

and the details of the data in the following [paper](https://arxiv.org/pdf/1908.03720.pdf):

`Brown, M. J. I., Duncan, K. J., Landt, H., Kirk, M., Ricci, C., Kamraj, N., ... & Ananna, T. (2019). The spectral energy distributions of active galactic nuclei. Monthly Notices of the Royal Astronomical Society, 489(3), 3351-3367.`
