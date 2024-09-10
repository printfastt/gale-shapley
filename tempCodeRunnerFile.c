#include <stdio.h>
#include <stdlib.h>
#include "Gale-Shapley.h"
#include <stdbool.h>
#include "cs4050A0.h"

/*
GALE–SHAPLEY (preference lists for hospitals and students) 
INITIALIZE	M to empty matching.
WHILE	(some hospital h is unmatched and hasn’t proposed to every student)
s	 first student on h’s list to whom h has not yet proposed.
IF	(s is unmatched)
Add h–s to matching M.
ELSE IF	(s prefers h to current partner h) Replace h–s with h–s in matching M.
ELSE
s rejects h.

RETURN stable matching M.
*/

bool studentPrefers(int potential_match,  int current_match, Match PessimalPreferences[], int n, int s);

bool studentPrefers(int potential_match,  int current_match, Match PessimalPreferences[], int n, int s){
    for (int i = 0; i<n; i++){
        if(PessimalPreferences[s * n + i].optimal == potential_match){return true;}
        if(PessimalPreferences[s * n + i].optimal == current_match){return false;}       
}
printf("Student doesn't rank h");
return NULL;
}

Match * GaleShapley(char * Optimals[], char * Pessimals[], Match OptimalPreferences[], Match PessimalPreferences[], int n){
   
    Match * matches = (Match *)malloc(n * sizeof(Match));  
    int * proposed = (int *)malloc(n * sizeof(int));
    int * studentMatch = (int *)malloc(n * sizeof(int));
    #define UNMATCHED -1

    for (int i = 0; i<n; i++){
        matches[i].optimal=UNMATCHED;
        matches[i].indexLastProposed=-1;
        studentMatch[i]=UNMATCHED;
    }
    int h = 0;
    while(h<n){
        while(matches[h].optimal==UNMATCHED && matches[h].indexLastProposed<n-1){
            int s = OptimalPreferences[(h*n) + matches[h].indexLastProposed+1].pessimal;
            printf("%s proposes to %s\n",Optimals[h], Pessimals[s]);
              if (studentMatch[s]==UNMATCHED){
                printf("%s accepts %s's proposal b/c was unmatched\n", Pessimals[s], Optimals[h]);
                matches[h].optimal = h;
                matches[h].pessimal = s;
                studentMatch[s] = h; 
            } else if(studentPrefers(h, studentMatch[s], PessimalPreferences, n, s)){
                printf("%s accepts %s's proposal b/c prefer to %s\n", Pessimals[s], Optimals[h],Optimals[studentMatch[s]]);
                matches[studentMatch[s]].optimal=UNMATCHED;
                studentMatch[s] = h;
                matches[h].optimal=h;
                matches[h].pessimal=s;
                matches[h].indexLastProposed++;
                h=-1;
                break;
            } else{
                printf("%s rejects %s's proposal b/c prefer %s to them\n", Pessimals[s], Optimals[h], Optimals[studentMatch[s]]);
                matches[h].indexLastProposed++;
                h-=1;
                break;
            }
                  
            matches[h].indexLastProposed++;     
        }
    h++;
    }


free(proposed);
free(studentMatch);
return matches;
}

