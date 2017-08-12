public class gd{

public static void main(String []args){
double []y={4.02,5.96,7.0,10.04,10.14};
int []x={4,8,10,16,18};
double a=0.8,b=0.7,sum,sum2;
for(int j=0;j<5;j++){
	sum=0;sum2=0;
for(int i=0;i<5;i++){
	sum=sum+(a+b*x[i]-y[i]);
	sum2=sum2+((a+b*x[i]-y[i])*x[i]);
}
sum=a-sum*(0.02/5);
sum2=b-sum2*(0.02/5);
a=sum;
b=sum2;
System.out.println("iteration "+j);
System.out.println("sum: "+sum);
System.out.println("sum2: "+sum2);
}
}
}
