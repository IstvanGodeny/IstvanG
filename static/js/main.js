$(document).ready(function() {
    var lastScrollTop = 0;
    $(window).scroll(function() {
        var st = $(this).scrollTop();
        if (st > lastScrollTop){
            // Scroll down
            $('.navbar').css('top', '-60px');
            $('.navbar').css('background', 'var(--green-0)');
            $('.navbar').css('opacity', '1');
        } else if (st === 0){
            // Again on the top
            $('.navbar').css('top', '0');
            $('.navbar').css('background', 'var(--green-0)');
            $('.navbar').css('opacity', '1');
        } else {
            // Scroll up
            $('.navbar').css('top', '0');
            $('.navbar').css('background', 'var(--green-0)');
            $('.navbar').css('opacity', '0.75');
        }
        lastScrollTop = st;
    });
});

var animation = lottie.loadAnimation({
        container: document.getElementById('backgroundAnimation'),
        renderer: 'svg',
        loop: true,
        autoplay: true,
        path: 'static/assets/lotti/Animation.json' // Replace with your actual path
    });
    animation.setSpeed(0.20);
