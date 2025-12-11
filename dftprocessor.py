#include <stdio.h>
#include <math.h>

#define PI 3.14159

typedef struct
{
  float real;
  float imag;
} COMPLEX;

void dft(float *x, COMPLEX *X, int N)
{
  int k, n;

  for (k = 0; k < N; k++)
  {
    X[k].real = 0;
    X[k].imag = 0;

    for (n = 0; n < N; n++)
    {
      X[k].real += x[n] * cos(2 * PI * k * n / N);
      X[k].imag -= x[n] * sin(2 * PI * k * n / N);
    }

    printf("\n%.2f %.2fj", X[k].real, X[k].imag);
  }
}

void main()
{
  float x[] = {1, 2, 3, 4};

  int N = sizeof(x) / sizeof(float);

  COMPLEX X[100];

  dft(x, X, N);
}