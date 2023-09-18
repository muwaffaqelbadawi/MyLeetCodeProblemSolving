// Time Complexity of generating all substring = O(n**3)

const subArray = (arr) => {
  const n = arr.length;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n - i; j++) {
      for (let k = i; k <= i + j; k++) {
        console.log(arr[k] + " ");
        console.log("\n");
        
      }
    }
  }
};

subArray([1, 2, 3, 4, 5, 6]);
