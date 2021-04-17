const logOutBtn = document.querySelector('.btn-nav__logout');
const logOutForm = document.querySelector('.logout-form-container');
const logoOutNo = document.querySelector('.logout-no');
const alertCross = document.querySelector('.alert__cross');
const alertMessage = document.querySelector('.alert');

function showLogoutForm() {
	logOutForm.classList.remove('u-invisible');
}

function hideLogoutForm() {
	logOutForm.classList.add('u-invisible');
}

function hideAlertMessage() {
	alertMessage.classList.add('u-invisible');
}

logOutBtn.addEventListener('click', showLogoutForm);
logoOutNo.addEventListener('click', hideLogoutForm);
alertCross.addEventListener('click', hideAlertMessage);
