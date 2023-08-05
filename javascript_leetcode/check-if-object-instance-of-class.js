//link https://leetcode.com/problems/check-if-object-instance-of-class

/**
 * @param {any} obj
 * @param {any} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function (obj, classFunction) {
  while (obj != null) {
    if (obj.constructor === classFunction) {
      return true;
    }
    obj = obj.__proto__;
  }
  return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
