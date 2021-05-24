const password = document.getElementById("password")
const passwordConfirmation = document.getElementById("passwordConfirmation")

function confirmPassword(confirmPasswordInput) {
    if (passwordConfirmation.value === "") {
        confirmPasswordInput.setCustomValidity("Required confirm password")
    } else if (password.value !== passwordConfirmation.value) {
        confirmPasswordInput.setCustomValidity("Passwords do not match")
    } else {
        confirmPasswordInput.setCustomValidity("")
    }
}
