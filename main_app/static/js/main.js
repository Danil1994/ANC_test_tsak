$(document).on('click', '.subordinates-link', function() {
    // Получаем идентификатор сотрудника из атрибута data-employee-id
    var employeeId = $(this).data('employee-id');

    // Отправляем AJAX-запрос на сервер для получения подчиненных сотрудников
    $.ajax({
        url: '/main_app/get_subordinates/' + employeeId + '/',
        method: 'GET',
        success: function(response) {
            // Обновляем интерфейс, добавляя подчиненных к выбранному сотруднику
            $(this).parent().append(response);  // Вставляем ответ после выбранного сотрудника
        }.bind(this),
        error: function(xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText); // сообщение об ошибке в консоль
        }
    });
});


function toggleOrder(field) {
    var currentOrder = getParameterByName('order_by');
    var newOrder = currentOrder === field ? '-' + field : field;
    window.location.href = updateQueryStringParameter('order_by', newOrder);
}

function getParameterByName(name) {
    var urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

function updateQueryStringParameter(key, value) {
    var urlParams = new URLSearchParams(window.location.search);
    urlParams.set(key, value);
    return window.location.pathname + '?' + urlParams.toString();
}

