const overlay = document.querySelector('.overlay-container');
const cross = document.querySelector('.overlay__cross');

window.addEventListener('load', () => {
	showOverlay();
});

const showOverlay = () => {
	const timeLimit = 1; // seconds
	let i = 0;
	const timer = setInterval(() => {
		i++;
		if (i == timeLimit) {
			clearInterval(timer);
			overlay.classList.remove('u-invisible');
		}
	}, 1000);
};

cross.addEventListener('click', () => {
	overlay.classList.add('u-invisible');
});
