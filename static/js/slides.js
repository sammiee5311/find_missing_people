
setTimeout(() => {
    $('#message').fadeOut('slow');
}, 3000);

let slideIndex = 1;

const showDivs = (n, id) => {
    let i;
    let x = document.getElementsByClassName(`mySlides_${id}`);
    if (n > x.length) {slideIndex = 1}
    if (n < 1) {slideIndex = x.length} ;
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    console.log(slideIndex-1);
    x[slideIndex-1].style.display = "block";
}

const plusDivs = (n, id) => {
    showDivs(slideIndex += n, id);
}

// showDivs(slideIndex, 0);
