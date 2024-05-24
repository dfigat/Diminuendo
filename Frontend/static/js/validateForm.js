const toggleCssClasses = (obj, classToRemove, classToAdd) => {
    obj.classList.remove(classToRemove);
    obj.classList.add(classToAdd);
}

const validateErrorIncomingFromServer = (fieldName, errorInfo) => {
    errorBlock = document.querySelector(`.${fieldName}`);
    if (errorBlock) {
        capitalizedErrorInfo = errorInfo.charAt(0).toUpperCase() + errorInfo.slice(1);
        errorBlock.innerHTML = capitalizedErrorInfo;

        toggleCssClasses(errorBlock, 'hidden', 'shown');
    }
}

const getCSRFToken = () => {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

const validateField = (field) => {

    const isEmailCorrect = (email) => {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            return false;
        }
        return true;
    }

    const value = field.value.trim();
    const fieldName = field.name;
    const errorBlock = document.querySelector(`form .${fieldName}`);

    errorBlock.innerHTML = '';
    toggleCssClasses(errorBlock, 'shown', 'hidden');

    if (fieldName == 'email') {
        if (!isEmailCorrect(value)) {
            errorBlock.innerHTML = 'E-mail is of incorrect format';
            toggleCssClasses(errorBlock, 'hidden', 'shown');
        }
    } else if (fieldName == 'password') {
        if (value.length < 8) {
            errorBlock.innerHTML = 'Password must be at least 8 characters long';
            toggleCssClasses(errorBlock, 'hidden', 'shown');
        }
    } else if (fieldName == 'password_verify') {
        const passwordField = field.previousElementSibling
            .previousElementSibling
            .previousElementSibling; // to get to the previous input as we have two elements on our way between
        if (value != passwordField.value) {
            errorBlock.innerHTML = 'Passwords must be identical';
            toggleCssClasses(errorBlock, 'hidden', 'shown');
        }
    }
    if (value.length == 0 && field.required) {
        errorBlock.innerHTML = 'This field cannot be left blank';
        toggleCssClasses(errorBlock, 'hidden', 'shown');

    } else if (value.length < 3 && fieldName != 'password' && fieldName != 'password_verify') {
        errorBlock.innerHTML = 'This field must contain at least 3 characters';
        toggleCssClasses(errorBlock, 'hidden', 'shown');
    }
}