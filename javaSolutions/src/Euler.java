import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.Stack;
import java.util.function.Function;

public class Euler {

	private static long problem10() {

		int n = 2000000;

		boolean isPrime[] = new boolean[n + 1];

		for (int i = 2; i <= n; ++i) {
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
		for (int i = 2; i <= n; ++i) {
			if (isPrime[i]) {
				sum += i;
			}
		}

		return sum;
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

	public long problem45() {
				
		Function<Integer, Long> tri = (val) -> {
			return (long) (val * (val + 1) / 2);
		};
		
		Function<Integer, Long> pent = (val) -> {
			return (long) (val * (3 * val - 1) / 2);
		};
		
		Function<Integer, Long> hex = (val) -> {
			return (long) (val * (2 * val - 1));
		};

		List<Long> tris = new ArrayList<>();
		Set<Long> pents = new HashSet<>();
		Set<Long> hexs = new HashSet<>();

		for (int i = 2; i < 1000000; ++i) {
			tris.add(tri.apply(i));
			pents.add(pent.apply(i));
			hexs.add(hex.apply(i));
		}
						
		List<Long> list = new ArrayList<>();
		
		for (Long i : tris) {
			if (pents.contains(i) && hexs.contains(i)) {
				list.add(i);
			}
		}
		
		System.out.println(list.size());
		
		Collections.sort(list);
		
		return list.get(0);
	}
	
	public Euler() {
		System.out.println(problem45());
	}

	public static void main(String[] args) {
		new Euler();
	}
}
