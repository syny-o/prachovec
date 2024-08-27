// Navbar Scroll Effect

function scrollEffect() {
  const navbar = document.querySelector(".navbar");
  const navbarImg = document.querySelector(".navbar-brand");

  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      navbar.classList.add("navbar-scroll");
      navbarImg.classList.add("logo-small");
    } else {
      navbar.classList.remove("navbar-scroll");
      navbarImg.classList.remove("logo-small");
    }
  });
}

// Go to Top Button
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

// Spinner
function hideSpinner() {
  const spinnerWrapper = document.getElementById("spinner-wrapper");
  spinnerWrapper.classList.add("spinner-hidden");
  // spinnerWrapper.style.display = "none";
  setTimeout(() => {
    spinnerWrapper.remove();
  }, 500);
}

// after whole DOM is loaded, add particular event listeners
document.addEventListener("DOMContentLoaded", () => {
  scrollEffect();
  goToTop();
});

// hide spinner after everything is loaded including all images
window.onload = hideSpinner;
