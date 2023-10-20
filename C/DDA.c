#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<math.h>
void main()
{
int gd=DETECT,gm,x1,y1,x2,y2,dx,dy,s1,s2,f=0,dpd,x,y,t,i,dpd1;
clrscr();
printf("Enter start coordinates:\n");
scanf("%d%d",&x1,&y1);
printf("Enter end coordinates:\n");
scanf("%d%d",&x2,&y2);
initgraph(&gd,&gm,"..//BGI");
x=x1;
y=y1;
dx=fabs(x2-x1);
dy=fabs(y2-y1);
putpixel(x1,y1,10);
if(x2-x1<0)
s1=-1;
else if((x2-x1)>0)
s1=1;
else
s1=0;
if(y2-y1<0)
s2=-1;
else if(y2-y1>0)
s2=1;
else
s2=0;
dpd=(2*dy)-dx;
dpd1=dpd;
if(dy>dx)
{
f=1;
t=dy;
dy=dx;
dx=t;
}
for(i=0;i<=dx;i++)
{
if(dpd1<0)
{
if(f==0)
{
y=y;
x=x+s1;
}
else{
x=x;
y+=s2;
}
dpd1=dpd1+(2*dy);}
else{
x+=s1;
y+=s2;
dpd1+=2*dy-2*dx;
}
putpixel(x,y,WHITE);
}
getch();
closegraph();
}
