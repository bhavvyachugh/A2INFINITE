const dropdownHeading = document.querySelector('.dropdownHeading');
const nonDropdownHeading = document.querySelector('.nonDropdownHeading');
const dropdownOl = document.querySelector(
	'.section-topics__list-items__dropdown-list'
);
const dropdownListItem = document.querySelector(
	'.section-topics__list-items--dropdown'
);
const listIcon = document.querySelector(
	'.section-topics__list-items__icon--dropdown'
);

dropdownHeading.addEventListener('mouseover', () => {
	dropdownOl.style.display = 'block';
	dropdownOl.style.opacity = '1';
	nonDropdownHeading.style.height = '19rem';
   listIcon.classList.add('u-rotate-90');
   dropdownOl.style.animation = 'showDropdownMenu 1s forwards'
});

dropdownListItem.addEventListener('mouseleave', () => {
	dropdownOl.style.display = 'none';
	nonDropdownHeading.style.height = 'inherit';
	listIcon.classList.remove('u-rotate-90');
});
