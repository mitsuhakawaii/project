include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

int main()
{
        int str=5;
        int luk=3;
        char yes[20];
        char yes1[20]="yes";
        srand(time(NULL));
        while(1){
                printf("You start spell?\n");
                printf("> ");
                scanf("%s", &yes);
                if(!strcmp(yes, yes1)){
                        if(rand()%3==2){
                                str+=2;
                                luk+=3;
                                printf("str : %d\nluk : %d", str, luk);
                        }
                        else{
                                printf("Fail..\n");
                        }
                }
        }
}
