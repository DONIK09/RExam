$(window).bind('hashchange', function () {
    if (location.hash === '') {
        location.hash = '/news';
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
        location.hash = '/news';
    }
    $('a').on('click', function () {
        if ($(this).attr('noajax') === 'true') return true;
        location.hash = $(this).attr('href');
        return false;
    });
});