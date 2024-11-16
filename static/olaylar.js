// HEADER

function navDesktopDahaFazlaMenusunuAcVeyaKapat() {
	var buton = document.querySelector(".header-nav.sadece-desktop .header-nav-daha-fazla-btn");
	var menu = document.querySelector(".header-nav.sadece-desktop .header-nav-daha-fazla-menu");
	buton.classList.toggle("aktif");
	menu.classList.toggle("gizle");
}

function navMobilDahaFazlaMenusunuAcVeyaKapat() {
	var buton = document.querySelector(".header-nav.sadece-mobil .header-nav-daha-fazla-btn");
	var menu = document.querySelector(".header-nav.sadece-mobil .header-nav-daha-fazla-menu");
	buton.classList.toggle("aktif");
	menu.classList.toggle("gizle");
}


// SLIDESHOW
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
	showSlides(slideIndex += n);
}

function currentSlide(n) {
	showSlides(slideIndex = n);
}

function showSlides(n) {
	var i;
	var slides = document.getElementsByClassName("mySlides");
	if (n > slides.length) { slideIndex = 1 }
	if (n < 1) { slideIndex = slides.length }
	for (i = 0; i < slides.length; i++) {
		slides[i].style.display = "none";
	}
	slides[slideIndex - 1].style.display = "block";
}



// SSS (AKORDİYON)

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("active");

    var panel = this.nextElementSibling;
    if (panel.style.maxHeight) {
			panel.style.maxHeight = null;
			panel.style.opacity = 0;
    } else {
			panel.style.maxHeight = panel.scrollHeight + "px";
			panel.style.opacity = 1;
    }
  });
}

