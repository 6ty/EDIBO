using System;

    public class DecToBin
    {
        public static void Main(string[] args)
        {

            int n, i;
            int[] a = new int[10];

            Console.Write("Ievadiet skaitli parveidošanai:");
            
            n= int.Parse(Console.ReadLine());

                for(i=0;n>0;i++){
                    a[i]=n%2;
                    n=n/2;
                }

            Console.Write("Binarī šis skaitlis būs= ");

                for(i=i-1 ;i>=0;i--){
                    Console.Write(a[i]);
                }
        }
    }