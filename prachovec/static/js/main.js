// Navbar Scroll Effect

function scrollEffect() {
  const navbar = document.querySelector(".navbar");

  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      navbar.classList.add("navbar-scroll");
    } else {
      navbar.classList.remove("navbar-scroll");
    }
  });
}

function goToTop() {
  const goTop = document.querySelector(".go-top");

  window.addEventListener("scroll", () => {
    if (window.scrollY > 100) {
      goTop.classList.add("go-top-visible");
    } else {
      goTop.classList.remove("go-top-visible");
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  scrollEffect();
  goToTop();
});
