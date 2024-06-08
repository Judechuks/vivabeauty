import { headerData } from "../constants/index.js";

// DOM variables
const navLinks = document.querySelector(".nav-links");
const hamburger = document.querySelector(".hamburger");

// populating the header with content
let output = "";
headerData?.forEach((data) => {
  output += `<li><a href=${data.link}>${data.text}</a></li>`;
});
navLinks.innerHTML = output;

hamburger.addEventListener("click", () => hamburger.classList.toggle("active"));

/* Review Swiper */
let swiperReview = new Swiper(".review-container", {
  loop: true,
  grabCursor: true,
  spaceBetween: 48,

  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    dynamicBullets: true,
  },

  breakpoints: {
    800: {
      slidesPerView: 2,
    },
  },
});

// footer get full year
document.querySelector("span.year").innerHTML = new Date().getFullYear();
