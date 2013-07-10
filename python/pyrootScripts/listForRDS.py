

dataPeriods = [
    "A",
    "A06aug",
    "B",
    "C-v1",
    "C-v2",
    "D",
    ]

sampleList = [
    "DATA",
    #"TT",
    "TT-FullLept",
    "ZZ",
    "DY",
    "DY50-70",
    "DY70-100",
    "DY100",
    "DY180",
    "DY1j",
    "DY2j",
    "DY3j",
    "DY4j",
    "ZH125"
    ]#,"ZH120","ZH115","ZH130","ZH135"]

totsampleList  = [
    "DATA",
    #"TT",
    "TT-FullLept",
    "ZZ",
    "Zbb",
    "Zbx",
    "Zxx",
    "Zno",
    "ZH125"
    ]#,"ZH120","ZH115","ZH130","ZH135"]#,"ZA"]

sigMCsampleList= ["ZH125"]#,"ZH120","ZH115","ZH130","ZH135"]#,"ZA"]
MCsampleList=[]
bkgMCsampleList=[]

for sample in totsampleList :
    if sample=="DATA" : continue
    MCsampleList.append(sample)
    if not sample in sigMCsampleList : bkgMCsampleList.append(sample)

from zbbCommons import zbbnorm
nev_DYjets_summer12=29310189 # to be used on events produced in 532p4
lumi = { "DATA"   : zbbnorm.lumi_tot2012,
         "TT"     : zbbnorm.nev_TTjets_summer12/zbbnorm.xsec_TTjets_8TeV/1000.,
         "TT-FullLept" : zbbnorm.nev_TTFullLept_summer12/zbbnorm.xsec_TTFullLept_8TeV/1000.,
         "Zbb_Zbb"     : zbbnorm.nev_Zbb_summer12/zbbnorm.xsec_Zbb_8TeV/1000.,
         "Zbb"     : zbbnorm.nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
         "Zbx"     : zbbnorm.nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
         "Zxx"     : zbbnorm.nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
         "Zno"     : zbbnorm.nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
#         "Zbb"     : nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
#         "Zbx"     : nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
#         "Zxx"     : nev_DYjets_summer12/zbbnorm.xsec_DYjets_8TeV/1000.,
         "ZZ"     : zbbnorm.nev_ZZ_summer12/zbbnorm.xsec_ZZ_8TeV/1000.,
         "ZH110"  : zbbnorm.nev_ZH110_summer12/zbbnorm.xsec_ZH110_8TeV/1000.,
         "ZH115"  : zbbnorm.nev_ZH115_summer12/zbbnorm.xsec_ZH115_8TeV/1000.,
         "ZH120"  : zbbnorm.nev_ZH120_summer12/zbbnorm.xsec_ZH120_8TeV/1000.,
         "ZH125"  : zbbnorm.nev_ZH125_summer12/zbbnorm.xsec_ZH125_8TeV/1000.,
         "ZH130"  : zbbnorm.nev_ZH130_summer12/zbbnorm.xsec_ZH130_8TeV/1000.,
         "ZH135"  : zbbnorm.nev_ZH135_summer12/zbbnorm.xsec_ZH135_8TeV/1000.
         }


