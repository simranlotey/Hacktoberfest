public class knapsackProblem {
    public static int[] knapsackProblem(int[][] items, int capacity) {
        int[][] knapsackValues = new int[items.length + 1][capacity + 1];
        for (int i = 1; i < items.length + 1; i++) {
            int currentValue = items[i - 1][0];
            int currentWeight = items[i - 1][1];
            for (int c = 0; c < capacity + 1; c++) {
                if (currentWeight > c) {
                    knapsackValues[i][c] = knapsackValues[i - 1][c];
                } else {
                    knapsackValues[i][c] = Math.max(
                            knapsackValues[i - 1][c],
                            knapsackValues[i - 1][c - currentWeight] + currentValue
                    );
                }
            }
        }
        return new int[] {knapsackValues[items.length][capacity], getKnapsackItems(knapsackValues, items)};
    }

    public static int[] getKnapsackItems(int[][] knapsackValues, int[][] items) {
        List<Integer> sequence = new ArrayList<>();
        int i = knapsackValues.length - 1;
        int c = knapsackValues[0].length - 1;
        while (i > 0) {
            if (knapsackValues[i][c] == knapsackValues[i - 1][c]) {
                i -= 1;
            } else {
                sequence.add(i - 1);
                c -= items[i - 1][1];
                i -= 1;
            }
            if (c == 0) break;
        }
        int[] result = new int[sequence.size()];
        for (int j = 0; j < sequence.size(); j++) {
            result[j] = sequence.get(j);
        }
        return result;
    }
}