#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

struct Person {
	char name[100];
	int age;
	char address[1000];
};
int main()
{
	int roopVar;
	int roopVarArray;
	int select;
	int roopVarArray1;
	struct Person person[1000];
	char response[100];
	char response1[100] = "YES";
	int roopVarArray2;
	while(1)
	{
		printf("Please enter the number of information to be entered.\n");
		printf("1. Input information\n");
		printf("2. Print information\n");
		printf("3. Exit\n");	
		scanf("%d", &select);
		if(select == 1)
		{	
			printf("Roop : ");
			scanf("%d", &roopVar);
			for(roopVarArray = 1; roopVarArray <= roopVar; roopVarArray++)
			{
				printf("Name : ");
				scanf("%s", person[roopVarArray1].name);
				printf("\n");
				printf("age : ");
				scanf("%d", &person[roopVarArray].age);
				printf("address : ");
				scanf("%s", person[roopVarArray].address);
			}
		}

		else if(select == 2)
		{
			for(roopVarArray1 = 1; roopVarArray1 <= roopVar; roopVarArray1++)
			{
				printf("%s\n", person[roopVarArray1].name);
				printf("%d\n", person[roopVarArray1].age);
				printf("%s\n", person[roopVarArray1].address);
				
			}
		}
		
		else if(select == 3)
		{
			printf("Bye Bye~\n");
			exit(1);
		}
	}
}
