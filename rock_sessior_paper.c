#include <stdio.h>

int main(){
        int rock;
        int sessior;
        int paper;
        char select[20];
        char *select1;
        while(1){
                printf("rock ~ sessior ~ paper~~\nexit~~\n");
                scanf("%s", select);
                if(!strcmp("rock", select)){
                        printf("test\n");
                }
                else if(!strcmp("sessior", select)){
                        printf("test1\n");
                }
                else if(!strcmp("paper", select)){
                        printf("test2\n");
                }
                else{
                        printf("bye bye\n");
                        return 0;
                }
        }
}