MuCorrFact = 1.0
Extra_norm={ "MuMuChannelDATA"  : 1.0,
             "EEChannelDATA"    : 1.0,
             "MuMuChannelTT"    : 1.0,#(2984./4412.)/MuCorrFact,
             "EEChannelTT"      : 1.0,
             "MuMuChannelTT-FullLept"    : (15000./62506.)/MuCorrFact,
             "EEChannelTT-FullLept"      : 15000./46492.,
	     "MuMuChannelZbb_Zbb"    : (20000./111784.)/MuCorrFact,
             "EEChannelZbb_Zbb"      : 20000./80672.,
	     "MuMuChannelZbb"    : 1.0/MuCorrFact,
             "EEChannelZbb"      : 1.0,
	     "MuMuChannelZbx"    : 1.0/MuCorrFact,
             "EEChannelZbx"      : 1.0,
	     "MuMuChannelZxx"    : 1.0/MuCorrFact,
             "EEChannelZxx"      : 1.0,
	     "MuMuChannelZno"    : 1.0/MuCorrFact,
             "EEChannelZno"      : 1.0,
	     "MuMuChannelZZ"    : (10000./16986.)/MuCorrFact,
             "EEChannelZZ"      : 10000./11936.,
	     "MuMuChannelZH125" : (10000./65412.)/MuCorrFact,
             "EEChannelZH125"   : 10000./48726.,

	     "MuMuChannelZH110" : (10000./58765.)/MuCorrFact,
             "EEChannelZH110"   : 10000./42745.,
	     "MuMuChannelZH115" : (10000./368736.)/MuCorrFact,
             "EEChannelZH115"   : 10000./44633.,
	     "MuMuChannelZH120" : (10000./63643.)/MuCorrFact,
             "EEChannelZH120"   : 10000./46265.,
	     "MuMuChannelZH130" : (10000./68489.)/MuCorrFact,
             "EEChannelZH130"   : 10000./50189.,
	     "MuMuChannelZH135" : (10000./69881.)/MuCorrFact,
             "EEChannelZH135"   : 10000./51567.,
	     "MuMuChannelZH140" : (10000./70994.)/MuCorrFact,
             "EEChannelZH140"   : 10000./52219.,
	     "MuMuChannelZH145" : (10000./73747.)/MuCorrFact,
             "EEChannelZH145"   : 10000./54375.,
	     "MuMuChannelZH150" : (10000./75391.)/MuCorrFact,
             "EEChannelZH150"   : 10000./56013.,

             "MuMuChannelDY50-70" : 4000./6517.,
             "EEChannelDY50-70" : 4000./4615.,
             "MuMuChannelDY70-100" : 2000./3242.,
             "EEChannelDY70-100" : 2000./2304.,
             "MuMuChannelDY100" : 5000./9040,
             "EEChannelDY100" : 5000./6789.,
             "MuMuChannelDY180" : 5000./7281.,
             "EEChannelDY180" : 5000./5648.,
             "MuMuChannelDY1j" : 5000./8655.,
             "EEChannelDY1j" : 5000./5942.,
             "MuMuChannelDY2j" : 15000./38485.,
             "EEChannelDY2j" : 15000./27727.,
             "MuMuChannelDY3j" : 15000./39129.,
             "EEChannelDY3j" : 15000./28325.,
             "MuMuChannelDY4j" : 25000./43536.,
             "EEChannelDY4j" : 25000./32339.,
            }

L_DY = 10325.26
DYlumi = {
    "DY50-70"   : 40626.58,
    "DY70-100"  : 27019.59,
    "DY100"     : 78068.53,
    "DY180"     : 341113.16,
    "DY1j"      : 41506.68,
    "DY2j"      : 119183.18,
    "DY3j"      : 203041.98,
    "DY4j"      : 277900.48,
    }

DYrew={}
for sample in DYlumi:
    for c in ["MuMuChannel","EEChannel"]:
        if sample!="DY180":
            DYrew[c+sample+"Extra_norm"]=str(L_DY/(DYlumi[sample]*Extra_norm[c+sample]+L_DY))
            DYrew[c+sample]=str(L_DY/(DYlumi[sample]+L_DY))
        else :
            DYrew[c+sample+"Extra_norm"]=str(L_DY/(DYlumi[sample]*Extra_norm[c+sample]+DYlumi["DY100"]*Extra_norm[c+"DY100"]+L_DY))
            DYrew[c+sample]=str(L_DY/(DYlumi[sample]+DYlumi["DY100"]+L_DY))            

#SFs_fit_MM={ "MuMuChannelDATA"  : "*1.0",
#          "EEChannelDATA"    : "*1.0",
#          "MuMuChannelTT"    : "*1.03",
#          "EEChannelTT"      : "*1.03",
#          "MuMuChannelTT-FullLept"    : "*1.03",
#          "EEChannelTT-FullLept"      : "*1.03",
#          "MuMuChannelZbb"    : "*( (1.09*(@4==2))+(1.23*(@4>2)) )",
#          "EEChannelZbb"      : "*( (1.09*(@4==2))+(1.23*(@4>2)) )",
#          "MuMuChannelZbx"    : "*1.23",
#          "EEChannelZbx"      : "*1.23",
#          "MuMuChannelZxx"    : "*1.52",
#          "EEChannelZxx"      : "*1.52",
#          "MuMuChannelZno"    : "*1.52",
#          "EEChannelZno"      : "*1.52",
#          "MuMuChannelZZ"    : "*1.0",
#          "EEChannelZZ"      : "*1.0",
#          "MuMuChannelZH125" : "*1.0",
#          "EEChannelZH125"   : "*1.0",
#          }

