#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct point {
    char nom;
    float x;
    float y;
};

void init(struct point ***, int);
void afficher(struct point **, int);

int main() {
    int nb;
    struct point** plan;
    scanf("%d", &nb);
    init(&plan, nb);
    afficher(plan, nb);
}

void afficher(struct point **plan, int nb) {
    for (int i=0; i<nb; i++) {
        printf("Point nom: %c ; x: %f ; y: %f\n", plan[i]->nom, plan[i]->x, plan[i]->y);
    }
}

void init(struct point ***plan, int nb) {
    *plan = malloc(nb * sizeof(struct point*));
    
    for (int i=0; i<nb; i++) {
        (*plan)[i] = malloc(sizeof(struct point));
        // ou *(*plan + i) = ...

        struct point* p = (*plan)[i];
        scanf(" %c %f %f", &(p->nom), &(p->x), &(p->y));
    }
}