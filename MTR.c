#include <stdio.h>
#include <stdlib.h>
int main(){
    int temp, line[2][2][1]; //= {{'0','0'},{'0','0'}};

    char str[2][2][20] = {{"start from: ","end at: "},{"starting","stopping"}};
    char district[2][10] = {"N","N"};
    char distList[5][5][10] = {{"N","N","K","H","H"},{"K","K","K","K","K"},{"N","N","K","K","K"},{"N","N","N","K","H"},{"H","H","H","H","H"}};
    printf("--------Welcome to the Railway system!-------- \n");
    while (1){
        printf("\n----Menu----\n1. Select a line to ride \n2. Check which lines and stations are available \n3. Exit the program \nYour Choice: ");
        scanf("%d",&temp);
        printf("\n");
        switch(temp){
            case 1:
                for(int i=0;i<2;i++){
                    printf("1. Red Line \n2. Green Line \n3. Purple Line \n4. Yellow Line \n5. Blue Line \n6. Exit \nSelect your line to %s",str[0][i]);
                    scanf("%d",&temp);
                    line[0][i][1] = temp-1;
                    printf("%d",line[0][i][1]);
                    switch (temp){
                        case 1: 
                            printf("Red Line\n1. Tsewn Wan \n2. Lai King \n3. Prince Edward \n4. Admiralty \n5. Central \nSelect your %s station: ",str[1][i]);
                            break;
                        case 2:
                            printf("Green Line\n1. Whampoa \n2. Yau Ma Tei \n3. Kowloon Tong \n4. Kownloon Bay \n5. Tiu King Leng \nSelect your %s station: ",str[1][i]);
                            break;
                        case 3:
                            printf("Purple Line\n1. Tuen Mun \n2. Tswen Wan West \n3. Nam Cheong \n4. East Tsim Sha Tsui \n5. Hung Hom \nSelect your %s station: ",str[1][i]);
                            break;
                        case 4:
                            printf("Yellow Line\n1. Tung Chung \n2. Sunny Bay \n3. Tsing Yi \n4. Olympic \n5. Hong Kong \nSelect your %s station: ",str[1][i]);
                            break;
                        case 5:
                            printf("Blue Line\n1. Kennedy Town \n2. Sheung Wan \n3. Wan Chai \n4. North Point \n5. Chai Wan \nSelect your %s station: ",str[1][i]);
                            break;
                        default:
                            printf("Action Cancelled\n");
                            temp = 0;
                    }
                    if (temp == 0)
                        break;
                    scanf("%d",&temp);
                    line[1][i][1] = temp;
                    district[i][10] = distList[line[0][i][1]][temp-2][10];
                }
                if ((line[0][0][1] == line[0][1][1]) && (district[0][10] == district[1][10]) && (line[1][0][1] == line[1][1][1])){
                    printf("Your starting point cannot be the same as your ending point!\n");
                    break;
                }
                if (temp == 0)
                    break;
                //Farecount
                int fare=5;

                if (((district[0][10] == 'N') && (district[1][10] == 'N')) || ((district[0][10] == 'H') && (district[1][10] == 'H')) || ((district[0][10] == 'K') && (district[1][10] == 'K')))
                    fare += 0;
                else if (((district[0][10] == 'N') && (district[1][10] == 'K')) || ((district[0][10] == 'K') && (district[1][10] == 'N')))
                    fare += 2;
                else if (((district[0][10] == 'H') && (district[1][10] == 'K')) || ((district[0][10] == 'K') && (district[1][10] == 'H')))
                    fare += 3;
                else if (((district[0][10] == 'N') && (district[1][10] == 'H')) || ((district[0][10] == 'H') && (district[1][10] == 'N')))
                    fare += 4;
                if (line[0][0][1] != line[0][1][1])
                    fare += 2;
                printf("The fair is $%d \n",fare);
                
                break;
            case 2:
                printf("----------Avaliable Lines and Stations---------- \nRed Line: Tsewn Wan, Lai King, Prince Edward, Admiralty, Central \n");
                printf("Green Line: Whampoa, Yau Ma Tei, Kowloon Tong, Kownloon Bay, Tiu King Leng \n");
                printf("Purple Line: Tuen Mun, Tsewn Wan West, Nam Cheong, East Tsim Sha Tsui, Hung Hom \n");
                printf("Yellow Line: Tung Chung, Sunny Bay, Tsing Yi, Olympic, Hong Kong \n");
                printf("Blue Line: Kennedy Town, Sheung Wan, Wan Chai, North Point, Chai Wan \n");
                break;
            case 3:
                printf("See you next time!\n");
                exit(0);
            default:
                printf("Please enter a valid option!");
        }
    }
}