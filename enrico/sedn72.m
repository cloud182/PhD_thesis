set(0,'DefaultAxesFontSize',16)
%load synchrtr.dat
%x=synchrtr(:,1);
%y=synchrtr(:,2);
%plot(x,y+4.,'k.')
%hold on
load fort12g.dat
x=fort12g(:,1);
y=fort12g(:,2);
plot(x,y-9.5,'k-.')
hold on
load fort12d.dat
x=fort12d(:,1);
y=fort12d(:,2);
plot(x,y-11.2,'k-.')
hold on
load fortsync.dat
x=fortsync(:,1);
y=fortsync(:,2);
plot(x,y-10.7,'k-')
hold on
hold on
load fort12_600d.dat
x=fort12_600d(:,1);
y=fort12_600d(:,2);
plot(x,y-11.2,'k--')
hold on
load fort12_600g.dat
x=fort12_600g(:,1);
y=fort12_600g(:,2);
plot(x,y-10.5,'k--')
hold on
load fort12_100g.dat
x=fort12_100g(:,1);
y=fort12_100g(:,2);
plot(x,y-8.,'k-')
hold on
hold on
load fort12_100d.dat
x=fort12_100d(:,1);
y=fort12_100d(:,2);
plot(x,y-10.0,'k-')
hold on
hold on
load fort18.dat     
x=fort18(:,1);
y=fort18(:,2);
plot(x,y-13.3,'k-')
hold on
load fort113_ic3.dat
x=fort113_ic3(:,1);
y=fort113_ic3(:,2);
plot(x,y-19.1,'r-')
hold on
hold on
load fort113_ic2.dat
x=fort113_ic2(:,1);
y=fort113_ic2(:,2);
plot(x,y-13.5,'r--')
hold on
load ic50sed.dat      
x=ic50sed(:,1);
y=ic50sed(:,2);
%plot(log10(x),log10(y)+0.89,'ko')
hold on
load n7212cont.dat    
x=n7212cont(:,1);
y=n7212cont(:,2);
plot(log10(x),log10(y)+0.89,'ko')
axis([7. 20. -16.5 -8.])
xlabel('log \nu [Hz]')
ylabel('log \nu F_{\nu} [erg cm^{-2} s^{-1}]')
