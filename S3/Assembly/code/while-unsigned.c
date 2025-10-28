/* ===========================================
 Author : Yann Lemaire--Suau
 GitHub : https://github.com/Malayme
 Date   : 2025-09-24 12:27:28
 File : while-unsigned.c
 =========================================== */
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  unsigned int i = 0;

  while(i <= 10 )
  {
    printf("Valeur de i : %d\n", i);
    i++;
  }
  return EXIT_SUCCESS;
}
