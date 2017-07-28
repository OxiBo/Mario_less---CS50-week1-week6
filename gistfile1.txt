/**
* CS50 week1 mario_less
*/

#include <stdio.h>
#include <cs50.h>
int main (void) 
{
int height;
int h=1;
do 
{
printf ("height:");
height=get_int();
} 
while (height<0||height>23);
int i=0;
int t=height;
for (i=0; i<height; i++)
{
int s=0;
for (s=0; s<t-1; s++)
{
    printf(" ");
}
int n=0;
for (n=0; n<h+1; n++)
{
    printf("#");
}
h++;
t--;
    printf("\n");
}
}