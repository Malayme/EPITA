#include <stdio.h>
#include <stdlib.h>

int * merge(int *tabA, int nA, int *tabB, int nB){
    
    int total_size = nA + nB;
    int *tabC = malloc(sizeof(int) * total_size);

    
    if (tabC == NULL) {
        
        perror("Failed to allocate memory for tabC");
        return NULL;
    }

    int i = 0; 
    int j = 0; 

    
    for(int k = 0; k < total_size; k++){
        
        if(i >= nA){
            tabC[k] = tabB[j];
            j++;
        
        } else if (j >= nB) {
            tabC[k] = tabA[i];
            i++; 
        
        } else if (tabA[i] < tabB[j]){
            tabC[k] = tabA[i];
            i++;
        
        } else {
            tabC[k] = tabB[j];
            j++;
        }
    }
    
    printf("Résultat Merge: ");
    for (int idx = 0; idx < total_size; idx++) {
        printf("%d ", tabC[idx]);
    }
    printf("\n");

    return tabC;
}

int * mergeSort(int * tab, int n){
	if (n <= 1){
		return tab;
	}else{
		int nA = n/2;
		int nB = n-nA;
		int *tabA = malloc(sizeof(int) * nA);
		for(int i=0; i < nA; i++){ tabA[i] = tab[i]; }
		int *tabB = malloc(sizeof(int) * nB);
		for (int i=0; i < nB; i++){ tabB[i] = tab[i + nA]; }
		
		return merge(mergeSort(tabA, nA), nA, mergeSort(tabB, nB), nB);
	}
}

int main(){

    int tab[] = {8, 6, 4, 2};
    int n = 4;

    int *merged_result = mergeSort(tab, n);

    
    if (merged_result != NULL) {
        free(merged_result);
    }

    return 0;
}
