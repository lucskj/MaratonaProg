#include <stdio.h>
     
int saida_tamanho = 0;

int entrada[] = {289384, 930887, 692778, 636916, 747794, 238336, 885387, 760493, 516650, 641422};
int tamanho_entrada = 10;
int saida[11] = {0};

int primos[1000000] = {2, 3, 5, 7, 11, 13, 17, 19};
int primos_pos = 8;

int inicio = 23;
int fim;

int boolean = 1;
int x = 0;

int main(void) {
  for(int i = 0; i < tamanho_entrada; i++){
    if(entrada[i]>fim){
      fim = entrada[i];
    }
  }

  while(inicio < fim){
    boolean = 1;
    x = 0;
    
    while(primos[x]*primos[x] <= inicio){
      
      if(inicio%primos[x] == 0){
        boolean = 0;
        break;
      }

      x += 1;
    }
    
    if(boolean){
      primos[primos_pos] = inicio;
      primos_pos += 1;
    }

    inicio += 1;
  }
  
  for(int i = 0; i < tamanho_entrada; i++){
    int fatores[100] = {1};
    int fatores_tamanho = 0;
    int n_atual = entrada[i];
    for(int x = 0; x < primos_pos-1; x++){
      int fator = 0;
      while(n_atual%primos[x] == 0){
        fator = 1;
        if(primos[x] == n_atual){
          break;
        }
        else{
          n_atual = n_atual/primos[x];
        }
      }
      if(fator){
        fatores[fatores_tamanho+1] = primos[x];
        fatores_tamanho += 1;
      }
    }
    int aux = fatores_tamanho;
    saida[saida_tamanho] = aux;
    saida_tamanho += 1;
  }

  int cont = 0;
  while(cont < tamanho_entrada){
    printf("\n%d -> %d", entrada[cont], saida[cont]);
    cont += 1;
  }
  return 0;
}
