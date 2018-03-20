(function ($) {

    "use strict";

    var cfg = {
            scrollDuration: 800 // smoothscroll duration
        },

        $WIN = $(window);

    // Add the User Agent to the <html>
    // will be used for IE10 detection (Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0))
    var doc = document.documentElement;
    doc.setAttribute('data-useragent', navigator.userAgent);

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $(function () {
        $.ajaxSetup({
            headers: {"X-CSRFToken": getCookie("csrftoken")}
        });
    });

    /* Welcome
     * -------------------------------------------------- */
    var Welcome = function () {
        var welcomeSection = $('.welcome-section'),
            enterButton = welcomeSection.find($('.enter-button'));
        setTimeout(function () {
            welcomeSection.removeClass('content-hidden')
        }, 800);

        enterButton.on('click', function (e) {
            e.preventDefault();
            welcomeSection.addClass('content-hidden').fadeOut('slow');
        })


    };

    /* Preloader
     * -------------------------------------------------- */
    var clPreloader = function () {

        $("html").addClass('cl-preload');

        $WIN.on('load', function () {

            //force page scroll position to top at page refresh
            // $('html, body').animate({ scrollTop: 0 }, 'normal');

            // will first fade out the loading animation 
            $("#loader").fadeOut("slow", function () {
                // will fade out the whole DIV that covers the website.
                $("#preloader").delay(300).fadeOut("slow");
            });

            // for hero content animations 
            $("html").removeClass('cl-preload');
            $("html").addClass('cl-loaded');

        });
    };


    /* Menu on Scrolldown
     * ------------------------------------------------------ */
    var clMenuOnScrolldown = function () {

        var menuTrigger = $('.header-menu-toggle');

        $WIN.on('scroll', function () {

            if ($WIN.scrollTop() > 150) {
                menuTrigger.addClass('opaque');
            }
            else {
                menuTrigger.removeClass('opaque');
            }

        });
    };


    /* OffCanvas Menu
     * ------------------------------------------------------ */
    var clOffCanvas = function () {

        var menuTrigger = $('.header-menu-toggle'),
            nav = $('.header-nav'),
            closeButton = nav.find('.header-nav__close'),
            siteBody = $('body'),
            mainContents = $('section, footer');

        // open-close menu by clicking on the menu icon
        menuTrigger.on('click', function (e) {
            e.preventDefault();
            // menuTrigger.toggleClass('is-clicked');
            siteBody.toggleClass('menu-is-open');
        });

        // close menu by clicking the close button
        closeButton.on('click', function (e) {
            e.preventDefault();
            menuTrigger.trigger('click');
        });

        // close menu clicking outside the menu itself
        siteBody.on('click', function (e) {
            if (!$(e.target).is('.header-nav, .header-nav__content, .header-menu-toggle, .header-menu-toggle span')) {
                // menuTrigger.removeClass('is-clicked');
                siteBody.removeClass('menu-is-open');
            }
        });

    };

    /* slick slider
     * ------------------------------------------------------ */
    var clSlickSlider = function () {

        $('.clients').slick({
            arrows: false,
            dots: true,
            infinite: true,
            slidesToShow: 6,
            slidesToScroll: 2,
            //autoplay: true,
            pauseOnFocus: false,
            autoplaySpeed: 1000,
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 5
                    }
                },
                {
                    breakpoint: 1000,
                    settings: {
                        slidesToShow: 4
                    }
                },
                {
                    breakpoint: 800,
                    settings: {
                        slidesToShow: 3,
                        slidesToScroll: 2
                    }
                },
                {
                    breakpoint: 500,
                    settings: {
                        slidesToShow: 2,
                        slidesToScroll: 2
                    }
                }

            ]
        });

        $('.testimonials').slick({
            arrows: true,
            dots: false,
            infinite: true,
            slidesToShow: 1,
            slidesToScroll: 1,
            adaptiveHeight: true,
            pauseOnFocus: false,
            autoplaySpeed: 1500,
            responsive: [
                {
                    breakpoint: 900,
                    settings: {
                        slidesToShow: 1,
                        slidesToScroll: 1
                    }
                },
                {
                    breakpoint: 800,
                    settings: {
                        arrows: false,
                        dots: true
                    }
                }
            ]
        });

    };

    /* Smooth Scrolling
     * ------------------------------------------------------ */
    var clSmoothScroll = function () {

        $('.smoothscroll').on('click', function (e) {
            var target = this.hash,
                $target = $(target);

            e.preventDefault();
            e.stopPropagation();

            $('html, body').stop().animate({
                'scrollTop': $target.offset().top
            }, cfg.scrollDuration, 'swing').promise().done(function () {

                // check if menu is open
                if ($('body').hasClass('menu-is-open')) {
                    $('.header-menu-toggle').trigger('click');
                }

                window.location.hash = target;
            });
        });

    };


    /* Placeholder Plugin Settings
     * ------------------------------------------------------ */
    var clPlaceholder = function () {
        $('input, textarea, select').placeholder();
    };


    /* Alert Boxes
     * ------------------------------------------------------ */
    var clAlertBoxes = function () {

        $('.alert-box').on('click', '.alert-box__close', function () {
            $(this).parent().fadeOut(500);
        });

    };


    /* Animate On Scroll
     * ------------------------------------------------------ */
    var clAOS = function () {

        AOS.init({
            offset: 200,
            duration: 600,
            easing: 'ease-in-sine',
            delay: 300,
            once: true,
            disable: 'mobile'
        });

    };


    /* Back to Top
     * ------------------------------------------------------ */
    var clBackToTop = function () {

        var pxShow = 500,         // height on which the button will show
            fadeInTime = 400,         // how slow/fast you want the button to show
            fadeOutTime = 400,         // how slow/fast you want the button to hide
            scrollSpeed = 300,         // how slow/fast you want the button to scroll to top. can be a value, 'slow', 'normal' or 'fast'
            goTopButton = $(".go-top");

        // Show or hide the sticky footer button
        $(window).on('scroll', function () {
            if ($(window).scrollTop() >= pxShow) {
                goTopButton.fadeIn(fadeInTime);
            } else {
                goTopButton.fadeOut(fadeOutTime);
            }
        });
    };

    var CastingForm = function () {
        $('#contactForm').submit(function (e) {
            var sLoader = $('.cast-form.submit-loader');
            sLoader.slideDown("slow");

            var form = $(this).closest("form");

            var images = $('#contact_image');

            var input = document.querySelector('input[type=file]'),
                file = input.files[0];
            var formData = new FormData(document.querySelector("#contactForm"));

            formData.append('photos', file);

            $.ajax({
                url: form.attr("data-url"),
                type: "POST",
                processData: false,
                contentType: false,
                mimeType: 'multipart/form-data',
                data: formData,
                beforeSend: function () {
                    sLoader.slideDown("slow");
                },
                success: function () {
                    sLoader.slideUp("slow");
                    $('.cast-form.message-warning').fadeOut();
                    $('#contactForm').fadeOut();
                    $('.cast-form.message-success').fadeIn();
                },
                error: function () {
                    sLoader.slideUp("slow");
                    $('.cast-form.message-warning').html("Something went wrong. Please try again.");
                    $('.cast-form.message-warning').slideDown("slow");

                }
            });

            e.preventDefault();
        });
    };


    var SubscribeForm = function () {
        $('#mailForm').submit(function (e) {

            var sLoader = $('.sub-mail.submit-loader');
            sLoader.slideDown("slow");

            var form = $(this).closest("form");
            $.post(form.attr("data-url"), $(this).serialize())
                .done(function () {
                    sLoader.slideUp("slow");
                    $('.sub-mail.message-warning').fadeOut();
                    $('#mailForm').fadeOut();
                    $('.sub-mail.message-success').fadeIn();
                })
                .fail(function () {
                    sLoader.slideUp("slow");
                    $('.sub-mail.message-warning').html("Something went wrong. Please try again.");
                    $('.sub-mail.message-warning').slideDown("slow");
                });
            e.preventDefault();
        });
    };

    function PersoneInfoClose() {
        $('.casting-person-info-overlay').on("click", function (e) {
            $('.casting-person-info-overlay').fadeOut("slow");
            $('.casting-person-info').fadeOut("slow");
            $('.casting-content').fadeIn("slow");
            $('#personImages').html("");
        });

        $('#person-close').on("click", function (e) {
            $('.casting-person-info-overlay').fadeOut("slow");
            $('.casting-person-info').fadeOut("slow");
            $('.casting-content').fadeIn("slow");
            $('#personImages').html("");
        });
    }

    function GetAllInfo() {
        $('.cast-table *[data-link]').on("click", function () {
            var link = $(this).data('link');
            var person_id = $(this).data('id');

            $.get(link, {person_id: person_id})
                .done(function (data) {

                    $('.person-id').html(data.id);
                    $('.person-first_name').html(data.first_name);
                    $('.person-second_name').html(data.second_name);
                    $('.person-email').html(data.email);
                    $('.person-phone').html(data.phone);
                    $('.person-age').html(data.age);
                    $('.person-city').html(data.city);
                    $('.person-gender').html(data.gender);
                    $('.person-prof').html(data.prof);
                    $('.person-experience').html(data.experience);
                    $('.person-crowd_scene').html(data.crowd_scene);
                    $('.person-grouping').html(data.grouping);
                    $('.person-about_info').html(data.about_info);
                    $('.person-video_url').html(data.video_url);
                    console.log(data.video);
                    if (data.video !== '') {
                        var video_id = data.video_url.split("v=")[1].split("?")[0];
                        $('.person-video-iframe').attr("src", 'https://www.youtube.com/embed/' + video_id + '?autoplay=0&amp;rel=0&amp;enablejsapi=1&amp;widgetid=1');
                    }

                    if (data.contact_image !== '') {
                        var img_arr = data.contact_image.split("\n");
                        $.each(img_arr, function (index, img_url) {
                            if (img_url !== '') {
                                var img = $('<img class="swiper-slide">');
                                img.attr("src", '/media/' + img_url);
                                img.attr("class", ' person-contact_image');
                                img.appendTo('#personImages');
                            }

                        });
                    }


                    $('.like-vote').data('link').replace('1', data.id);
                    $('.like-vote').data('id', data.id);
                    $('.like-count').text(data.like_count);
                    $('.casting-person-info-overlay').fadeIn("slow");
                    $('.casting-person-info').fadeIn("slow");
                    $('.casting-content').fadeOut("slow");
                });


            $("td > a").on("click", function (e) {
                e.stopPropagation();
            });
        });
    }

    function youtubeNext() {
        $('li.youtube-child').on("click", function (e) {
            var youtube_id = $(this).data('youtube-id');
            $('iframe.main-youtube').attr("src", 'https://www.youtube.com/embed/' + youtube_id + '?autoplay=1&amp;rel=0&amp;enablejsapi=1&amp;widgetid=1');
            $('iframe.main-youtube').attr("data-youtube-id", youtube_id);
            e.stopPropagation();
        })
    }

    function facebookShare() {
        $('#facebook_share').on("click", function (e) {
            var youtube_id = $('iframe.main-youtube').attr("data-youtube-id");
            $(this).attr("href", 'https://www.facebook.com/sharer/sharer.php?u=https://www.youtube.com/watch?v=' + youtube_id)
        })
    }

    function twitterShare() {
        $('#twitter_share').on("click", function (e) {
            var youtube_id = $('iframe.main-youtube').attr("data-youtube-id");
            $(this).attr("href", 'https://twitter.com/home?status=https://www.youtube.com/watch?v=' + youtube_id)
        })
    }

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

    function like() {
        var like = $(this);
        var type = like.data('type');
        var pk = like.data('id');
        var action = like.data('action');
        var dislike = like.next();
        var link = like.data('link').replace('1', pk);

        $.ajax({
            url: link,
            type: 'POST',
            data: {
                'obj': pk
            },

            success: function (json) {
                like.find("[data-count='like']").text(json.like_count);
            }
        });

        return false;
    }

    $(function () {
        $('[data-action="like"]').click(like);
    });


    /* Initialize
     * ------------------------------------------------------ */
    (function ssInit() {
        Welcome();
        clPreloader();
        clMenuOnScrolldown();
        clOffCanvas();
        clSlickSlider();
        clSmoothScroll();
        clPlaceholder();
        clAlertBoxes();
        clAOS();
        clBackToTop();
        CastingForm();
        GetAllInfo();
        PersoneInfoClose();
        navigationSection();
        youtubeNext();
        facebookShare();
        twitterShare();
        SubscribeForm();

    })();


})(jQuery);