function knapsackProblem() {
    const maxWeight = 5;
    const items = [
      { name: "a", weight: 1, value: 6 },
      { name: "b", weight: 2, value: 10 },
      { name: "c", weight: 3, value: 12 }
    ];
  
    const knapsack = (currentWeight, currentItem, currentItems) => {
      if (currentItem >= items.length) {
        return;
      }
  
      if (currentWeight + items[currentItem].weight <= maxWeight) {
        currentItems.push(items[currentItem]);
        knapsack(currentWeight + items[currentItem].weight, currentItem + 1, currentItems);
        currentItems.pop();
      }
  
      knapsack(currentWeight, currentItem + 1, currentItems);
  
      if (currentWeight > currentMaxWeight) {
        currentMaxWeight = currentWeight;
        maxWeightItems = currentItems.slice();
      }
    };
  
    let currentMaxWeight = 0;
    let maxWeightItems = [];
    knapsack(0, 0, []);
  
    console.log(currentMaxWeight);
    console.log(maxWeightItems);
  }
  
  knapsackProblem();