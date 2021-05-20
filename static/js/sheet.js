/* ------------------------ elements ----------------------- */

const viewBwBtn = document.getElementById('viewBwBtn');
const viewColoredBtn = document.getElementById('viewColoredBtn');

const bwSheet = document.querySelector('.img-container__img--black');
const coloredSheet = document.querySelector('.img-container__img--colored');

const printBwBtn = document.getElementById('printBwBtn');
const printColoredBtn = document.getElementById('printColoredBtn');

/* -------------------------------- functions ------------------------------- */

const viewBwSheet = () => {
	$('.flip-container').addClass('flipped');
	$('#colored_1').removeClass('printMe');
	$('#black_and_white_1').addClass('printMe');
};

const viewColoredSheet = () => {
	$('.flip-container').removeClass('flipped');
	$('#colored_1').addClass('printMe');
	$('#black_and_white_1').removeClass('printMe');
};

const printBwSheet = () => {
	viewBwSheet();
	window.print();
};

const printColoredSheet = () => {
	viewColoredSheet();
	window.print();
};

/* --------------------------------- events --------------------------------- */

// viewBwBtn.addEventListener('click', viewBwSheet);
// viewColoredBtn.addEventListener('click', viewColoredSheet);
printBwBtn.addEventListener('click', printBwSheet);
printColoredBtn.addEventListener('click', printColoredSheet);
