// заглушка
var testData = {
    "headline": "Проверочная работа №1",
    "deadline": "2024-05-04",
    "problems": [
        {
            "problem_id": 1,
            "headline": "Подсчет количества информации",
            "url": "/1/"
        },
        {
            "problem_id": 2,
            "headline": "Алгебра логики",
            "url": "/2/"
        },
        {
            "problem_id": 3,
            "headline": "Системы счисления",
            "url": "/3/"
        },
        {
            "problem_id": 6,
            "headline": "Поиск путей в графе",
            "url": "/6/"
        }
    ]
};

// Функция для отображения данных
function displayHomeworkData(data) {
    // заголовок
    document.getElementById('headline').textContent = data.headline;

    // дедлайн
    document.getElementById('deadline').textContent = `Крайний срок: ${data.deadline}`;

    // задачи
    var problemsList = document.getElementById('problems-list');
    data.problems.forEach(problem => {
        var listItem = document.createElement('li');
        var button = document.createElement('button');
        button.textContent = problem.headline;
        button.onclick = function() {
            window.location.href = problem.url;
        };
        listItem.appendChild(button);
        problemsList.appendChild(listItem);
    });
}


displayHomeworkData(testData);

// закомменти строку выше и раскомменти код ниже
/*
// id из URL-адреса
var homework_id = window.location.pathname.split('/')[3];

// запрос на endpoint
fetch("http://127.0.0.1:8000/api/homework/" + homework_id)
  .then(response => response.json())
  .then(data => displayHomeworkData(data))
  .catch(error => console.error('Error fetching homework data:', error));
*/