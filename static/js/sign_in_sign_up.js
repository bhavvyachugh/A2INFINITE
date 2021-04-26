const loginBtn = document.querySelector('.btn-nav__login');
const signupBtn = document.querySelector('.btn-nav__signup');

const crossLogin = document.querySelector('.cross-login');
const crossSignup = document.querySelector('.cross-signup');

const loginFormContainer = document.querySelector('.login-form-container');
const signupFormContainer = document.querySelector('.signup-form-container');

const welcomeBtn = document.querySelector('.welcome__btn');
const footerBtn = document.querySelector('.footer__btn');

const formOverlayLinkLogin = document.querySelector(
	'.form-overlay__link-login'
);
const formOverlayLinkSignup = document.querySelector(
	'.form-overlay__link-signup'
);

const alertCross = document.querySelector('.alert__cross');
const alertMessage = document.querySelector('.alert');

function showLoginForm() {
	loginFormContainer.classList.remove('u-invisible');
}

function hideLoginForm() {
	loginFormContainer.classList.add('u-invisible');
}

function showSighupForm() {
	signupFormContainer.classList.remove('u-invisible');
}

function hideSignupForm() {
	signupFormContainer.classList.add('u-invisible');
}

function showHideSignup() {
	loginFormContainer.classList.remove('u-invisible');
	signupFormContainer.classList.add('u-invisible');
}

function showHideLogin() {
	loginFormContainer.classList.add('u-invisible');
	signupFormContainer.classList.remove('u-invisible');
}

function hideAlertMessage() {
	alertMessage.classList.add('u-invisible');
}

loginBtn.addEventListener('click', showLoginForm);
signupBtn.addEventListener('click', showSighupForm);

crossLogin.addEventListener('click', hideLoginForm);
crossSignup.addEventListener('click', hideSignupForm);

welcomeBtn.addEventListener('click', showSighupForm);hideSignupForm
footerBtn.addEventListener('click', showSighupForm);

//formOverlayLinkLogin.addEventListener('click', showHideSignup);
formOverlayLinkSignup.addEventListener('click', showHideLogin);

alertCross.addEventListener('click', hideAlertMessage);
