/**
 * @param {string[][]} paths
 * @return {string}
 */
var destCity = function(paths) {
    /*
        EASY

        You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct
        path going from cityAi to cityBi. Return the destination city, that is, the city without any path
        outgoing to another city.
        It is guaranteed that the graph of paths forms a line without any loop, therefore, there
        will be exactly one destination city.
    */

    if (paths.length === 1) {
        return paths[0][1]
    }

    let cityLast = paths[0][1];
    let cityResult = cityLast;

    paths.map((element, indx) => {
        for (let m = 0; m < paths.length; m++) {
            if (paths[m][0] === cityLast) {
                cityResult = paths[m][1];
                cityLast = paths[m][1];
            }
        }
    })

    return cityResult
};