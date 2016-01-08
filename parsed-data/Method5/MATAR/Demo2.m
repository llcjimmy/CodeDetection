%% STEP 0: Load Data, Set Default Param
clear;

addpath('../');
dataname='Feature.mat';
load(dataname);
dataname='Label.mat';
load(dataname);
load('WeakPro.mat');

feature=full(feature);
label=full(label);
WeakPro=full(WeakPro);

[N,~]=size(label);
n=round(N*0.1);

train_data=feature(1:N-n,:);
train_label=label(1:N-n,:);
test_data=feature(N-n+1:N,:);
test_label=label(N-n+1:N,:);

WeakProTrain=WeakPro(1:N-n,:);
WeakProTest=WeakPro(N-n+1:N,:);

disp('data load');

Num=70;
Smooth=1; %Set the number of nearest neighbors consider to 10 and the smoothing paremeter to 1

%% STEP 3: Training Small
disp('---------Training: ---------');
tic;
[Prior,PriorN,Cond,CondN,KeyCondLabel,KeyCondLabelN,NKeyCondLabel,NKeyCondLabelN,~]=MLKNN_train_fast(train_data,train_label,Num,Smooth,WeakProTrain);
toc;
%% STEP 4: Evaluation Small
disp('---------Result: ---------');
tic;
[Outputs,Pre_Labels]=MLKNN_test_fast2(train_data,train_label,test_data,Num,Prior,PriorN,Cond,CondN,WeakProTest,KeyCondLabel,KeyCondLabelN,NKeyCondLabel,NKeyCondLabelN);
toc;
mRecall(Outputs,test_label',5)
mRecall(Outputs,test_label',10)
mRecall(Outputs,test_label',20)

mPrecision(Outputs,test_label',5)
mPrecision(Outputs,test_label',10)
mPrecision(Outputs,test_label',20)