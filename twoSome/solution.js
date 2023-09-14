/* 
   Test Cases
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. 
*/

var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
};

var twoSumVersion2 = function (nums, target) {
  let map = {};
  for (let i = 0; i < nums.length; i++) {
    let value = nums[i];
    let complementPair = target - value;
    if (map[complementPair] !== undefined) {
      return [map[complementPair], i];
    } else {
      map[value] = i;
    }
  }
};

let twoSumVersion3 = (nums, target) => {
  let map = {};
  for (let i = 0; i < nums.length; i++) {
    let value = nums[i];
    let x = target - value;
    if (map[x] !== undefined) {
      return [map[x], i];
    } else {
      map[value] = i;
    }
  }
};

let twoSumVersion4 = (nums, target) => {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
};

let twoSumVersion5 = (nums, target) => {
  for (let i = 0; i < nums.length; i++) {
    const map = {};
    let value = nums[i];
    let rem = target - value;
    if (map[rem] !== undefined) {
      // object map has a key of rem
      return [map[rem], i];
    } else {
      map[value] = i;
    }
  }
};

const twoSumVersion6 = (nums, target) => {
  let map = {};
  for (let i = 0; i < nums.length; i++) {
    let value = nums[i];
    let complement = target - value;
    // this assures you find the the first two added sum give the solution
    if (map[complement] !== undefined) {
      return [map[complement], i];
    } else {
      map[value] = i;
    }
  }
};

const newObj = {};
newObj[7888] = "";
console.log(newObj[7888]);

const nums = [2, 7, 11, 15];
const target = 9;
const testCase5 = twoSumVersion4(nums, target);
console.log(testCase5);

const testCase2 = twoSumVersion2(nums, target);

console.log(testCase2);
