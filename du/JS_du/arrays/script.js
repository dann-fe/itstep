// 11)
let breadPrices = [14, 25, 15, 9, 13, 11, 10];
// 12)
// for (let i = 1; i<=breadPrices.length; i++) {
//     console.log(`the price of bread for day ${i} is ${breadPrices[i]}`);
// }

// 13)
// for (let i = 0; i<=breadPrices.length; i++) {
//     console.log(`new price for day ${i + 1} including tax is ${Math.floor(breadPrices[i] * 1.15)}`)
// }

// 14)
for (let i = 0; i<=breadPrices.length; i++) {
    if (breadPrices[i] <= 10) {
        console.log(`the day when the bread price is lower than 10 is day ${breadPrices[i]}`)
    }
}