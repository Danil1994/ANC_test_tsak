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
