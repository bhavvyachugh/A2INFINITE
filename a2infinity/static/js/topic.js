const dropdownHeading = document.querySelector('.dropdownHeading');
const nonDropdownHeading = document.querySelector('.nonDropdownHeading');
const list = document.querySelector(
	'.section-topics__list-items__dropdown-list'
);

dropdownHeading.addEventListener('mouseover', () => {
	list.style.display = 'block';
	nonDropdownHeading.style.height = '19rem';
});

dropdownHeading.addEventListener('mouseout', () => {
	list.style.display = 'none';
	nonDropdownHeading.style.height = 'inherit';
});
