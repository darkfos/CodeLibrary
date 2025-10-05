/**
 * @param {Function} fn
 * @return {Function}
 * Medium Level
 * https://leetcode.com/problems/memoize/
 */
function memoize(fn) {
    const cashMap = new Map()

    return function(...args) {
        const key = args.join(',')
        if (cashMap.has(key)) {
            return cashMap.get(key)
        }
        
        const resultFunc = fn(...args)
        cashMap.set(key, resultFunc)
        return resultFunc
    }
}
