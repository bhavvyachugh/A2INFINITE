'use strict';

const body = document.body;

const settingIcon = document.querySelector('.setting-list__icon');
const dropdownList = document.querySelector('.setting-dropdown');
const navList = document.getElementsByClassName('list__link');
const navListLastElement = navList[navList.length - 1];

settingIcon.addEventListener('click', () => {
	dropdownList.classList.toggle('visible-dropdown');
	navListLastElement.classList.toggle('moveLastChild');

	console.log('click');
});

const closeDropdown = () => {
	navListLastElement.classList.remove('moveLastChild');
	dropdownList.classList.remove('visible-dropdown');
};

body.addEventListener('click', (e) => {
	const settings = e.target.closest('.setting-list__icon');
	if (settings) return;
	if (dropdownList.classList.contains('visible-dropdown')) {
		closeDropdown();
	}
});

document.addEventListener('keydown', (e) => {
	if (
		e.key === 'Escape' &&
		dropdownList.classList.contains('visible-dropdown')
	) {
		closeDropdown();
	}
});
