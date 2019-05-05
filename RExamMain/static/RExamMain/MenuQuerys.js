$(window).bind('hashchange', function () {
    if (location.hash === '') {
        location.hash = '/main';
        return true
    }
    let link = location.hash.replace('#', '');
    $('#content').text('Загрузка!');
    $.get(link, function (data) {
        $('#content').html($(data).filter('#body')).fadeIn('slow');
        document.title = $(data).filter('title').text();
    });

});
$(document).ready(function () {
    if (location.hash !== '') {
        let link = location.hash.replace('#', '');
        $.get(link, function (data) {
            $('#content').html($(data).filter('#body')).fadeIn('slow');
            document.title = $(data).filter('title').text();
        });
    } else {
        location.hash = '/main';
    }
    $('a').on('click', function () {
        if ($(this).attr('noajax') === 'true') return true;
        location.hash = $(this).attr('href');
        return false;
    });
});