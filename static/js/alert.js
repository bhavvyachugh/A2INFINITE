'use strict';

const alertContainer = document.querySelector('.alert');
const alertCross = document.querySelector('.alert__cross');

alertCross.addEventListener('click', () => {
	alertContainer.style.display = 'none';
});
