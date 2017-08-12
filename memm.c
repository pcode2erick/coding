#include <stdio.h>

#define value1 35
#define value2 47
#define value3 59
#define target 699

int main(){
	
	int i=0,j=0,k=0;
	int closet=1000;
	int X=0,Y=0,Z=0;
	
	for(i=1;i<=9;i++){
		for(j=1;j<=9;j++){
			for(k=1;k<=9;k++){
				if((i*value1+j*value2+k*value3)<=target){
					if((target-(i*value1+j*value2+k*value3))<closet){
						closet=(target-(i*value1+j*value2+k*value3));
						X=i;Y=j;Z=k;
					}
				}
			}
		}

	}
	printf("answer is %d %d %d\n",X,Y,Z);
	printf("Sum is %d \n",X*value1+Y*value2+Z*value3);
	
	return 0;
}