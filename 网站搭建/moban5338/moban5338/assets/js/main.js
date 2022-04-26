(function ($) {
    "use strict";
    
    /*----------------------------------------
	   Sticky Menu Activation
	---------------------------------*/
	$(window).on('scroll', function () {
		if ($(this).scrollTop() > 350) {
			$('.header-sticky').addClass('sticky');
		} else {
			$('.header-sticky').removeClass('sticky');
		}
	});
	/*----------------------------------------
		Off Canvas
	-------------------------------------------*/
	$(".off-canvas-btn").on('click', function () {
		$("body").addClass('fix');
		$(".off-canvas-wrapper").addClass('open');
	});

	$(".btn-close-off-canvas,.off-canvas-overlay").on('click', function () {
		$("body").removeClass('fix');
		$(".off-canvas-wrapper").removeClass('open');
	});

	/*----------------------------------------
		Off Canvas Menu
	-------------------------------------------*/
	$(".off-canvas-menu-btn").on('click', function () {
		$("body").addClass('fix');
		$(".off-canvas-menu-wrapper").addClass('open');
	});

	$(".btn-close-off-canvas,.off-canvas-overlay").on('click', function () {
		$("body").removeClass('fix');
		$(".off-canvas-menu-wrapper").removeClass('open');
	});

	/*----------------------------------------
		Off Canvas Search
	-------------------------------------------*/
	$(".off-canvas-search-btn").on('click', function () {
		$("body").addClass('fix');
		$(".off-canvas-search-wrapper").addClass('open');
	});

	$(".btn-close-off-canvas,.off-canvas-overlay").on('click', function () {
		$("body").removeClass('fix');
		$(".off-canvas-search-wrapper").removeClass('open');
	});
	/*----------------------------------------
		Responsive Mobile Menu
	------------------------------------------*/
	//Variables
	var $offCanvasNav = $('.mobile-menu'),
	$offCanvasNavSubMenu = $offCanvasNav.find('.dropdown');

	//Add Toggle Button With Off Canvas Sub Menu
	$offCanvasNavSubMenu.parent().prepend('<span class="menu-expand"><i></i></span>');

	//Close Off Canvas Sub Menu
	$offCanvasNavSubMenu.slideUp();

	//Category Sub Menu Toggle
	$offCanvasNav.on('click', 'li a, li .menu-expand', function(e) {
	var $this = $(this);
		if ( ($this.parent().attr('class').match(/\b(menu-item-has-children|has-children|has-sub-menu)\b/)) && ($this.attr('href') === '#' || $this.hasClass('menu-expand')) ) {
			e.preventDefault();
			if ($this.siblings('ul:visible').length){
				$this.parent('li').removeClass('active');
				$this.siblings('ul').slideUp();
			} else {
				$this.parent('li').addClass('active');
				$this.closest('li').siblings('li').removeClass('active').find('li').removeClass('active');
				$this.closest('li').siblings('li').find('ul:visible').slideUp();
				$this.siblings('ul').slideDown();
			}
		}
	});
	/*----------------------------------------
		Swiper Slider Activation Js
	------------------------------------------*/
	// Home 01 Slider
	var intro11Slider = new Swiper('.intro11-slider', {
        loop: true,
        speed: 400,
		slidesPerView: 1,
        spaceBetween: 10,
		effect: 'fade',
        navigation: {
            nextEl: '.home1-slider-next',
            prevEl: '.home1-slider-prev',
		},
		pagination: {
			el: '.swiper-pagination',
			type: 'bullets',
			clickable: 'true',
		},
		//autoplay: {},
	});
	// Single Slide 1
	var intro11Slider = new Swiper('.single-slide-1', {
        loop: true,
        speed: 400,
		slidesPerView: 1,
        spaceBetween: 10,
		effect: 'slide',
        autoHeight: true,
		pagination: {
			el: '.swiper-pagination',
			type: 'bullets',
			clickable: 'true',
		}
	});
	/*-----------------------------
		Video Background
	-----------------------------------*/
	$('.bg-video').vide('assets/video/bg-home', {
		playbackRate: .8,
		muted: true,
		loop: true,
		autoplay: true,
		position: '50% 50%', // Similar to the CSS `background-position` property.
		posterType: 'jpg', // Poster image type. "detect" — auto-detection; "none" — no poster; "jpg", "png", "gif",... - extensions.
		resizing: true, // Auto-resizing, read: https://github.com/VodkaBears/Vide#resizing
  		className: 'video-area' // Add custom CSS class to Vide div
	});
	/*----------------------------------------
		Splitting Activation Js
	------------------------------------------*/
	Splitting();

	var results = Splitting({
		target: '.text-slider, .video-title'
	  });
	/*---------------------------------
		Sticky Sidebar Activation
	-----------------------------------*/
	$('#sticky-sidebar').theiaStickySidebar({
		// Settings
		additionalMarginTop: 150
	});
	/*----------------------------------------
		Aos Activation Js
	------------------------------------------*/
	AOS.init({
		duration: 1200, // values from 0 to 3000, with step 50ms
		disable: false, // accepts following values: 'phone', 'tablet', 'mobile', boolean, expression or function
		offset: 30, // offset (in px) from the original trigger point
        once: true,
        easing: 'ease',
	  });
	/*---------------------------
		Counter To Up JS
	------------------------------*/
	// Counter
	$('.counter').counterUp({
		delay: 10,
		time: 1000
	});
	/*---------------------------
        Magnific Popup
    -----------------------------------*/
    $('.video-popup').magnificPopup({
        type: 'iframe'
	});
    /* ----------------------------
        Portfolio Masonry Activation
    -------------------------------*/
    $(window).on('load', function () {
            // filter items on button click
            $('.messonry-button').on('click', 'button', function () {
                var filterValue = $(this).attr('data-filter');
                $(this).siblings('.is-checked').removeClass('is-checked');
                $(this).addClass('is-checked');
                $grid.isotope({
                    filter: filterValue
                });
            });

            // init Isotope
            var $grid = $('.mesonry-list').isotope({
                percentPosition: true,
                transitionDuration: '0.7s',
                layoutMode: 'masonry',
                masonry: {
                    columnWidth: '.resizer',
                }
            });
	})
	/*---------------------------------
	 	MailChimp
    -----------------------------------*/
    $('#mc-form').ajaxChimp({
        language: 'en',
        callback: mailChimpResponse,
        // ADD YOUR MAILCHIMP URL BELOW HERE!
        url: 'http://devitems.us11.list-manage.com/subscribe/post?u=6bbb9b6f5827bd842d9640c82&amp;id=05d85f18ef'
    });
    function mailChimpResponse(resp) {
        if (resp.result === 'success') {
            $('.mailchimp-success').html('' + resp.msg).fadeIn(900);
            $('.mailchimp-error').fadeOut(400);
        } else if (resp.result === 'error') {
            $('.mailchimp-error').html('' + resp.msg).fadeIn(900);
        }
	}
	/*-------------------------
        Ajax Contact Form 
    ---------------------------*/
    $(function() {

        // Get the form.
        var form = $('#contact-form');

        // Get the messages div.
        var formMessages = $('.form-messege');

        // Set up an event listener for the contact form.
        $(form).submit(function(e) {
            // Stop the browser from submitting the form.
            e.preventDefault();

            // Serialize the form data.
            var formData = $(form).serialize();

            // Submit the form using AJAX.
            $.ajax({
                type: 'POST',
                url: $(form).attr('action'),
                data: formData
            })
            .done(function(response) {
                // Make sure that the formMessages div has the 'success' class.
                $(formMessages).removeClass('error');
                $(formMessages).addClass('success');

                // Set the message text.
                $(formMessages).text(response);

                // Clear the form.
                $('#contact-form input,#contact-form textarea').val('');
            })
            .fail(function(data) {
                // Make sure that the formMessages div has the 'error' class.
                $(formMessages).removeClass('success');
                $(formMessages).addClass('error');

                // Set the message text.
                if (data.responseText !== '') {
                    $(formMessages).text(data.responseText);
                } else {
                    $(formMessages).text('Oops! An error occured and your message could not be sent.');
                }
            });
        });

    });
	/*-----------------------------
		Scroll Up
	-----------------------------------*/
	function scrollToTop() {
		var $scrollUp = $('#scroll-top'),
			$lastScrollTop = 0,
			$window = $(window);

		$window.on('scroll', function () {
			var st = $(this).scrollTop();
			if (st > $lastScrollTop) {
				$scrollUp.removeClass('show');
			} else {
				if ($window.scrollTop() > 200) {
					$scrollUp.addClass('show');
				} else {
					$scrollUp.removeClass('show');
				}
			}
			$lastScrollTop = st;
		});

		$scrollUp.on('click', function (evt) {
			$('html, body').animate({scrollTop: 0}, 600);
			evt.preventDefault();
		});
	}
	scrollToTop();
	/*----------------------------------------*/
	/*-----  Preloader
	---------------------------------*/
	$(window).on('load', function () {
		$('#preloader').delay(250).fadeOut('slow')
		$('body').delay(250).css({'overflow':'visible'});
	});

})(jQuery);

