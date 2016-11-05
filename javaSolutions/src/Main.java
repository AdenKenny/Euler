public class Main {

	public Main() {
		System.out.println(question10());
	}
	
	private static long question10() {
		
		int n = 2000000;
		
		boolean isPrime[] = new boolean[n + 1];
		
		for(int i = 2; i <= n; ++i) {
			isPrime[i] = true;
		}
		
		for (int factor = 2; factor * factor <= n; ++factor) {
			if (isPrime[factor]) {
				for (int j = factor; factor * j <= n; ++j) {
					isPrime[factor * j] = false;
				}
			}
		}
		
		long sum = 0;
		for(int i = 2; i <= n; ++i) {
			if (isPrime[i]) {
				sum += i;
			}
		}
		
		return sum;
	}
	
	private static int question12() {
		
		
		return 0;
	}
	
	public static void main(String[] args) {
		new Main();
	}
	
}
