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

  

document.addEventListener("DOMContentLoaded", () => {
  scrollEffect();
  goToTop();
  hideSpinner();
});
