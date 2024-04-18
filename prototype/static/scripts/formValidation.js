document.addEventListener('DOMContentLoaded', function() {
    // Получаем ссылки на поле ввода и кнопку
    const userInput = document.getElementById('userInput');
    const submitButton = document.getElementById('submitButton');

    // Функция для проверки содержимого поля ввода и активации/деактивации кнопки
    function validateInput() {
        if (userInput.value.trim() !== '') {
            submitButton.disabled = false; // Разрешаем нажатие кнопки
            submitButton.style.pointerEvents = 'auto'; // Включаем обработку событий
        } else {
            submitButton.disabled = true; // Запрещаем нажатие кнопки
            submitButton.style.pointerEvents = 'none'; // Отключаем обработку событий
        }
    }

    // Добавляем обработчик события при вводе в поле
    userInput.addEventListener('input', validateInput);

    // Вызываем функцию проверки при загрузке страницы
    validateInput();
});
