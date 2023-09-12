#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Definiremos unas contantes para el programa
#define NOMBRE_ARCHIVO "ENTRADA1.txt"
#define LONGITUD_MAXIMA_DE_LINEA 10000

//Definiremos la estructura de las aristas y Vertices de las graficas
struct Arista{
    int V1;
    int V2;
};

struct Vertice{
    int V;
    int Grado;
    struct Arista* Aristas;
};

struct Grafo{
    /* data */
    struct Vertice* Vertices;
    struct Arista* Aristas;
};



//Funcion main donde trabajaremos todo

int main(){
    //Definiremos los arreglos en los cuales trabajaremos
    struct Arista* Aristas;
    struct Vertice* Vertices;
    struct Grafo* Grafo;
    char character;
    printf("Buscaremos El Archivo ......\n");
    FILE* fp = fopen(NOMBRE_ARCHIVO, "r"); //Abre el archivo en modo lectura
    if(fp == NULL){ //Si el archivo no existe
        printf("Error al abrir el archivo ......\n");
        return 0;
    }else{
        printf("El archivo se abrio correctamente ......\n");
        while (character = fgetc(fp) != EOF){
            switch (character)
            {
            case ',':
                //No haremos nada con este Caracter ya que solo nos servira para separar los numeros
                break;
            
            default:
                break;
            }
        }
    }


}