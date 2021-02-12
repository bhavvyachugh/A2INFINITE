const logOutBtn = document.querySelector('.btn-nav__logout');
const logOutForm = document.querySelector('.logout-form-container');
const logoOutNo = document.querySelector('.logout-no');

function showLogoutForm() {
	logOutForm.classList.remove('u-invisible');
}

function hideLogoutForm() {
	logOutForm.classList.add('u-invisible');
}

logOutBtn.addEventListener('click', showLogoutForm);
logoOutNo.addEventListener('click', hideLogoutForm);