SFs_fit_MM={ "MuMuChannelDATA"  : "*1.0",
          "EEChannelDATA"    : "*1.0",
          "MuMuChannelTT"    : "*1.01",
          "EEChannelTT"      : "*1.01",
          "MuMuChannelTT-FullLept"    : "*1.01",
          "EEChannelTT-FullLept"      : "*1.01",
          "MuMuChannelZbb"    : "*( (1.12*(@4==2))+(1.26*(@4>2)) )",
          "EEChannelZbb"      : "*( (1.12*(@4==2))+(1.26*(@4>2)) )",
          "MuMuChannelZbx"    : "*1.26",
          "EEChannelZbx"      : "*1.26",
          "MuMuChannelZxx"    : "*1.18",
          "EEChannelZxx"      : "*1.18",
          "MuMuChannelZno"    : "*1.18",
          "EEChannelZno"      : "*1.18",
          "MuMuChannelZZ"    : "*1.0",
          "EEChannelZZ"      : "*1.0",
          "MuMuChannelZH125" : "*1.0",
          "EEChannelZH125"   : "*1.0",
          }

#SFs_fit_ML={ "MuMuChannelDATA"  : "*1.0",
#          "EEChannelDATA"    : "*1.0",
#          "MuMuChannelTT"    : "*1.09",
#          "EEChannelTT"      : "*1.09",
#          "MuMuChannelTT-FullLept"    : "*1.09",
#          "EEChannelTT-FullLept"      : "*1.09",
#          "MuMuChannelZbb"    : "*( (1.05*(@4==2))+(1.21*(@4>2)) )",
#          "EEChannelZbb"      : "*( (1.05*(@4==2))+(1.21*(@4>2)) )",
#          "MuMuChannelZbx"    : "*1.21",
#          "EEChannelZbx"      : "*1.21",
#          "MuMuChannelZxx"    : "*1.49",
#          "EEChannelZxx"      : "*1.49",
#          "MuMuChannelZno"    : "*1.49",
#          "EEChannelZno"      : "*1.49",
#          "MuMuChannelZZ"    : "*1.0",
#          "EEChannelZZ"      : "*1.0",
#          "MuMuChannelZH125" : "*1.0",
#          "EEChannelZH125"   : "*1.0",
#          }

SFs_fit_ML={ "MuMuChannelDATA"  : "*1.0",
          "EEChannelDATA"    : "*1.0",
          "MuMuChannelTT"    : "*1.07",
          "EEChannelTT"      : "*1.07",
          "MuMuChannelTT-FullLept"    : "*1.07",
          "EEChannelTT-FullLept"      : "*1.07",
          "MuMuChannelZbb"    : "*( (1.03*(@4==2))+(1.27*(@4>2)) )",
          "EEChannelZbb"      : "*( (1.03*(@4==2))+(1.27*(@4>2)) )",
          "MuMuChannelZbx"    : "*1.27",
          "EEChannelZbx"      : "*1.27",
          "MuMuChannelZxx"    : "*1.35",
          "EEChannelZxx"      : "*1.35",
          "MuMuChannelZno"    : "*1.35",
          "EEChannelZno"      : "*1.35",
          "MuMuChannelZZ"    : "*1.0",
          "EEChannelZZ"      : "*1.0",
          "MuMuChannelZH125" : "*1.0",
          "EEChannelZH125"   : "*1.0",
          }

