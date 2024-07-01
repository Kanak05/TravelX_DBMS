var TrandingSlider = new Swiper('.tranding-slider', {
    effect: 'coverflow',
    grabCursor: true,
    centeredSlides: true,
    loop: true,
    slidesPerView: 'auto',
    coverflowEffect: {
      rotate: 0,
      stretch: 0,
      depth: 100,
      modifier: 2.5,
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    }
  });

  var swiper = new Swiper(".slide-content", {
    slidesPerView: 4,
    spaceBetween: 25,
    loop: true,
    centerSlide: 'true',
    fade: 'true',
    grabCursor: 'true',
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },

    breakpoints:{
        0: {
            slidesPerView: 1,
        },
        480: {
            slidesPerView: 2,
        },
        950: {
            slidesPerView: 3,
        },
        1050: {
            slidesPerView: 4,
        },
        1550: {
            slidesPerView: 5,
        },
    },
  });




//  <script>
//   $(document).ready(function(){
//     $("#myCarousel").owlCarousel({
//       items: 3, // Number of cards shown in each slide
//       loop: true, // Continuously loop the carousel
//       margin: 20, // Space between cards
//       nav: true, // Show navigation buttons
//       navText: ["<i class='fas fa-chevron-left'></i>", "<i class='fas fa-chevron-right'></i>"], // Custom navigation icons
//       responsive: {
//         0: {
//           items: 1 // Number of cards shown in the carousel for smaller screens
//         },
//         768: {
//           items: 2 // Number of cards shown in the carousel for medium screens
//         },
//         992: {
//           items: 3 // Number of cards shown in the carousel for large screens
//         }
//       }
//     });
//   });
// </script> 
