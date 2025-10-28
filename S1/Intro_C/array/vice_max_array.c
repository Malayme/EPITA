#include <stdio.h>
#include <limits.h>
#include <stddef.h>
#include <stdlib.h>
 
 int vice_max_array(const int vec[], size_t size)
 {
     if (vec == NULL && size < 2)
     {
         return (INT_MIN);
     }
 
     int vice_max_value = vec[0];
     int max_value = vec[0];
     size_t i = 1;
 
     while (i < size)
     {
         if (vec[i] > max_value)
         {
             vice_max_value = max_value;
             max_value = vec[i];
         }
         else if (vec[i] > vice_max_value && vec[i] != max_value)
         {
             vice_max_value = vec[i];
         }
         i++;
     }
 
     return vice_max_value;
 }
 
 int main(int argc, char *argv[])
 {
     if (argc < 2)
     {
         return (0);
     }
 
     int nbr[argc - 1];
     int i = 1;
 
     while (i < argc)
     {
         nbr[i - 1] = atoi(argv[i]);
         i++;
     }
 
     int vice_max_value = vice_max_array(nbr, argc - 1);
     printf("The vice max value is : %d\n", vice_max_value);
 
     return (0);
 }

