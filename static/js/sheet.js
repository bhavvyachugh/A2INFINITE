/* ------------------------ elements ----------------------- */

const viewBwBtn = document.getElementById('viewBwBtn');
const viewColoredBtn = document.getElementById('viewColoredBtn');

const bwSheet = document.querySelector('.img-container__img--black');
const coloredSheet = document.querySelector('.img-container__img--colored');

const printBwBtn = document.getElementById('printBwBtn');
const printColoredBtn = document.getElementById('printColoredBtn');

/* -------------------------------- functions ------------------------------- */

const viewBwSheet = () => {
	bwSheet.style.display = 'block';
	coloredSheet.style.display = 'none';
};

const viewColoredSheet = () => {
	coloredSheet.style.display = 'block';
	bwSheet.style.display = 'none';
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

document.addEventListener('contextmenu', (event) => event.preventDefault());
viewBwBtn.addEventListener('click', viewBwSheet);
viewColoredBtn.addEventListener('click', viewColoredSheet);
printBwBtn.addEventListener('click', printBwSheet);
printColoredBtn.addEventListener('click', printColoredSheet);
