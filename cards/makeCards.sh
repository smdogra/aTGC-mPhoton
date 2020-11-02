#!/bin/zsh

#CARDDIR=$(cd $(dirname $0); pwd)
#CARDDIR='pwd'
#echo $CARDDIR

CARDDIR=$PWD
echo $CARDDIR
i=1
while IFS= read -r line
do
    test $i -eq 1 && ((i=i+1)) && continue    
    h3a=$(echo $line | awk -F " " '{print$1}')
    h4a=$(echo $line | awk -F " " '{print$2}')
    echo  $h3a $h4a

    h3a_=$(echo ${h3a} | sed -e 's/\./p/' -e 's/-/m/'  -e 's/-/m/')
    h4a_=$(echo ${h4a} | sed -e 's/\./p/' -e 's/-/m/'  -e 's/-/m/')
    CARDLABEL=Znunugamma_aTGC_Zgg_h3${h3a_}_h4${h4a_}_Ptg130to600_2jets
    CARDNAME=${CARDLABEL}    
    DIR=${CARDLABEL}
    mkdir -p $DIR
    cp $CARDDIR/Znunugamma_Monophoton_aTGC_Zgg_h3_h4_Ptg130to600_2jets_extramodels.dat $DIR/${CARDNAME}_extramodels.dat
    cp $CARDDIR/Znunugamma_Monophoton_aTGC_Zgg_h3_h4_Ptg130to600_2jets_run_card.dat $DIR/${CARDNAME}_run_card.dat
    sed -e "s/_h3a_/$h3a/" -e "s/_h4a_/$h4a/"  $CARDDIR/Znunugamma_Monophoton_aTGC_Zgg_h3_h4_Ptg130to600_2jets_customizecards.dat > $DIR/${CARDNAME}_customizecards.dat
    sed "s/_NAME_/$CARDNAME/" $CARDDIR/Znunugamma_Monophoton_aTGC_Zgg_h3_h4_Ptg130to600_2jets_proc_card.dat > $DIR/${CARDNAME}_proc_card.dat
    
    #######################

    h3z=$(echo $line | awk -F " " '{print$1}')
    h4z=$(echo $line | awk -F " " '{print$2}')
    echo  $h3z $h4z

    h3z_=$(echo ${h3z} | sed -e 's/\./p/' -e 's/-/m/'  -e 's/-/m/')
    h4z_=$(echo ${h4z} | sed -e 's/\./p/' -e 's/-/m/'  -e 's/-/m/')
    CARDLABEL2=Znunugamma_aTGC_ZZg_h3${h3z_}_h4${h4z_}_Ptg130to600_2jets
    CARDNAME2=${CARDLABEL2}
    DIR2=${CARDLABEL2}
    mkdir -p $DIR2
    cp $CARDDIR/Znunugamma_Monophoton_aTGC_ZZg_h3_h4_Ptg130to600_2jets_extramodels.dat $DIR2/${CARDNAME2}_extramodels.dat
    cp $CARDDIR/Znunugamma_Monophoton_aTGC_ZZg_h3_h4_Ptg130to600_2jets_run_card.dat $DIR2/${CARDNAME2}_run_card.dat
    sed -e "s/_h3z_/$h3z/" -e "s/_h4z_/$h4z/"  $CARDDIR/Znunugamma_Monophoton_aTGC_ZZg_h3_h4_Ptg130to600_2jets_customizecards.dat > $DIR2/${CARDNAME2}_customizecards.dat
    sed "s/_NAME_/$CARDNAME2/" $CARDDIR/Znunugamma_Monophoton_aTGC_ZZg_h3_h4_Ptg130to600_2jets_proc_card.dat > $DIR2/${CARDNAME2}_proc_card.dat
    
done < massgrid.txt


