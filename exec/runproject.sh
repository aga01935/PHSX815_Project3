#! /usr/bin/env python3
rm ${4:-"H0.txt"}
rm ${6:-"H1.txt"}
python3 $PWD/python/Simulator.py -Nexp ${1:-30} -Nmes ${2:-200}  -seed ${3:-4000} -output ${4:-"H0.txt"} -cause ${5:-"HF"}
python3 $PWD/python/Simulator.py -Nexp ${1:-30} -Nmes ${2:-200}  -seed ${3:-4000} -output ${6:-"H1.txt"} -cause ${7:-"ED"}
#echo $7
#echo $5
root -l -b -q $PWD/src/prob_calculator.C\(\"H0.txt\",\"\H1.txt\"\)
#root -l -b -q $PWD/src/prob_calculator.C\(\"H1.txt\"\)
python3 $PWD/python/ElectricityUse.py -input0 ${5:-H0.txt} -input1 ${7:-H1.txt}
