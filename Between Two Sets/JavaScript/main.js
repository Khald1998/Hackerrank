'use strict';

const fs = require('fs');

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
 * Complete the 'getTotalX' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY a
 *  2. INTEGER_ARRAY b
 */

function getTotalX(a, b) {
    // Function to calculate the Greatest Common Divisor (GCD) of two numbers
    function calculateGCD(firstNumber, secondNumber) {
        // Continue the loop until secondNumber is 0
        while (secondNumber !== 0) {
            let temp = secondNumber;
            secondNumber = firstNumber % secondNumber;
            firstNumber = temp;
        }
        return firstNumber;
    }
    
    // Function to calculate the Least Common Multiple (LCM) of two numbers
    function calculateLCM(firstNumber, secondNumber) {
        return (firstNumber * secondNumber) / calculateGCD(firstNumber, secondNumber);
    }
    
    // Calculate the LCM for all elements in array 'a'
    // This will be the smallest number that is a multiple of all elements in 'a'
    const totalLCM = a.reduce((accumulatedLCM, currentValue) => {
        return calculateLCM(accumulatedLCM, currentValue);
    }, 1);
    
    // Calculate the GCD for all elements in array 'b'
    // This will be the largest number that is a divisor of all elements in 'b'
    const totalGCD = b.reduce((accumulatedGCD, currentValue) => {
        return calculateGCD(accumulatedGCD, currentValue);
    });
    
    // Initialize the count of numbers that satisfy both conditions
    let countOfNumbers = 0;
    
    // Check for multiples of the LCM that are also divisors of the GCD
    for (let multiple = totalLCM; multiple <= totalGCD; multiple += totalLCM) {
        if (totalGCD % multiple === 0) {
            // If the condition is met, increment the count
            countOfNumbers++;
        }
    }
    
    // Return the total count of such numbers
    return countOfNumbers;
}


function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

    const n = parseInt(firstMultipleInput[0], 10);

    const m = parseInt(firstMultipleInput[1], 10);

    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));

    const brr = readLine().replace(/\s+$/g, '').split(' ').map(brrTemp => parseInt(brrTemp, 10));

    const total = getTotalX(arr, brr);

    ws.write(total + '\n');

    ws.end();
}
