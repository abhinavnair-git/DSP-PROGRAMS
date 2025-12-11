#include <stdio.h>

int main() {
    int x[] = {1, 2, 3, 4};    // Input signal
    int h[] = {4, 3, 2};       // Impulse response
    int n = 4;                 // Length of x
    int m = 3;                 // Length of h
    int y[10];                 // Output array
    int i, j;

    // Initialize output array to zero
    for(i = 0; i < n + m - 1; i++)
        y[i] = 0;

    // Perform linear convolution
    for(i = 0; i < n; i++) 
    {
        for(j = 0; j < m; j++) 
        {
            y[i + j] += x[i] * h[j];
        }
    }

    // Display result
    printf("Linear Convolution Result:\n");
    for(i = 0; i < n + m - 1; i++)
        printf("%d ", y[i]);

    printf("\n");

    return 0;
}
