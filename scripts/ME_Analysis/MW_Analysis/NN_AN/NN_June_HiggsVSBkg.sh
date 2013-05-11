#! /bin/sh
HOME=~acaudron/
cd /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/NN_537
source /nfs/soft/cms/cmsset_default.sh; export SCRAM_ARCH=slc5_amd64_gcc462 ; source /nfs/soft/grid/ui/setup/grid-env.sh ; source /nfs/soft/crab/setup/crab.sh
cmsenv

#Check for correct number of arguments
if [ $# -lt 2 ]
then
    echo "missing arguments, example : source NN_June_HiggsVSBkg.sh channel"
    echo "channel is : Mu, El or comb"
    echo "mass is : 110, 115, 120, 125, 130, 135, 140, 145 or 150. !!! for the moment use only 125 !!!"
    exit
fi

if [[ -d ${CMSSW_BASE} ]]
then
    echo 'running in CMSSW'
else
    export ROOTSYS=/nfs/soft/root/root-5.34.05-sl5_amd64_gcc41
    #export ROOTSYS=/nfs/soft/root/latest_sl5
    export PATH=$ROOTSYS/bin:$PATH
    export LD_LIBRARY_PATH=$ROOTSYS/lib:$LD_LIBRARY_PATH
    echo 'not running in CMSSW, setup root'
fi

echo ----------- Hello $USER -----------------------
echo "channel is "$1
channel=$1
echo "higgs mass is "$2
mass=$2
echo "struct fo the NN is "$3
struct=$3
echo "number of iterations is "$4
iter=$4

root -l -b > logroot_${mass}_${channel}_${struct}_${iter}.txt << EOF

TString channel("${channel}")
TString mass("${mass}")
TString struct("${struct}")
TString iter("$iter") 
TString DIR("/nfs/user/acaudron/Tree2_537/");
TString fDY("ME_zbb_Zbb_"+channel+"_MC.root")
TString fTT("ME_zbb_TT-FullLept_"+channel+"_MC.root")
TString fZZ("ME_zbb_ZZ_"+channel+"_MC.root")
TString fZH("ME_zbb_ZH"+mass+"_"+channel+"_MC.root")

cout<<"Directory is "<<DIR<<endl;

// Output name
TString NN("ZH"+mass+"_"+channel+"_"+struct+"_"+iter);
cout<<" OUTPUT NAME : "<<NN<<endl;
cout<<" OUTPUT root : ../../NN/NN_Higgs_vs_Bkg_"<<NN<<endl;

// Structure of the NN and nbr of iteration
TString NNStruct=struct.ReplaceAll("_",":");
int iterations=$4;
cout<<"NNStruct "<<NNStruct<<endl;
cout<<"iterations "<<iterations<<endl;

// COmpilation and submission
.L /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/include.h
.L /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/NN_537/Read_input_NN_inputs.h 
.L /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/NN_537/Generic_NN_higgs_NN_inputs.C+

Neural_net_E(DIR+fDY,DIR+fTT,DIR+fZZ,DIR+fZH,NN,NNStruct,iterations)

.q

EOF

grep Epoch logroot_${mass}_${channel}_${struct}_${iter}.txt | sed -e 's/Epoch: //' | sed -e 's/learn=//' |sed -e 's/test=//' > epoch_${mass}_${channel}_${struct}_${iter}.txt

NUMOFPOINTS=$(cat epoch_${mass}_${channel}_${struct}_${iter}.txt| wc -l )
echo "NUMOFPOINTS READ =" $NUMOFPOINTS

root -l -b NN*${mass}*${channel}*${struct}*${iter}*.root << EOF

//This part is copy and paste from the first time we call root

TString channel("${channel}")
TString mass("${mass}")
TString struct("${struct}")
TString iter("$iter") 
TString NN("ZH"+mass+"_"+channel+"_"+struct+"_"+iter);

int numberOfPoints=${NUMOFPOINTS}

cout << "numberOfPoints=" << numberOfPoints << endl;

TString epochinputtxt = "epoch_"+mass+"_"+channel+"_"+struct+"_"+iter+".txt";

TFile* foutput = TFile::Open("NN_Higgs_vs_Bkg_"+NN+".root","UPDATE");

.L /home/fynu/acaudron/scratch/CMSSW_5_3_7/src/UserCode/zbb_louvain/scripts/ME_Analysis/MW_Analysis/NN_AN/ComputeGraphFromTrainTxt.C
ComputeGraphFromTrainTxt(foutput, epochinputtxt, numberOfPoints);
.q
<< EOF
