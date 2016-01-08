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

disp('data load');

Num=70;
Smooth=1; %Set the number of nearest neighbors consider to 10 and the smoothing paremeter to 1

% %% STEP 3: Training Small
% disp('---------Training: ---------');
% tic;
% [Prior,PriorN,Cond,CondN,KeyCondLabel,KeyCondLabelN,NKeyCondLabel,NKeyCondLabelN]=MLKNN_train_small(feature,label,Num,Smooth,WeakPro);
% toc;
% %% STEP 4: Evaluation Small
% disp('---------Result: ---------');
% tic;
% [Outputs,Pre_Labels]=MLKNN_test_small(feature,label,feature,Num,Prior,PriorN,Cond,CondN,WeakPro,KeyCondLabel,KeyCondLabelN,NKeyCondLabel,NKeyCondLabelN);
% toc;
% mRecall(Outputs,label',5)
% mRecall(Outputs,label',10)
% mRecall(Outputs,label',20)
% 
% mPrecision(Outputs,label',5)
% mPrecision(Outputs,label',10)
% mPrecision(Outputs,label',20)

%% STEP 3: Training Small
disp('---------Training: ---------');
tic;
[Prior,PriorN,Cond,CondN,KeyCondLabel,KeyCondLabelN,NKeyCondLabel,NKeyCondLabelN,T1]=MLKNN_train_fast(feature,label,Num,Smooth,WeakPro);
toc;
%% STEP 4: Evaluation Small
disp('---------Result: ---------');
tic;
[Outputs,Pre_Labels]=MLKNN_test_fast(label,feature,Num,Prior,PriorN,Cond,CondN,WeakPro,KeyCondLabel,KeyCondLabelN,NKeyCondLabel,NKeyCondLabelN,T1);
toc;
mRecall(Outputs,label',5)
mRecall(Outputs,label',10)
mRecall(Outputs,label',20)

mPrecision(Outputs,label',5)
mPrecision(Outputs,label',10)
mPrecision(Outputs,label',20)