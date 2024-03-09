'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'plusMinus' function below.
 *
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function plusMinus(arr) {
    let positiveCount = 0;
    let negativeCount = 0;
    let zeroCount = 0;
    const totalElements = arr.length;

    for (let num of arr) {
        if (num > 0) {
            positiveCount += 1;
        } else if (num < 0) {
            negativeCount += 1;
        } else {
            zeroCount += 1;
        }
    }

    const positiveRatio = (positiveCount / totalElements).toFixed(6);
    const negativeRatio = (negativeCount / totalElements).toFixed(6);
    const zeroRatio = (zeroCount / totalElements).toFixed(6);

    console.log(positiveRatio);
    console.log(negativeRatio);
    console.log(zeroRatio);


}

function main() {
    const n = parseInt(readLine().trim(), 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    plusMinus(arr);
}
