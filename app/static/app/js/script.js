import { headerData } from "../constants/index.js";

// DOM variables
const navLinks = document.querySelector(".header .nav-links");
const mobileNavLinks = document.querySelector("nav .nav-links");
const hamburger = document.querySelector(".hamburger");

// populating the header with content
let output = "";
headerData?.forEach((data) => {
  output += `<li><a href=${data.link}>${data.text}</a></li>`;
});
navLinks.innerHTML = output;
mobileNavLinks.innerHTML = output;

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  mobileNavLinks.classList.toggle("active");
});

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

/* Sample Work Images Swiper */
let swiperWorkSample = new Swiper(".sample-container", {
  loop: true,
  grabCursor: true,
  spaceBetween: 10,

  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    dynamicBullets: true,
  },

  breakpoints: {
    1000: {
      slidesPerView: 3,
    },
    650: {
      slidesPerView: 2,
    },
  },
});

// footer get full year
document.querySelector("span.year").innerHTML = new Date().getFullYear();

// Cart
// plus-cart - when quantity is to be incremented by 1
$(".plus-cart-btn").click(function () {
  let id = $(this).attr("pid").toString();
  let selectedElement = this.parentNode.children[2];
  $.ajax({
    type: "GET",
    url: "/plus_cart",
    data: { prod_id: id },
    success: function (data) {
      // console.log("data =", data);
      selectedElement.innerText = data.quantity;
      document.getElementById("amount").innerText = data.amount;
      document.getElementById("totalamount").innerText = data.totalamount;
    },
  });
});

// minus-cart - when quantity is to be decremented by 1
$(".minus-cart-btn").click(function () {
  let id = $(this).attr("pid").toString();
  let selectedElement = this.parentNode.children[2];
  $.ajax({
    type: "GET",
    url: "/minus_cart",
    data: { prod_id: id },
    success: function (data) {
      // console.log("data =", data);
      selectedElement.innerText = data.quantity;
      document.getElementById("amount").innerText = data.amount;
      document.getElementById("totalamount").innerText = data.totalamount;
    },
  });
});

// remove-cart - when quantity is to be decremented by 1
$(".remove-btn").click(function () {
  let id = $(this).attr("pid").toString();
  let selectedElement = this;
  // console.log(selectedElement.parentNode.parentNode.parentNode.parentNode);
  $.ajax({
    type: "GET",
    url: "/remove_cart",
    data: { prod_id: id },
    success: function (data) {
      document.getElementById("amount").innerText = data.amount;
      document.getElementById("totalamount").innerText = data.totalamount;
      selectedElement.parentNode.parentNode.parentNode.parentNode.remove(); // remove the 4th parent that nests the clicked item
    },
  });
});
