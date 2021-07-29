// const date = new Date();
// document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(() => {
    $('#message').fadeOut('slow');
}, 3000);

let slideIndex = 1;
showDivs(slideIndex);

const plusDivs = (n) => {
    console.log(n);
    showDivs(slideIndex += n);
}

const showDivs = (n) => {
    let i;
    let x = document.getElementsByClassName("mySlides");
    if (n > x.length) {slideIndex = 1}
    if (n < 1) {slideIndex = x.length} ;
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    x[slideIndex-1].style.display = "block";
}
