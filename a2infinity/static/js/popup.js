const signupPopup = document.querySelector('.signup-form-container');

window.addEventListener('load', function () {
	showPopup();
});

function showPopup() {
	const timeLimit = 7; // Seconds
	let i = 0;
	const timer = setInterval(() => {
		i++;
		console.log(i);
		if (i == timeLimit) {
			clearInterval(timer);
			signupPopup.classList.remove('u-invisible');
		}
	}, 1000);
}
