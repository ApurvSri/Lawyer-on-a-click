#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX_CMN_LEN 100

int main(int argc, char *argv[])
{
	char ch;
        char cmd[MAX_CMN_LEN] = "", **p;
	printf("\nWelcome ");
	if (argc < 2) 
        {
                printf("Usage: ./program_name terminal_command");
                exit(EXIT_FAILURE);
        }
        else
        {
                strcat(cmd, argv[1]);
                for (p = &argv[2]; *p; p++)
                {
                        strcat(cmd, " ");
                        strcat(cmd, *p);
                }
                system(cmd);
        }
	FILE *fp;
	printf("\n\n\n");
	fp = fopen("data1.txt","r");
	while((ch = fgetc(fp)) != EOF) {
		printf("%c",ch);
	}
	return 0;
}

