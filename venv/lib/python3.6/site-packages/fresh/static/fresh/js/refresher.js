function checkRefresh() {
    var req = new XMLHttpRequest();

    req.open('GET', '/fresh/', false);
    req.send();

    var fresh = JSON.parse(req.responseText).fresh;
    if (fresh) location.reload();

    doPoll();
}

function doPoll() {
    setTimeout(function() {
        checkRefresh();
    }, 1000);
}

doPoll();

