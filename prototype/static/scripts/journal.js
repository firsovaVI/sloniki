

var homework_example = {
    "headline": "Проверочная работа №1",
    "deadline": "2024-05-04",
    "problems": [
        {"problem_id": 1, "headline": "Подсчет количества информации"},
        {"problem_id": 2, "headline": "Алгебра логики"},
        {"problem_id": 3, "headline": "Системы счисления"},
        {"problem_id": 6, "headline": "Поиск путей в графе"}
    ]
};

var example_students_list = {
    "students_list": [
        {"first_name": "Иван", "last_name": "Смирнов", "solved_problems": [1, 2]},
        {"first_name": "Сергей", "last_name": "Васильев", "solved_problems": [1, 2, 3, 4]}
    ]
};
// id из URL-адреса
var homework_id = window.location.pathname.split('/')[3];

response = await fetch('http://127.0.0.1:8000/api/homework/' + homework_id);
homework = await response.json();
response = await fetch('http://127.0.0.1:8000/api/user/all/');
students_list = await response.json();


var table = document.getElementById("homeworkTable");
var headerRow = table.insertRow();
var headerCell = headerRow.insertCell();
headerCell.innerHTML = "Фамилии \\ ID задач";

// Добавление заголовков задач
//homework_example.problems.forEach(function(problem) {
    homework.problems.forEach(function(problem) {
var headerCell = headerRow.insertCell();
headerCell.innerHTML = problem.problem_id;
});

// Добавление заголовка для столбца процента
var percentHeaderCell = headerRow.insertCell();
percentHeaderCell.innerHTML = "Процент";

// Добавление данных учеников и их решений
//example_students_list.students_list.forEach(function(student) {
    students_list.students_list.forEach(function(student) {
var row = table.insertRow();
var nameCell = row.insertCell();
nameCell.innerHTML = student.last_name;

// Счетчик решенных задач
var solvedCount = 0;
//homework_example.problems.forEach(function(problem) {
    homework.problems.forEach(function(problem) {
    var solved = student.solved_problems.includes(problem.problem_id) ? '+' : '-';
    var cell = row.insertCell();
    cell.innerHTML = solved;
    if (solved === '+') {
        solvedCount++;
    }
});

// Расчет процента решенных задач
//var percent = (solvedCount / homework_example.problems.length * 100).toFixed(2);
var percent = (solvedCount / homework_example.problems.length * 100).toFixed(2);
var percentCell = row.insertCell();
percentCell.innerHTML = percent + "%";
});
