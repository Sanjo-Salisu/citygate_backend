;(function($) {
    "use strict";
    
    var navbar=$('.menu_inner_area,.main_menu_bg,.menu_inner_area_two');
    var nav_offset_top = $('.main_menu_area,.main_menu_area_three,.main_menu_area_four,.main_menu_area_five,.error_area,.coming_soon_area').offset().top + 200;
    /*-------------------------------------------------------------------------------
	  Navbar 
	-------------------------------------------------------------------------------*/

	navbar.affix({
	  offset: {
	    top: nav_offset_top,
	  }
	});


	navbar.on('affix.bs.affix', function() {
		if (!navbar.hasClass('affix')){
			navbar.addClass('animated slideInDown');
		}
	});
    
    navbar.on('affixed-top.bs.affix', function() {
	  	navbar.removeClass('animated slideInDown');
	});
    
    /*----------------------------------------------------*/
    /* Offcanvas Menu js
    /*----------------------------------------------------*/
    $('.bar_menu,#nav-icon1').on('click',function(){
        if( $(".right_sidebar_menu").hasClass('open') ){
            $(".right_sidebar_menu").removeClass('open')
        }
        else{
            $(".right_sidebar_menu").addClass('open')
        }
        return false
    });
    
    $(window).on("load",function(){
        $(".right_widget_inner").niceScroll({
            scrollspeed: 50,
            mousescrollstep: 30,
            cursorcolor: "transparent",
            cursorwidth: "0px",
            cursorminheight: 32,
            cursorborderradius: "0px", 
            smoothscroll: true,
        });
    });
    
    /*========serch popup js==========*/
    $(document).ready(function() {
        $('.popup-with-zoom-anim').magnificPopup({
            type: 'inline',

            fixedContentPos: false,
            fixedBgPos: true,

            overflowY: 'auto',

            closeBtnInside: true,
            preloader: false,

            midClick: true,
            removalDelay: 300,
            mainClass: 'my-mfp-zoom-in'
        });

        $('.popup-with-move-anim').magnificPopup({
            type: 'inline',

            fixedContentPos: false,
            fixedBgPos: true,

            overflowY: 'auto',

            closeBtnInside: true,
            preloader: false,

            midClick: true,
            removalDelay: 300,
            mainClass: 'my-mfp-slide-bottom'
        });
    });
    
    /*----------------------------------------------------*/
    /*  Main Slider js
    /*----------------------------------------------------*/
    function main_slider(){
        if ( $('#main_slider').length ){
            $("#main_slider").revolution({
                sliderType:"standard",
                sliderLayout:"auto",
                delay:4000,
                disableProgressBar:"on",
                navigation: {
                    onHoverStop: 'off',
                    touch:{
                        touchenabled:"on"
                    },
                    arrows: {
                        style:"zeus",
                        enable:true,
                        hide_onmobile:true,
                        hide_under:820,
                        hide_onleave:true,
                        hide_delay:200,
                        hide_delay_mobile:1200,
                        tmp:'<div class="tp-title-wrap">  	<div class="tp-arr-imgholder"></div> </div>',
                        left: {
                            h_align: "left",
                            v_align: "center",
                            h_offset: 5,
                            v_offset: 0
                        },
                        right: {
                            h_align: "right",
                            v_align: "center",
                            h_offset: 5,
                            v_offset: 0
                        }
                    },
                },
                responsiveLevels:[4096,1320,1199,992,767,480],
                gridwidth:[1170,1170,960,720,700,300],
                gridheight:[800,800,800,800,500,500],
                lazyType:"smart",
                fallbacks: {
                    simplifyAll:"off",
                    nextSlideOnWindowFocus:"off",
                    disableFocusListener:false,
                }
            })
        }
    }
    main_slider();
    
     /*----------------------------------------------------*/
    /*  Main Slider Two js
    /*----------------------------------------------------*/
    function main_slider_two(){
        if ( $('#main_slider_two').length ){
            $("#main_slider_two").revolution({
                sliderType:"standard",
                sliderLayout:"auto",
                delay:4000,
                dottedOverlay:"false",
                disableProgressBar:"on",
                navigation: {
                    onHoverStop: 'off',
                    touch:{
                        touchenabled:"on"
                    },
                    arrows: {
                        style:"zeus",
                        enable:true,
                        hide_onmobile:true,
                        hide_under:820,
                        hide_onleave:true,
                        hide_delay:200,
                        hide_delay_mobile:1200,
                        tmp:'<div class="tp-title-wrap">  	<div class="tp-arr-imgholder"></div> </div>',
                        left: {
                            h_align: "left",
                            v_align: "center",
                            h_offset: 5,
                            v_offset: 0
                        },
                        right: {
                            h_align: "right",
                            v_align: "center",
                            h_offset: 5,
                            v_offset: 0
                        }
                    },
                },
                responsiveLevels:[4096,1320,1199,992,767,480],
                gridwidth:[1170,1170,1000,750,700,320],
                gridheight:[715,715,715,715,600,500],
                lazyType:"none",
                parallax: {
                    type:"mouse",
                    origo:"slidercenter",
                    speed:2000,
                    levels:[2,3,4,5,6,7,12,16,10,50,46,47,48,49,50,55],
                    type:"mouse",
                    disable_onmobile:"on"
                },
                shadow:0,
                spinner:"off",
                stopLoop:"on",
                stopAfterLoops:0,
                stopAtSlide:1,
                shuffle:"off",
                autoHeight:"off",
                fullScreenAutoWidth:"off",
                fullScreenAlignForce:"off",
                fullScreenOffsetContainer: "",
                fullScreenOffset: "60px",
                disableProgressBar:"on",
                hideThumbsOnMobile:"off",
                hideSliderAtLimit:0,
                hideCaptionAtLimit:0,
                hideAllCaptionAtLilmit:0,
                debugMode:false,
                fallbacks: {
                    simplifyAll:"off",
                    nextSlideOnWindowFocus:"off",
                    disableFocusListener:false,
                }
            })
        }
    }
    main_slider_two();
    
    /*----------------------------------------------------*/
    /*  Main Slider js
    /*----------------------------------------------------*/
    function main_slider_four(){
        if ( $('#main_slider_four').length ){
            $("#main_slider_four").revolution({
                sliderType:"standard",
                sliderLayout:"auto",
                delay:5000,
                disableProgressBar:"on",
                navigation: {
                    onHoverStop: 'off',
                    touch:{
                        touchenabled:"on"
                    },
                    arrows: {
                        style:"zeus",
                        enable:true,
                        hide_onmobile:true,
                        hide_under:767,
                        hide_onleave:true,
                        hide_delay:200,
                        hide_delay_mobile:1200,
                        tmp:'<div class="tp-title-wrap">  	<div class="tp-arr-imgholder"></div> </div>',
                        left: {
                            h_align: "left",
                            v_align: "center",
                            h_offset: 5,
                            v_offset: 0
                        },
                        right: {
                            h_align: "right",
                            v_align: "center",
                            h_offset: 5,
                            v_offset: 0
                        }
                    },
                },
                responsiveLevels:[4096,1320,1199,992,767,480],
                gridwidth:[1170,1170,1000,750,550,300],
                gridheight:[678,678,678,678,678,500],
                lazyType:"smart",
                fallbacks: {
                    simplifyAll:"off",
                    nextSlideOnWindowFocus:"off",
                    disableFocusListener:false,
                }
            })
        }
    }
    main_slider_four();
    
    /*----------------------------------------------------*/
    /*  Main Slider js
    /*----------------------------------------------------*/
    function main_slider_five(){
        if ( $('#main_slider_five').length ){
            $("#main_slider_five").revolution({
                sliderType:"standard",
                sliderLayout:"auto",
                delay:5000,
                disableProgressBar:"on",
                navigation: {
                    onHoverStop: 'off',
                    touch:{
                        touchenabled:"on"
                    },
                    arrows: {
                        style:"zeus",
                        enable:true,
                        hide_onmobile:true,
                        hide_under:767,
                        hide_onleave:true,
                        hide_delay:200,
                        hide_delay_mobile:1200,
                        tmp:'<div class="tp-title-wrap">  	<div class="tp-arr-imgholder"></div> </div>',
                        left: {
                            h_align: "left",
                            v_align: "center",
                            h_offset: 5,
                            v_offset: 0
                        },
                        right: {
                            h_align: "right",
                            v_align: "center",
                            h_offset: 5,
                            v_offset: 0
                        }
                    },
                },
                responsiveLevels:[4096,1320,1199,992,767,480],
                gridwidth:[1170,1170,1000,750,550,300],
                gridheight:[625,625,625,625,625,500],
                lazyType:"smart",
                fallbacks: {
                    simplifyAll:"off",
                    nextSlideOnWindowFocus:"off",
                    disableFocusListener:false,
                }
            })
        }
    }
    main_slider_five();
    
    /*----------------------------------------------------*/
    /*  Gallery Slider
    /*----------------------------------------------------*/
    function practice_slider(){
        if ( $('.practice_slider').length ){
            $('.practice_slider').owlCarousel({
                loop:true,
                margin: 30,
                items: 4,
                nav:true,
                autoplay: true,
                smartSpeed: 1500,
                dots:true,
                navContainerClass: 'practice_arrow',
                navText: ['<img src="img/arrow.png" alt="">','<img src="img/arrow-left.png" alt="">'],
                responsiveClass: true,
                responsive: {
                    0: {
                        items: 1,
                    },
                    600: {
                        items: 2,
                    },
                    800: {
                        items: 3,
                    },
                    1060: {
                        items: 4,
                    }
                }
            })
        }
    }
    practice_slider();
    
    /*----------------------------------------------------*/
    /*  testimonial Slider
    /*----------------------------------------------------*/
    function testimonial_slider(){
        if ( $('#testimonial_slider').length ){
            $('#testimonial_slider').owlCarousel({
                loop:true,
                margin:230,
                items: 2,
                nav:false,
                autoplay: true,
                smartSpeed: 1500,
                dots:true,
                responsiveClass: true,
                responsive: {
                    0: {
                        items: 1,
                        margin:20
                    },
                    650: {
                        items: 2,
                        margin:100
                    },
                    800: {
                        items: 2,
                        margin:100
                    },
                    1199: {
                        items: 2,
                    }
                }
            })
        }
    }
    testimonial_slider();
    
    
    /*----------------------------------------------------*/
    /*  testimonial Slider Two
    /*----------------------------------------------------*/
    function testimonial_two(){
        if ( $('.testimonial_slider_two').length ){
            $('.testimonial_slider_two').owlCarousel({
                loop:true,
                margin:30,
                items: 3,
                nav:false,
                autoplay: true,
                smartSpeed: 1500,
                dots:true,
                responsiveClass: true,
                responsive: {
                    0: {
                        items: 1,
                    },
                    600: {
                        items: 2,
                    },
                    800: {
                        items: 2,
                    },
                    1060: {
                        items: 3,
                    }
                }
            })
        }
    }
    testimonial_two();
    
    /*----------------------------------------------------*/
    /*  Gallery Slider
    /*----------------------------------------------------*/
    function client_slider(){
        if ( $('.client_slider').length ){
            $('.client_slider').owlCarousel({
                loop:true,
                margin: 30,
                items: 6,
                nav:false,
                autoplay: true,
                smartSpeed: 1500,
                dots:true,
                responsiveClass: true,
                responsive: {
                    0: {
                        items: 1,
                    },
                    480: {
                        items: 2,
                    },
                    600: {
                        items: 4,
                    },
                    992: {
                        items: 6,
                    }
                }
            })
        }
    }
    client_slider();
    
    
    $('.counter').counterUp({
        delay: 10,
        time: 1000
    });
    
    
    /*----------------------------------------------------*/
    /*  Magnificpopup js 
    /*----------------------------------------------------*/
    $(document).ready(function() {
        $('.popup-youtube').magnificPopup({
            disableOn: 700,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,

            fixedContentPos: false
        });
    });
    
    /*----------------------------------------------------*/
    /*  Cases Isotop
    /*----------------------------------------------------*/
    function our_cases(){
        if ( $('.our_cases_area,.projects_area,.projects_full_area').length ){
            // Activate isotope in container
            $(".our_case_inner,.project_full_inner").imagesLoaded( function() {
                $(".our_case_inner,.project_full_inner").isotope({
                    layoutMode: 'fitRows',
                }); 
            }); 
            // Add isotope click function
            $(".project_fillter li").on('click',function(){
                $(".project_fillter li").removeClass("active");
                $(this).addClass("active");

                var selector = $(this).attr("data-filter");
                $(".our_case_inner,.project_full_inner").isotope({
                    filter: selector,
                    animationOptions: {
                        duration: 450,
                        easing: "linear",
                        queue: false,
                    }
                });
                return false;
            });
        }
    }
    our_cases();
    
    
    /*=============================================== 
      Skrollr Init
    ================================================*/
    var mySkrollr = skrollr.init({
        forceHeight: false,
        easings: {
            easeOutBack: function (p, s) {
                s = 1.70158;
                p = p - 1;
                return (p * p * ((s + 1) * p + s) + 1);
            }
        },
        mobileCheck: function() {
            //hack - forces mobile version to be off
            return false;
        }
    });
    
    /*----------------------------------------------------*/
    /*  Google map js
    /*----------------------------------------------------*/
    
    if ( $('#mapBox1').length ){
        var $lat = $('#mapBox1').data('lat');
        var $lon = $('#mapBox1').data('lon');
        var $zoom = $('#mapBox1').data('zoom');
        var $marker = $('#mapBox1').data('marker');
        var $info = $('#mapBox1').data('info');
        var $markerLat = $('#mapBox1').data('mlat');
        var $markerLon = $('#mapBox1').data('mlon');
        var map = new GMaps({
        el: '#mapBox1',
        lat: $lat,
        lng: $lon,
        scrollwheel: false,
        scaleControl: true,
        streetViewControl: false,
        panControl: true,
        disableDoubleClickZoom: true,
        mapTypeControl: false,
        zoom: $zoom,
            styles: [
                {
                    "featureType": "water",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#e2a062"
                        }
                    ]
                },
                {
                    "featureType": "transit",
                    "stylers": [
                        {
                            "color": "#e2a062"
                        },
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "road.highway",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "visibility": "on"
                        },
                        {
                            "color": "#e2a062"
                        }
                    ]
                },
                {
                    "featureType": "road.highway",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        }
                    ]
                },
                {
                    "featureType": "road.local",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "visibility": "on"
                        },
                        {
                            "color": "#ffffff"
                        },
                        {
                            "weight": 1.8
                        }
                    ]
                },
                {
                    "featureType": "road.local",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "color": "#b53c00"
                        }
                    ]
                },
                {
                    "featureType": "poi",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "visibility": "on"
                        },
                        {
                            "color": "#b53c00"
                        }
                    ]
                },
                {
                    "featureType": "administrative",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "color": "#e2a062"
                        }
                    ]
                },
                {
                    "featureType": "road.arterial",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        }
                    ]
                },
                {
                    "featureType": "road.arterial",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#ffffff"
                        }
                    ]
                },
                {
                    "featureType": "landscape",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "visibility": "on"
                        },
                        {
                            "color": "#e0d3c9"
                        }
                    ]
                },
                {
                    "featureType": "road",
                    "elementType": "labels.text.fill",
                    "stylers": [
                        {
                            "color": "#b53c00"
                        }
                    ]
                },
                {
                    "featureType": "administrative",
                    "elementType": "labels.text.fill",
                    "stylers": [
                        {
                            "visibility": "on"
                        },
                        {
                            "color": "#737373"
                        }
                    ]
                },
                {
                    "featureType": "poi",
                    "elementType": "labels.icon",
                    "stylers": [
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "poi",
                    "elementType": "labels",
                    "stylers": [
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "road.arterial",
                    "elementType": "geometry.stroke",
                    "stylers": [
                        {
                            "color": "#d6d6d6"
                        }
                    ]
                },
                {
                    "featureType": "road",
                    "elementType": "labels.icon",
                    "stylers": [
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {},
                {
                    "featureType": "poi",
                    "elementType": "geometry.fill",
                    "stylers": [
                        {
                            "color": "#e2a062"
                        }
                    ]
                }
            ]
        });

        map.addMarker({
            lat: $markerLat,
            lng: $markerLon,
            icon: $marker,    
            infoWindow: {
              content: $info
            }
        })
    }
    
    
    /*----------------------------------------------------*/
    /*  Google map Two js
    /*----------------------------------------------------*/
    
    if ( $('#mapBox').length ){
        var $lat = $('#mapBox').data('lat');
        var $lon = $('#mapBox').data('lon');
        var $zoom = $('#mapBox').data('zoom');
        var $marker = $('#mapBox').data('marker');
        var $info = $('#mapBox').data('info');
        var $markerLat = $('#mapBox').data('mlat');
        var $markerLon = $('#mapBox').data('mlon');
        var map = new GMaps({
            el: '#mapBox',
            lat: $lat,
            lng: $lon,
            scrollwheel: false,
            scaleControl: true,
            streetViewControl: false,
            panControl: true,
            disableDoubleClickZoom: true,
            mapTypeControl: false,
            zoom: $zoom,
                styles: [
                    {
                        "featureType": "administrative.country",
                        "elementType": "geometry",
                        "stylers": [
                            {
                                "visibility": "simplified"
                            },
                            {
                                "hue": "#ff0000"
                            }
                        ]
                    }
                ]
            });
        
            map.addMarker({
                lat: $markerLat,
                lng: $markerLon,
                icon: $marker,    
                infoWindow: {
                  content: $info
                }
            })
        }
    
    
    /*----------------------------------------------------*/
    /*  Google map js
    /*----------------------------------------------------*/
    
})(jQuery)
