#include <stdio.h>

int main(void) {
	int t, i, m, n, count;
	scanf("%d", &t);
	for (i=0; i<t; ++i) {
		count = 0;
		m = 5;
		scanf("%d",&n);
		while (m<=n) {
			count += n/m;
			m*=5;
		}
		printf("%d\n",count);
	}

	return 0;
}
