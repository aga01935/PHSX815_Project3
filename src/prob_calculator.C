#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include "TH1D.h"
#include "TFile.h"

using namespace std;
vector<int> GetLineValues(std::string& line);

void prob_calculator(string inFileName0,string inFileName1){

 string line;
 vector<int> lineVals;

 int Nmeas;
 int Nexp;
 string InputFile[2];

 InputFile[0] = inFileName0;
 InputFile[1] = inFileName1;
 int Ncount_max = 0;

 vector<double> count[2];
 vector<vector<double> > counts[2];
 //cout << "infileName: "<< InputFile[0]<<","<< InputFile[1]<< endl;
 // read in experiment times
 for(int h = 0; h < 2; h++){
   //cout<< InputFile[h]<< endl;
   ifstream ifile(InputFile[h].c_str());
   if(!ifile.is_open()){
     cout << "Unable to read input data file " << InputFile[h] << std::endl;
     //return 0;
   }

   int iexp = 0; // count number of experiments
   getline(ifile,line);
   while(getline(ifile, line)){

     lineVals = GetLineValues(line);

     // number of measurements in this experiment
     Nmeas = lineVals.size();
     //cout<<"number of measurement is :" <<Nmeas << endl;
     // add a new vector for this experiment
     counts[h].push_back(vector<double>());
     for(int i = 0; i < Nmeas; i++){
 count[h].push_back(lineVals[i]);
 counts[h][iexp].push_back(lineVals[i]);
 if(lineVals[i] > Ncount_max)
   Ncount_max = lineVals[i];
     }
     iexp++;
   }
   //cout<<"number of experiment is :" <<iexp << endl;
   ifile.close();
 }

 // first, we use our simulated data to build the *probability distribution* for the
 // number of missing cookies for a single measurement (integrating over all nuisances implicitly)
 // we represent these probability distributions with histograms
 TH1D* prob_H0 = new TH1D("prob_H0", "prob_H0",
        Ncount_max+1, -0.5, Ncount_max+0.5);
 TH1D* prob_H1 = new TH1D("prob_H1", "prob_H1",
        Ncount_max+1, -0.5, Ncount_max+0.5);

 for(auto c : count[0])
   prob_H0->Fill(c);
 for(auto c : count[1])
   prob_H1->Fill(c);

 // normalize histograms to make PDFs
 prob_H0->Scale(1./prob_H0->Integral());
 prob_H1->Scale(1./prob_H1->Integral());

 prob_H0->Draw();
 prob_H1->Draw();
 vector<double> LLR[2]; // Log Likelihood Ratios for each hypothesis, vector of experiments

 // construct vector of likelihood ratios for each experiment, for each hypothesis
 for(int h = 0; h < 2; h++){ // loop over hypotheses
    Nexp = counts[h].size();
   for(int e = 0; e < Nexp; e++){ // loop over experiments
     Nmeas = counts[h][e].size();
     double LogLikeRatio = 0;
     bool ok_LLR = true;
     for(int m = 0; m < Nmeas; m++){ // loop over times in an experiment
 double prob_of_H0 = prob_H0->GetBinContent(prob_H0->FindBin(counts[h][e][m]));
 double prob_of_H1 = prob_H1->GetBinContent(prob_H1->FindBin(counts[h][e][m]));
 if(prob_of_H0 > 0 && prob_of_H1 > 0){
   LogLikeRatio += log(prob_of_H1); // Log-like for H1
   LogLikeRatio -= log(prob_of_H0); // Log-like for H0
 } else {
   ok_LLR = false;
 }
     }
     if(ok_LLR)
 LLR[h].push_back(LogLikeRatio);
   }
 }
 ofstream outfile[2];
   //cout << "checking of probability is 1" << checkbin/bin_width << endl;

   for(int h = 0; h < 2; h++){ // loop over hypotheses
   string outfilename = "prob_"+InputFile[h];
   outfile[h].open(outfilename.c_str());
   for(int e = 0; e < Nexp; e++){
    // for(int k =0; k<Nmeas;k++){
        outfile[h]<< LLR[h][e] << " ";

     //}
    }
    outfile[h].close();
  }
}

vector<int> GetLineValues(std::string& line){
  // remove leading whitespace
  while(line[0] == string(" ")[0])
    line.erase(0,1);

  vector<int> ret;
  string num;
  while(line.find(" ") != string::npos){
    size_t p = line.find(" ");
    num = line.substr(0,p);
    line.erase(0,p+1);
    while(line[0] == string(" ")[0])
      line.erase(0,1);

    ret.push_back(stoi(num));
  }

  return ret;
}
