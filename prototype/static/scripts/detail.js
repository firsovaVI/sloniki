document.addEventListener("DOMContentLoaded", function() {
    // Получаем данные из элемента <script id="problem">
    var problemData = JSON.parse(document.getElementById("problem").textContent);
    var taskWindow = document.querySelector('.task-window');

    // Выводим заголовок задачи и изображение
    var headlineElement = document.createElement("h1");
    headlineElement.textContent = problemData.headline;
    taskWindow.appendChild(headlineElement);
    
   // Если в JSON-данных есть поле image_url и оно не равно null, создаем элемент <img>
    if (problemData.hasOwnProperty('image_url') && problemData.image_url !== null) {
        var imageElement = document.createElement("img");
        imageElement.src = problemData.image_url;

        // Добавляем элемент <img> в DOM
        taskWindow.appendChild(imageElement);
    }
    
    // Выводим условие задачи
    var statementElement = document.createElement("p");
    statementElement.textContent = problemData.statement;
    taskWindow.appendChild(statementElement);
    
    // Находим поле ввода и кнопку на странице
var userInput = document.getElementById("userInput");
var submitButton = document.getElementById("submitButton");

// Добавляем обработчик события для кнопки
submitButton.addEventListener("click", function() {
    // Получаем значение из поля ввода
    var userValue = userInput.value.trim();
    
    // Здесь вы можете использовать значение userValue для выполнения каких-либо действий, например, сравнения с правильным ответом

    // Пример: сравнение с правильным ответом из JSON-данных
    var correctAnswer = problemData.answer;
    if (userValue === correctAnswer) {
        alert("Правильный ответ!");
    } else {
        alert("Неправильный ответ. Попробуйте еще раз.");
    }
});

});
