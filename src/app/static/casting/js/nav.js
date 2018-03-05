(function ($) {

    // Page Nav
    var clickMenu = function () {

        $('a:not([class="external"])').click(function (event) {
            var section = $(this).data('nav-section'),
                navbar = $('#navbar');
            $('html, body').animate({
                scrollTop: $('[data-section="' + section + '"]').offset().top
            }, 500);

            if (navbar.is(':visible')) {
                navbar.removeClass('in');
                navbar.attr('aria-expanded', 'false');
                $('.js-cast-nav-toggle').removeClass('active');
            }

            event.preventDefault();
            return false;
        });

    };

    // Window Scroll
    var windowScroll = function () {
        var lastScrollTop = 0;

        $(window).scroll(function (event) {

            var header = $('#cast-header'),
                scrlTop = $(this).scrollTop();

            if (scrlTop > 500 && scrlTop <= 2000) {
                header.addClass('navbar-fixed-top cast-animated slideInDown');
            } else if (scrlTop <= 500) {
                if (header.hasClass('navbar-fixed-top')) {
                    header.addClass('navbar-fixed-top cast-animated slideOutUp');
                    setTimeout(function () {
                        header.removeClass('navbar-fixed-top cast-animated slideInDown slideOutUp');
                    }, 100);
                }
            }

        });
    };

    // Reflect scrolling in navigation
    var navActive = function (section) {

        var $el = $('#navbar > ul');
        $el.find('li').removeClass('active');
        $el.each(function () {
            $(this).find('a[data-nav-section="' + section + '"]').closest('li').addClass('active');
        });

    };
    var navigationSection = function () {

        var $section = $('div[data-section]');

        $section.waypoint(function (direction) {
            if (direction === 'down') {
                navActive($(this.element).data('section'));

            }
        }, {
            offset: '150px'
        });

        $section.waypoint(function (direction) {
            if (direction === 'up') {
                navActive($(this.element).data('section'));
            }
        }, {
            offset: function () {
                return -$(this.element).height() + 155;
            }
        });

    };

    // Animations


    var contentWayPoint = function () {
        var i = 0;
        $('.animate-box').waypoint(function (direction) {

            if (direction === 'down' && !$(this.element).hasClass('animated')) {

                i++;

                $(this.element).addClass('item-animate');
                setTimeout(function () {

                    $('body .animate-box.item-animate').each(function (k) {
                        var el = $(this);
                        setTimeout(function () {
                            var effect = el.data('animate-effect');
                            if (effect === 'fadeIn') {
                                el.addClass('fadeIn animated');
                            } else if (effect === 'fadeInLeft') {
                                el.addClass('fadeInLeft animated');
                            } else if (effect === 'fadeInRight') {
                                el.addClass('fadeInRight animated');
                            } else {
                                el.addClass('fadeInUp animated');
                            }

                            el.removeClass('item-animate');
                        }, k * 200, 'easeInOutExpo');
                    });

                }, 100);

            }

        }, {offset: '85%'});
    };
    var mobileMenuOutsideClick = function () {

        $(document).click(function (e) {
            var container = $("#cast-offcanvas, .js-cast-nav-toggle");
            if (!container.is(e.target) && container.has(e.target).length === 0) {

                if ($('body').hasClass('offcanvas')) {

                    $('body').removeClass('offcanvas');
                    $('.js-cast-nav-toggle').removeClass('active');

                }


            }
        });

    };

    var offcanvasMenu = function () {

        $('.s-header').prepend('<div id="cast-offcanvas" />');
        $('.s-header').prepend('<a href="#" class="js-cast-nav-toggle cast-nav-toggle cast-nav-white"><i></i></a>');
        var clone1 = $('.menu-1 > ul').clone();
        $('#cast-offcanvas').append(clone1);
        var clone2 = $('.menu-2 > ul').clone();
        $('#cast-offcanvas').append(clone2);

        $('#cast-offcanvas .has-dropdown').addClass('offcanvas-has-dropdown');
        $('#cast-offcanvas')
            .find('li')
            .removeClass('has-dropdown');

        // Hover dropdown menu on mobile
        $('.offcanvas-has-dropdown').mouseenter(function () {
            var $this = $(this);

            $this
                .addClass('active')
                .find('ul')
                .slideDown(500, 'easeOutExpo');
        }).mouseleave(function () {

            var $this = $(this);
            $this
                .removeClass('active')
                .find('ul')
                .slideUp(500, 'easeOutExpo');
        });


        $(window).resize(function () {

            if ($('body').hasClass('offcanvas')) {

                $('body').removeClass('offcanvas');
                $('.js-cast-nav-toggle').removeClass('active');

            }
        });
    };


    var burgerMenu = function () {

        $('body').on('click', '.js-cast-nav-toggle', function (event) {
            var $this = $(this);


            if ($('body').hasClass('overflow offcanvas')) {
                $('body').removeClass('overflow offcanvas');
            } else {
                $('body').addClass('overflow offcanvas');
            }
            $this.toggleClass('active');
            event.preventDefault();

        });
    };

    var goToTop = function () {

        $('.js-gotop').on('click', function (event) {

            event.preventDefault();

            $('html, body').animate({
                scrollTop: $('html').offset().top
            }, 500, 'easeInOutExpo');

            return false;
        });

        $(window).scroll(function () {

            var $win = $(window);
            if ($win.scrollTop() > 200) {
                $('.js-top').addClass('active');
            } else {
                $('.js-top').removeClass('active');
            }

            if ($win.scrollTop() > 100) {
                $('.cast-nav').addClass('scrolled');
            } else {
                $('.cast-nav').removeClass('scrolled');
            }

        });

    };
    /* Initialize
     * ------------------------------------------------------ */
    (function ssInit() {
        burgerMenu();
        mobileMenuOutsideClick();
        goToTop();
        offcanvasMenu();
        windowScroll();
        clickMenu();
        contentWayPoint();
        navigationSection();

    })();



})(jQuery);