const deviceHeight = window.innerHeight;
const bodyHeight = document.body.scrollHeight;

const footer = document.querySelector('.footer');

if (bodyHeight < deviceHeight) {
	footer.classList.add('footerHeight');
} else {
	footer.classList.remove('footerHeight');
}
