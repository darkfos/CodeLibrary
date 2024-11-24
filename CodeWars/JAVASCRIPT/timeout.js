/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    // Easy

    let timeId = setTimeout(() => {
        fn(...args);
    }, t);

    return function cancelFn() {clearTimeout(timeId)};
};