function [] = Lab_9()
    data = xlsread("data_nums.xlsx");
    [centers,U] = fcm(data, 3);

    maxU = max(U);
    index1 = find(U(1,:) == maxU);
    index2 = find(U(2,:) == maxU);
    index3 = find(U(3,:) == maxU);
    
    plot(data(index1,1),data(index1,2),'ob')
    hold on
    plot(data(index2,1),data(index2,2),'or')
    plot(data(index3,1),data(index3,2),'og')
    plot(centers(1,1),centers(1,2),'xb','MarkerSize',15,'LineWidth',3)
    plot(centers(2,1),centers(2,2),'xr','MarkerSize',15,'LineWidth',3)
    plot(centers(3,1),centers(3,2),'xg','MarkerSize',15,'LineWidth',3)
    hold off
end