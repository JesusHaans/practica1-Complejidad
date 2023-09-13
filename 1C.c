#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Definiremos unas contantes para el programa
#define NOMBRE_ARCHIVO "ENTRADA1.txt"
#define LONGITUD_MAXIMA_DE_LINEA 199
#define LONGITUD_MAXIMA_DE_VERTICES 100
#define LONGITUD_MAXIMA_DE_ARISTAS 4950 // n(n-1)/2 siendo n el numero de vertices

//Definiremos la estructura de las aristas y Vertices de las graficas
struct Arista{
    int V1;
    int V2;
};

struct Vertice{
    int V;
};

struct Grafica{
    /* data */
    struct Vertice* Vertices;
    struct Arista* Aristas;
};

//Funcion para agregar los vertices
void agregarVertices(char* Linea, struct Vertice* Vertices){
    char
    for(int i = 0 ; i < LONGITUD_MAXIMA_DE_LINEA ; i++){
        if(Linea[i] == '\n'){
            printf("Se encontro un salto de linea\n");
            break;
        }
        if(Linea[i] != ','){

        }
        printf("%c", Linea[i]);
    } 
    return;
}



//Funcion main donde trabajaremos todo
int main(){
    //Definiremos los arreglos en los cuales trabajaremos
    struct Arista Aristas[LONGITUD_MAXIMA_DE_ARISTAS];
    struct Vertice Vertices[LONGITUD_MAXIMA_DE_VERTICES];
    struct Grafica G;
    char* Linea;
    char AuxLinea[LONGITUD_MAXIMA_DE_LINEA];
    printf("Buscaremos El Archivo ......\n");
    FILE* fp = fopen(NOMBRE_ARCHIVO, "r"); //Abre el archivo en modo lectura
    if(fp == NULL){ //Si el archivo no existe
        printf("Error al abrir el archivo ......\n");
        return 0;
    }else{
            printf("El archivo se abrio correctamente ......\n");
            // la primera linea sera la de los vertices por lo tanto la leemos 
            //y metemos  a Vertices
            Linea = fgets(AuxLinea, LONGITUD_MAXIMA_DE_LINEA, fp);
            agregarVertices(Linea , Vertices);
        
        }
    fclose(fp);
    return 0;    
}





