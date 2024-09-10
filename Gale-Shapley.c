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


//studentPrefers returns true if, going in order down student preferences, the potential match is found first (potential preferred)
//               returns false if, going in order down student preferences, the current match is found first (current preffered)
bool studentPrefers(int potential_match,  int current_match, Match PessimalPreferences[], int n, int s){
    for (int i = 0; i<n; i++){
        if(PessimalPreferences[s * n + i].optimal == potential_match){return true;}
        if(PessimalPreferences[s * n + i].optimal == current_match){return false;}       
}
//if for some reason the student doesnt have a rank for both hospitals.
printf("Student doesn't rank h");
return NULL;
}

Match * GaleShapley(char * Optimals[], char * Pessimals[], Match OptimalPreferences[], Match PessimalPreferences[], int n){
   
    Match * matches = (Match *)malloc(n * sizeof(Match)); //initialize empty matching
    int * studentMatch = (int *)malloc(n * sizeof(int)); //array of current student matches so matches array does not have to be searched.
    #define UNMATCHED -2    //arbitrary value

    //initialization
    for (int i = 0; i<n; i++){
        matches[i].optimal=UNMATCHED;
        matches[i].indexLastProposed=-1; //starts at -1 so the increment operator for s declaration doesn't skip the first student.
        studentMatch[i]=UNMATCHED;
    }
    int h = 0;
    while(h<n){
        while(matches[h].optimal==UNMATCHED && matches[h].indexLastProposed<n-1){                   //while hospital h is unmatched and not every student has been proposed to.
            int s = OptimalPreferences[(h*n) + matches[h].indexLastProposed+1].pessimal;            //choose next student from hospital preference list. 
            printf("%s PROPOSES TO %s\n",Optimals[h], Pessimals[s]);
              if (studentMatch[s]==UNMATCHED){                                                      //if student does not have a match
                printf("%s accepts %s's proposal b/c previously unmatched\n\n", Pessimals[s], Optimals[h]);
                matches[h].optimal = h;                                                             //set pair
                matches[h].pessimal = s;                                                            //set pair
                studentMatch[s] = h;                                                                //update our studentmatch array
            } else if(studentPrefers(h, studentMatch[s], PessimalPreferences, n, s)){               //call studentprefers function to see if the student prefers the current h over its match.
                printf("%s accepts %s's proposal b/c prefer to %s\n\n", Pessimals[s], Optimals[h],Optimals[studentMatch[s]]);
                matches[studentMatch[s]].optimal=UNMATCHED;                                         //if he does, change the hospital back to unmatched.
                studentMatch[s] = h;                                                                //update our studentmatch array
                matches[h].optimal=h;                                                               //set pair
                matches[h].pessimal=s;                                                              //set pair
                matches[h].indexLastProposed++;                                                     //increment last proposed index.
                h=-1;                                                                               //start at beginning of hospital list.
                break;                                                                              //break so we do not undo our decrement with the outer for loop's increment.
            } else{
                printf("%s rejects %s's proposal b/c prefer %s to them\n\n", Pessimals[s], Optimals[h], Optimals[studentMatch[s]]);
                matches[h].indexLastProposed++;
                h=-1;                                                                               //start at beginning of hospital list.
                break;                                                                              
            }   
                  
            matches[h].indexLastProposed++;     
        }
    h++;
    }
free(studentMatch);
return matches;
}

