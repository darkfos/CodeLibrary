/**
 * @param {string} allowed
 * @param {string[]} words
 * @return {number}
 */
var countConsistentStrings = function(allowed, words) {
    // Easy

    let cnt = 0;

    words.map((el) => {

        let allowed_ch = 0;

        for (let ch = 0; ch < el.length; ch++) {
            if (allowed.includes(el[ch])) {
                allowed_ch++;
            }
        }

        if (allowed_ch === el.length) {
            cnt++;
        }
    });
    return cnt
};