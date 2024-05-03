async function loadData() {
    // URL-адрес endpoint'а: "http://127.0.0.1:8000/api/user/"
    response = await fetch('http://127.0.0.1:8000/api/user/');
    // В ответе содержится объект JSON (личная информация о пользователе)
    userData = await response.json();

//    const userData = {
//        username: "SlonTest1",
//        firstName: "Светлана",
//        lastName: "Романова",
//        group: "ST" // Измени на "TH", чтобы увидеть разные типы групп
//    };

    // URL-адрес endpoint'а: "http://127.0.0.1:8000/api/homework/all/"
    response = await fetch('http://127.0.0.1:8000/api/homework/all/');
    // В ответе содержится объект JSON (список проверочных работ)
    homeworksData = await response.json();

    // const homeworksData = [
    //     {
    //         headline: "Проверочная работа №1",
    //         deadline: "2024-05-04",
    //         url: "/account/homework-1/gradebook/"
    //     },
    //     {
    //         headline: "Домашнее задание по информатике",
    //         deadline: "2024-05-31",
    //         url: "/account/homework-2/gradebook/"
    //     }
    // ];

    // Добавляем данные о пользователе в HTML
    document.getElementById('user-info').innerHTML = `
        <p> ${userData.username}</p>
        <p> ${userData.firstName} ${userData.lastName}</p>
        <p> ${userData.group === 'TH' ? 'Учитель' : 'Студент'}</p>
    `;

    // Добавляем кнопки для домашних заданий
    homeworksData.forEach(homework => {
        const button = document.createElement('button');
        button.className = 'homework-button';
        button.innerHTML = `
            <div class="headline">${homework.headline}</div>
            <div class="deadline">${homework.deadline}</div>
        `;
        button.addEventListener('click', () => {
            window.location.href = homework.url;
        });
        document.getElementById('homework-buttons').appendChild(button);
    });
}

loadData();