PlotForCLsRaw = [
    #"NN_Higgs125vsDY_MM_N_CSV_2011_comb",#1
    #"NN_Higgs125vsZZ_MM_N_CSV_2011_comb",
    #"NN_Higgs125vsTT_MM_N_CSV_2011_comb",
    #"NN_Higgs125vsBKG_MM_N_CSV_2011_comb",
    #"NN_Higgs125vsDY_MM_N_CSV_2012_comb_ZH125",#5
    #"NN_Higgs125vsZZ_MM_N_CSV_2012_comb_ZH125",
    #"NN_Higgs125vsTT_MM_N_CSV_2012_comb_ZH125",
    #"NN_Higgs125vsBkgcomb",

    #"NN_Higgs125vsDY_MM_N_CSV_2012_comb3_2_1_600",
    #"NN_Higgs125vsTT_MM_N_CSV_2012_comb5_2_3_1_500",#10
    #"NN_Higgs125vsZZ_MM_N_CSV_2012_comb2_5_3_1_1000",
    #"NN_Higgs125vsBkgcomb_2_3_2_1_1000",
    #"NN_Higgs125vsBkgcomb_1_10000",
    #"NN_Higgs125vsBkgcomb_1_5000",
    #"NN_Higgs125vsBkgcomb_2_10000",#15
    #"NN_Higgs125vsBkgcomb_2_5000",
    #"NN_Higgs125vsBkgcomb_3_5000",
    #"NN_Higgs125vsBkgcomb_2_3_2_10000",
    #"NN_Higgs125vsBkgcomb_2_3_2_5000",
    #"NN_Higgs125vsBkgcomb_2_4_10000",#20
    #"NN_Higgs125vsBkgcomb_2_5_3_1_1000",
    #"NN_Higgs125vsBkgcomb_3_2_10000",

    "NN_Higgs125vsDYcomb_2_4_1000_Nj2Mbb80_150Pt402520",
    "NN_Higgs125vsZZcomb_2_4_750_Nj2Mbb80_150Pt402520",
    "NN_Higgs125vsTTcomb_5_10_700_Nj2Mbb50_200Pt402520",#25
    "NN_Higgs125vsBkg_2jcomb_2_2_2_500_Nj2Mbb50_200Pt402520",
    "NN_Higgs125vsBkg_2jcomb_6_6_131_Nj2Mbb80_150Pt402520_3",
    "NN_Higgs125vsBkg_2jcomb_9_3_100_Nj2Mbb80_150Pt402520_8",
    "NN_Higgs125vsBkg_2jcomb_9_3_100_Nj2Mbb80_150Pt402520_21",
    "NN_Higgs125vsBkg_2jcomb_2_500_Nj2Mbb80_150Pt402520_1",#30
    #"NN_Higgs125vsDYcombMbbjdRbjdRbb_3_9_500_Nj3Mbb50_150Pt402520",
    #"NN_Higgs125vsZZcombMbbjdRbjdRbb_2_4_501_Nj3Mbb50_150Pt402520",
    #"NN_Higgs125vsTTcombMbbjdRbjdRbb_2_4_500_Nj3Mbb50_150Pt402520",
    "NN_Higgs125vsBkg_3jcomb_4_1000_Nj3_Mbb50_150_Pt402520_4",
    "NN_Higgs125vsBkg_3jcomb_4_1000_Nj3_Mbb50_150_Pt402520_5",#35
    "NN_Higgs125vsBkg_3jcomb_4_1000_Nj3_Mbb50_150_Pt402520_9",
    "NN_Higgs125vsBkg_3jcomb_9_9_300_Nj3_Mbb50_150_Pt402520_4",
    "NN_Higgs125vsBkg_3jcomb_5_600_Nj3_Mbb50_150_Pt402520_1",
  
    #"SumNN",
    #"ProdNN",
    #"SumWeightedNN",
    #"SumNN_2j",
    "ProdNN_2j",
    #"SumWeightedNN_2j",
    #"SumNN_3j",
    "ProdNN_3j",
    #"SumWeightedNN_3j",      
    ]
PlotForCLs = []
for plot in PlotForCLsRaw:
    for m in ["110","115","120","125","130","135","140","145","150"] :
        PlotForCLs.append(plot+"_"+m)
        print plot+"_"+m
blindList = PlotForCLs

