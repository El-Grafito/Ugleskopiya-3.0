document.addEventListener('scroll', function() {
    var stripBottom = document.querySelector('.strip-bottom');
    var distanceFromTop = document.body.scrollHeight - window.innerHeight - window.scrollY;

    if (distanceFromTop <= 0) {
        stripBottom.style.bottom = '0';
    } else {
        stripBottom.style.bottom = '-30pt';
    }
});
