const alert = document.querySelector('.alert');
const cross = document.querySelector('.alert__cross');

function hideAlertMessage() {
	alert.classList.add('u-invisible');
}

cross.addEventListener('click', hideAlertMessage);
