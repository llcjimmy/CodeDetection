addpath('../');

% fid = fopen('allresult.txt','w');
% [m,n]=size(result);
% for i=1:m
%     for j=1:n
%         if j==n
%             fprintf(fid,'%g\n',result(i,j));
%         else
%             fprintf(fid,'%g\t',result(i,j));
%         end
%     end
% end
% fclose(fid);



resulttemp=zeros(45939,50);
for i=1:45939
    [t,ind] = sort(result(i,:),'descend');
    for j=1:50
        resulttemp(i,j)=ind(j);
    end
end

fid = fopen('lastresult.txt','w');
[m,n]=size(resulttemp);
for i=1:m
    for j=1:n
        if j==n
            fprintf(fid,'%g\n',resulttemp(i,j));
        else
            fprintf(fid,'%g\t',resulttemp(i,j));
        end
    end
end
fclose(fid);