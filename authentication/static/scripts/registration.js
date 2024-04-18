// Функция для валидации пароля
function validatePassword() {
    var passwordInput = document.getElementById('password'); // Получаем элемент поля ввода пароля
    var password = passwordInput.value; // Получаем значение введенного пароля

    // Проверяем длину пароля и его содержимое
    if (password.length < 8) {
        alert('Пароль должен содержать минимум 8 символов');
        return false; // Прерываем отправку формы
    }

    // Проверяем, что пароль состоит только из букв и цифр
    var alphanumericRegex = /^[a-zA-Z0-9]+$/; // Регулярное выражение: только буквы и цифры
    if (!alphanumericRegex.test(password)) {
        alert('Пароль должен состоять только из букв и цифр');
        return false; // Прерываем отправку формы
    }

    return true; // Пароль прошел валидацию
}
