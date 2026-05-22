function checkPassword() {

    let password = document.getElementById("password").value;

    let hasUpper = false;
    let hasLower = false;
    let hasNumber = false;
    let hasSymbol = false;

    let symbols = "!@#$%^&*()_-+={}[]:;'<>,.?/~`";

    for (let char of password) {
        if (char >= 'A' && char <= 'Z') {
            hasUpper = true;
        } else if (char >= 'a' && char <= 'z') {
            hasLower = true;
        } else if (char >= '0' && char <= '9') {
            hasNumber = true;
        } else if (symbols.includes(char)) {
            hasSymbol = true;
        }
    }

    let score = 0;

    if (hasUpper) score++;
    if (hasLower) score++;
    if (hasNumber) score++;
    if (hasSymbol) score++;
    if (password.length >= 8) score++;

    let result = "";

    if (score <= 2) {
        result = "Weak Password ❌";
    } else if (score === 3 || score === 4) {
        result = "Medium Password ⚠️";
    } else {
        result = "Strong Password ✅";
    }

    document.getElementById("result").innerText = result;
}