namePlotList = [
     "eventSelectionbestzmassMu"  , 
     "eventSelectionbestzmassEle" ,
     "eventSelectionbestzptMu"    ,    
     "eventSelectionbestzptEle"   ,
     "jetmetbjet1pt"              ,   
     "jetmetbjet2pt"              ,   
     "jetmetbjet1CSVdisc"         ,   
     "jetmetbjet2CSVdisc"         ,
     "jetmetbjet1JPdisc"         ,
     "jetmetbjet2JPdisc"         ,
     "jetmetbjet1SSVHEdisc"         ,
     "jetmetbjet2SSVHEdisc"         ,
     "jetmetMET"                  ,
     "jetmetMETsignificance"      ,
     "eventSelectiondphiZbb"      ,
##     "eventSelectiondphiZbj1"     , 
     "eventSelectiondijetPt"      ,
     "eventSelectiondijetM"       ,
     "eventSelectiondijetdR"      ,
##  #   "eventSelectiondijetSVdR"    ,
##     "eventSelectionZbbM"         ,
     "eventSelectiondrllMu"       ,
     "eventSelectiondrllEle"      ,
##     "eventSelectionZbM"          ,
     "jetmetnj"                   ,
     "vertexAssociationnvertices" ,
     "jetmetbjet1beta" ,
     "jetmetbjet1betaStar" ,
     "jetmetbjet2beta" ,
     "jetmetbjet2betaStar",

     "mcSelectionnJets",
     "mcSelectionnbJets",
     "mcSelectionncJets",
     "mcSelectionllpt",
     ]

namePlotListOnMC = [
    "mcSelectionnJets",
    "mcSelectionnbJets",
    "mcSelectionncJets",
    "mcSelectionllpt",
    ]


namePlotListOnMerged = [
     "jetmetbjetMinCSVdisc"   ,   
     "jetmetbjetMaxCSVdisc"   ,
     "jetmetbjetProdCSVdisc"  ,   
     "Wgg"           
     ,"Wqq"           
     ,"Wtt"           
     #    ,"Wtwb"           #to be added in the merged RDS (ttbar isr=0)
     ,"Wzz3"          
     ,"Wzz0"           
     ,"Whi3_125"           
     ,"Whi0_125"
     #,"jetmetMETsignificance"
    # ,"jetmetMET"

#    ,"mlpZbbvsTT_MM"
#    ,"mlpZbbvsTT_MM_N"
#    ,"mlpZbbvsTT_ML"
#    ,"mlpZbbvsTT_mu_MM"
     ,"mlpZbbvsTT_mu_MM_N",
#    ,"mlpZbbvsTT_mu_ML"
    ]
namePlotListOnMerged+=PlotForCLs

