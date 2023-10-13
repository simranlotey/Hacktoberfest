// Write a program to convert units (e.g., length, weight, volume) between different systems.

function convertUnits(value, fromUnit, toUnit) {
  // 1. convert to base unit
  // 2. convert to target unit
  // 3. return result
  const baseUnit = convertToBaseUnit(value, fromUnit);
  return convertFromBaseUnit(baseUnit, toUnit);
}

function convertToBaseUnit(value, fromUnit) {
  switch (fromUnit) {
    case "in":
      return value * 2.54;
    case "ft":
      return value * 30.48;
    case "yd":
      return value * 91.44;
    case "mi":
      return value * 160934.4;
    case "oz":
      return value * 28.3495;
    case "lb":
      return value * 453.592;
    case "gal":
      return value * 3.78541;
    case "l":
      return value * 1000;
    default:
      return value;
  }
}

function convertFromBaseUnit(value, toUnit) {
    switch (toUnit) {
        case "in":
        return value / 2.54;
        case "ft":
        return value / 30.48;
        case "yd":
        return value / 91.44;
        case "mi":
        return value / 160934.4;
        case "oz":
        return value / 28.3495;
        case "lb":
        return value / 453.592;
        case "gal":
        return value / 3.78541;
        case "l":
        return value / 1000;
        default:
        return value;
    }
    }

console.log(convertUnits(1, "in", "ft"));
console.log(convertUnits(1, "ft", "yd"));
console.log(convertUnits(1, "yd", "mi"));