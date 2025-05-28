function isValidBirthYear(byr) {
    const year = parseInt(byr);
    return byr.length === 4 && year >= 1920 && year <= 2002;
}

function isValidIssueYear(iyr) {
    const year = parseInt(iyr);
    return iyr.length === 4 && year >= 2010 && year <= 2020;
}

function isValidExpirationYear(eyr) {
    const year = parseInt(eyr);
    return eyr.length === 4 && year >= 2020 && year <= 2030;
}

function isValidHeight(hgt) {
    const match = hgt.match(/^(\d+)(cm|in)$/);
    if (!match) return false;

    const [, numStr, unit] = match;
    const num = parseInt(numStr);

    if (unit === 'cm') return num >= 150 && num <= 193;
    else if (unit === 'in') return num >= 59 && num <= 76;

    return false;
}

function isValidHairColor(hcl) {
    return /^#[0-9a-f]{6}$/.test(hcl);
}

function isValidEyeColor(ecl) {
    const validColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'];
    return validColors.includes(ecl);
}

function isValidPassportId(pid) {
    return /^\d{9}$/.test(pid);
}

function isValidPassport(passport) {
    const requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'];
    return requiredFields.every(field => passport.hasOwnProperty(field));
}

function isValidPassportWithData(passport) {
    if (!isValidPassport(passport)) return false;

    return isValidBirthYear(passport.byr) &&
           isValidIssueYear(passport.iyr) &&
           isValidExpirationYear(passport.eyr) &&
           isValidHeight(passport.hgt) &&
           isValidHairColor(passport.hcl) &&
           isValidEyeColor(passport.ecl) &&
           isValidPassportId(passport.pid);
}

function parsePassports(input) {
    const passportBlocks = input.trim().split('\n\n');
    return passportBlocks.map(block => {
        const passport = {};
        const pairs = block.split(/\s+/);

        pairs.forEach(pair => {
            const [key, value] = pair.split(':');
            if (key && value) {
                passport[key] = value;
            }
        });

        return passport;
    });
}

function validatePassports(input, part2 = false) {
    const passports = parsePassports(input);
    let validCount = 0;

    passports.forEach((passport) => {
        const isValid = part2 ? isValidPassportWithData(passport) : isValidPassport(passport);
        if (isValid) validCount++;
    });

    return validCount;
}

const answer1 = validatePassports(inputData, false);
const answer2 = validatePassports(inputData, true);

