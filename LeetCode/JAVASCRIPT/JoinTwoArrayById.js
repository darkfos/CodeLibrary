/**
*  @param {Object} initialObject
*  @return {Object}
*/
const sortedObj = (initialObject) => {
    const sortedKeys = Object.keys(initialObject).sort()
    return sortedKeys.reduce((obj, key) => {
        obj[key] = initialObject[key];
        return obj
    }, {})
}
/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {

    const map = new Map();

    for (let el of arr1) {
        map.set(el.id, sortedObj(el))
    }

    for (let el of arr2) {
        if (map.has(el.id)) {
            let newObj = map.get(el.id)
            map.set(el.id, sortedObj(Object.assign(newObj, el)))
        } else {
            map.set(el.id, sortedObj(el))
        }
    }

    return Array.from(map.values()).sort((v1, v2) => v1.id <= v2.id ? -1 : 1);
};
