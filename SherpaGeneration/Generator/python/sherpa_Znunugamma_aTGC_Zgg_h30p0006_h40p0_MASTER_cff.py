import FWCore.ParameterSet.Config as cms
import os

source = cms.Source("EmptySource")

generator = cms.EDFilter("SherpaGeneratorFilter",
  maxEventsToPrint = cms.int32(0),
  filterEfficiency = cms.untracked.double(1.0),
  crossSection = cms.untracked.double(-1),
  SherpaProcess = cms.string('Znunugamma_aTGC_Zgg_h30p0006_h40p0'),
  SherpackLocation = cms.string('./'),
  SherpackChecksum = cms.string('d01d24bf42cc8a241303371d078c4664'),
  FetchSherpack = cms.bool(False),
  SherpaPath = cms.string('./'),
  SherpaPathPiece = cms.string('./'),
  SherpaResultDir = cms.string('Result'),
  SherpaDefaultWeight = cms.double(1.0),
  SherpaParameters = cms.PSet(parameterSets = cms.vstring(
                             "MPI_Cross_Sections",
                             "Run"),
                              MPI_Cross_Sections = cms.vstring(
				" MPIs in Sherpa, Model = Amisic:",
				" semihard xsec = 37.4634 mb,",
				" non-diffractive xsec = 17.0318 mb with nd factor = 0.3142."
                                                  ),
                              Run = cms.vstring(
				" (run){",
				" EVENTS = 1; ERROR 0.1;",
				" FSF:=1.; RSF:=1.; QSF:=1.;",
				" SCALES STRICT_METS{FSF*MU_F2}{RSF*MU_R2}{QSF*MU_Q2};",
				" ME_SIGNAL_GENERATOR Comix;",
				" EVENT_GENERATION_MODE PartiallyUnweighted;",
				" MASSIVE[5] 1",
				" MASSIVE[4] 1",
				" BEAM_1 2212; BEAM_ENERGY_1 6500.;",
				" BEAM_2 2212; BEAM_ENERGY_2 6500.;",
				" PARTICLE_CONTAINER 900[m:-1] gammaZ 22 23;",
				" MODEL NTGC_UFO;",
				"}(run)",
				" (processes){",
				" Process 93 93 -> 900[a] 22;",
				" Decay 900[a] -> 91 91;",
				" Order (*,*,*);",
				" Print_Graphs Process;",
				" Integration_Error 0.02;",
				" End process",
				"}(processes)",
				" (selector){",
				" # phase space cuts for matrix elements",
				" DecayMass 900 30.0 E_CMS;",
				" IsolationCut 22 0.4 1 0.1;",
				" ET  22  150 1200;",
				" PseudoRapidity 22 -2.6 2.6",
				"}(selector)",
				" (ufo){",
				" block yukawa",
				" 1  0.00504     # ymdo",
				" 2  0.00255     # ymup",
				" 3  0.101       # yms",
				" 4  1.27        # ymc",
				" 5  4.7         # ymb",
				" 6  172         # ymt",
				" 11 0.000511    # yme",
				" 13 0.10566     # ymm",
				" 15 1.777       # ymtau",
				" block sminputs",
				" 1  127.9       # aEWM1",
				" 2  1.16637e-05 # Gf",
				" 3  0.1184      # aS",
				" block antgc",
				" 1  0.0          # f4a",
				" 2  0.0          # f4Z",
				" 3  0.0          # f5a",
				" 4  0.0          # f5Z",
				" 5  0.0          # h1a",
				" 6  0.0          # h1Z",
				" 7  0.0006     # h3a",
				" 8  0.0     # h3Z",
				" 9  0.0          # h2a",
				" 10 0.0          # h2Z",
				" 11 0.0     # h4a",
				" 12 0.0     # h4Z",
				" block mass",
				" 23 91.1876     # MZ",
				" 11 0.    # Me",
				" 13 0.     # MMU",
				" 15 1.777       # MTA",
				" 2  0.0     # MU",
				" 4  1.27        # MC",
				" 6  172         # MT",
				" 1  0.0     # MD",
				" 3  0.       # MS",
				" 5  4.7         # MB",
				" 25 125         # MH",
				" decay   23 2.4952      # WZ",
				" decay   24 2.085       # WW",
				" decay   6  1.50833649  # WT",
				" decay   25 0.00407     # WH",
				"}(ufo)"
                                                  ),
                             )
)

ProductionFilterSequence = cms.Sequence(generator)

