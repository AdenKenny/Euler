import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
import java.util.Stack;
import java.util.function.Function;

public class Euler {
	
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
	
	public int problem26() {
		return 0;
	}
	
	public int problem40() {
		
		StringBuilder build = new StringBuilder();
		build.append(0);

		for (int i = 1; i < 1000000; ++i) {
			build.append(i + "");
		}
		
		String sum = build.toString();
		
		int total = 1;
		
		for (int i = 10; i < (1000000); i *= 10) {
			int tmp = Integer.parseInt(sum.charAt(i) + "");
						
			total *= tmp;
		}
		
		return total;
	}
	
	public int problem44() {
		
		Function<Integer, Integer> pent = (val) -> {
			return val * (3 * val - 1) / 2; 
		};

		Set<Integer> pents = new HashSet<>();
				
		for (int i = 1; i < 10000; ++i) {
			pents.add(pent.apply(i));
		}
				
		Stack<Integer> stack = new Stack<>();
		
		for (int i : pents) {
			for (int j : pents) {
				int sum = i + j;
				int difference = j - i;
								
				if (pents.contains(sum) && pents.contains(difference)) {
					stack.push(Math.abs(i - j));
				}				
			}
		}
		
		Collections.sort(stack);
		
		return stack.pop();
	}

	public Euler() {
		System.out.println(question10());
	}
		
	public static void main(String[] args) {
		new Euler();
	}
}
