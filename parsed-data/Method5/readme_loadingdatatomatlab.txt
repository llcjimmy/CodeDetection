load('QuestionsFeature.txt');
QuestionsFeature = sparse(QuestionsFeature(:,1),QuestionsFeature(:,2),QuestionsFeature(:,3));

QuestionsFeature= full(QuestionsFeature);

load('QuestionsLabel.txt');
QuestionsLabel = sparse(QuestionsLabel(:,1),QuestionsLabel(:,2),QuestionsLabel(:,3));

QuestionsLabel= full(QuestionsLabel);

label = QuestionsLabel;
feature = QuestionsFeature;


load('WeakPro.txt');
WeakPro = sparse(WeakPro(:,1),WeakPro(:,2),WeakPro(:,3));
WeakPro = full(WeakPro);

A = zeros(19953,13);
WeakPro = [WeakPro A];
save('WeakPro.mat','WeakPro','-v7.3');