################
### minimums ###
################
min = {
    "eventSelectionbestzmassMu" :   60 ,  
    "eventSelectionbestzmassEle":   60 ,  
    "eventSelectionbestzptMu"   :    0 ,
    "eventSelectionbestzptEle"  :    0 ,
    "eventSelectiondijetPt"     :    0 ,
    "eventSelectiondrZbj1"      :    0 ,
    "jetmetbjet1pt"             :    0 ,
    "jetmetbjet2pt"             :    0 ,   
    "jetmetbjet1CSVdisc"        :    0.679 ,
    "jetmetbjet2CSVdisc"        :    0.679 ,   
    "jetmetbjet1JPdisc"        :    0. ,
    "jetmetbjet2JPdisc"        :    0. ,
    "jetmetbjet1SSVHEdisc"        :    0. ,
    "jetmetbjet2SSVHEdisc"        :    0. , 
    "jetmetbjetMinCSVdisc"      :    0.679 ,
    "jetmetbjetMaxCSVdisc"      :    0.679 ,
    "jetmetbjetProdCSVdisc"     :    0.679*0.679 ,
    "jetmetMET"                 :    0 , 
    "eventSelectiondphiZbj1"    :    0 ,
    "eventSelectiondphiZbb"     :    0 ,
    "eventSelectiondrZbb"       :    0 ,
    "eventSelectionscaldptZbj1" : -250 ,
    "eventSelectiondijetM"      :    0 ,
    "eventSelectiondijetdR"     :    0 ,
    "eventSelectiondijetSVdR"   :    0 ,
    "eventSelectionZbbM"        :    0 ,
    "eventSelectionZbM"         :    0 ,
    "eventSelectionZbbPt"       :    0 ,
    "jetmetjet1SSVHPdisc"       :    0 ,
    "jetmetjet1SVmass"          :    0 ,
    "eventSelectiondrllMu"      :    0 ,
    "eventSelectiondrllEle"     :    0 
    ,"jetmetnj" : 2
    ,"vertexAssociationnvertices" : -0.5
    ,"jetmetbjet1beta" : -1
    ,"jetmetbjet1betaStar" : -1
    ,"jetmetbjet2beta" : -1
    ,"jetmetbjet2betaStar" : -1
    
    ,"Wgg"      :    16 
    ,"Wqq"      :    16 
    ,"Wtt"      :    20 
#    ,"Wtwb"      :    20 
    ,"Wzz3"      :    8 
    ,"Wzz0"      :    18
    ,"Whi3_125"      :    11 
    ,"Whi0_125"      :    21 
    ,"jetmetMETsignificance" : 0
    ,"jetmetMET" : 0

    ,"mlpZbbvsTT_MM" : 0
    ,"mlpZbbvsTT_MM_N" : 0
    ,"mlpZbbvsTT_ML" : 0
    ,"mlpZbbvsTT_mu_MM" : 0
    ,"mlpZbbvsTT_mu_MM_N" : 0
    ,"mlpZbbvsTT_mu_ML" : 0,

    "mcSelectionnJets" : -0.5,
    "mcSelectionnbJets" : -0.5,
    "mcSelectionncJets" : -0.5,
    "mcSelectionllpt" : 0,
    }

################
### maximums ###
################
max = {
    "eventSelectionbestzmassMu" :  120 ,  
    "eventSelectionbestzmassEle":  120 ,  
    "eventSelectionbestzptMu"   :  500 ,
    "eventSelectionbestzptEle"  :  500 ,
    "eventSelectiondijetPt"     :  360 ,
    "eventSelectiondrZbj1"      :    5 ,
    "jetmetbjet1pt"             :  260 ,
    "jetmetbjet2pt"             :  250 ,   
    "jetmetbjet1CSVdisc"             :  1 ,
    "jetmetbjet2CSVdisc"             :  1 ,   
    "jetmetbjet1JPdisc"             :  2.5 ,
    "jetmetbjet2JPdisc"             :  2.5 ,   
    "jetmetbjet1SSVHEdisc"             :  10 ,
    "jetmetbjet2SSVHEdisc"             :  10 ,   
    "jetmetbjetMinCSVdisc"             :    1 ,
    "jetmetbjetMaxCSVdisc"             :    1 ,
    "jetmetbjetProdCSVdisc"             :    1 ,
    "jetmetMET"                 :  200 , 
    "eventSelectiondphiZbj1"    :  3.2 ,
    "eventSelectiondphiZbb"     :  3.2 ,
    "eventSelectiondrZbb"       :    5 ,
    "eventSelectionscaldptZbj1" :  250 ,
    "eventSelectiondijetM"      :  240 ,
    "eventSelectiondijetdR"     :    5 ,
    "eventSelectiondijetSVdR"   :    5 ,
    "eventSelectionZbbM"        : 1000 ,
    "eventSelectionZbM"         :  800 ,
    "eventSelectionZbbPt"       :  500 ,
    "jetmetjet1SSVHPdisc"       :    8 ,
    "jetmetjet1SVmass"          :    5 ,
    "eventSelectiondrllMu"      :    5 ,
    "eventSelectiondrllEle"      :    5 
    ,"jetmetnj" :  8
    ,"vertexAssociationnvertices" : 59.5
    ,"jetmetbjet1beta" : 1
    ,"jetmetbjet1betaStar" : 1
    ,"jetmetbjet2beta" : 1
    ,"jetmetbjet2betaStar" : 1
    ,"Wgg"      :    24 
    ,"Wqq"      :    24 
    ,"Wtt"      :    30 
#    ,"Wtwb"      :    24 
    ,"Wzz3"      :    16 
    ,"Wzz0"      :   28
    ,"Whi3_125"      :    21
    ,"Whi0_125"      :    31
    ,"jetmetMETsignificance" : 20
    ,"jetmetMET" : 100

    ,"mlpZbbvsTT_MM" : 1
    ,"mlpZbbvsTT_MM_N" : 1
    ,"mlpZbbvsTT_ML" : 1
    ,"mlpZbbvsTT_mu_MM" : 1
    ,"mlpZbbvsTT_mu_MM_N" : 1
    ,"mlpZbbvsTT_mu_ML" : 1,

    "mcSelectionnJets" : 9.5,
    "mcSelectionnbJets" : 9.5,
    "mcSelectionncJets" : 9.5,
    "mcSelectionllpt" : 500,
    }

