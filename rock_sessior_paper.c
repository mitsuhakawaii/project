#include <stdio.h>
#include <time.h>
#include <stdlib.h>
int main(){
        int rock;
        int sessior;
        int paper;
        char select[20];
        char *select1;
        int rand_time;
        while(1){
                printf("rock ~ sessior ~ paper~~\nexit~~\n");
                scanf("%s", select);
                srand(time(NULL));
                if(!strcmp("rock", select)){
                        rand_time = rand()%2;
                        if(rand_time==1){
                                printf("you lose..\n");
                                return 0;
                        }
                        else if(rand_time==2){
                                printf("same?~\n");
                        }
                        else{
                                printf("you win!\n");
                        }
                }
                else if(!strcmp("sessior", select)){
                        printf("test1\n");
                         rand_time = rand()%2;
                        if(rand_time==1){
                                printf("you lose..\n");
                                return 0;
                        }
                        else if(rand_time==2){
                                printf("same?~\n");
                        }
                        else{
                                printf("you win!\n");
                        }

                }
                else if(!strcmp("paper", select)){
                        printf("test2\n");
                         rand_time = rand()%2;
                        if(rand_time==1){
                                printf("you lose..\n");
                                return 0;
                        }
                        else if(rand_time==2){
                                printf("same?~\n");
                        }
                        else{
                                printf("you win!\n");
                        }

                }
                else{
                        printf("bye bye\n");
                        return 0;
                }
        }
}