################
### binning  ###
################
binning = {
    "eventSelectionbestzmassMu" :   24 , #2GeV 
    "eventSelectionbestzmassEle":   24 ,  
    "eventSelectionbestzptMu"   :   25 , #20GeV
    "eventSelectionbestzptEle"  :   25 ,
    "eventSelectiondijetPt"     :   18 ,
    "eventSelectiondrZbj1"      :   10 , #0.5
    "jetmetbjet1pt"             :   26 , #10GeV
    "jetmetbjet2pt"             :   20 , #12.5GeV   
    "jetmetbjet1CSVdisc"             :  20  ,
    "jetmetbjet2CSVdisc"             :  20  ,
    "jetmetbjet1JPdisc"             :  20  ,
    "jetmetbjet2JPdisc"             :  20  ,
    "jetmetbjet1SSVHEdisc"             :  60  , 
   "jetmetbjet2SSVHEdisc"             :  60  ,
    "jetmetbjetMinCSVdisc"             : 20 ,
    "jetmetbjetMaxCSVdisc"             :   20 ,
    "jetmetbjetProdCSVdisc"             :  20 ,   
    "jetmetMET"                 :   20 , #10GeV 
    "eventSelectiondphiZbj1"    :   16 , #0.2
    "eventSelectiondphiZbb"     :   16 ,
    "eventSelectiondrZbb"       :   10 , #0.5
    "eventSelectionscaldptZbj1" :   50 , #10GeV
    "eventSelectiondijetM"      :   240 , #50GeV
    "eventSelectiondijetdR"     :   10 , #0.5
    "eventSelectiondijetSVdR"   :   10 ,
    "eventSelectionZbbM"        :   20 , #50GeV
    "eventSelectionZbM"         :   16 ,
    "eventSelectionZbbPt"       :   50 , #10GeV
    "jetmetjet1SSVHPdisc"       :   16 ,
    "jetmetjet1SVmass"          :   20 , #0.25GeV
    "eventSelectiondrllMu"      :   10 , #0.5
    "eventSelectiondrllEle"      :   10
    ,"jetmetnj" : 6
    ,"vertexAssociationnvertices" : 60
    ,"jetmetbjet1beta" : 20
    ,"jetmetbjet1betaStar" : 20
    ,"jetmetbjet2beta" : 20
    ,"jetmetbjet2betaStar" : 20
    ,"Wgg"      :    20 
    ,"Wqq"      :    20 
    ,"Wtt"      :    25 
 #   ,"Wtwb"      :    24 
    ,"Wzz3"      :    16 
    ,"Wzz0"      :    20 
    ,"Whi3_125"      :    20 
    ,"Whi0_125"      :    20
    ,"jetmetMETsignificance" : 20
    ,"jetmetMET" : 20

    ,"mlpZbbvsTT_MM" : 20
    ,"mlpZbbvsTT_MM_N" : 10
    ,"mlpZbbvsTT_ML" : 20
    ,"mlpZbbvsTT_mu_MM" : 20
    ,"mlpZbbvsTT_mu_MM_N" : 20
    ,"mlpZbbvsTT_mu_ML" : 20,

    "mcSelectionnJets"  : 10,
    "mcSelectionnbJets" : 10,
    "mcSelectionncJets" : 10,
    "mcSelectionllpt" : 25,
    }
    

for p in PlotForCLs :
    min[p] = 0.
    max[p] = 1.
    binning[p] = 20