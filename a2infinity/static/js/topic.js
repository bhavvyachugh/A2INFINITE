// const dropdownHeading = document.querySelector('.dropdownHeading');
// const nonDropdownHeading = document.querySelector('.nonDropdownHeading');
// const dropdownOl = document.querySelector(
// 	'.section-topics__list-items__dropdown-list'
// );
// const dropdownListItem = document.querySelector(
// 	'.section-topics__list-items--dropdown'
// );
// const listIcon = document.querySelector(
// 	'.section-topics__list-items__icon--dropdown'
// );

// dropdownHeading.addEventListener('mouseover', () => {
// 	dropdownOl.style.display = 'block';
// 	dropdownOl.style.opacity = '1';
// 	nonDropdownHeading.style.height = '19rem';
// 	listIcon.classList.add('u-rotate-90');
// });

// dropdownListItem.addEventListener('mouseleave', () => {
// 	dropdownOl.style.display = 'none';
// 	nonDropdownHeading.style.height = 'inherit';
// 	listIcon.classList.remove('u-rotate-90');
// });

$('.section-topics__list-items--dropdown').mouseenter(function () {
	$(this).children('ol').show();
	$(this).children('ol').css('opacity', '1');
	$(this)
		.children('.section-topics__list-items__icon--dropdown')
		.addClass('u-rotate-90');
});

$('.section-topics__list-items--dropdown').mouseleave(function () {
	$(this).children('ol').hide();
	$(this).children('ol').css('opacity', '0');
	$(this)
		.children('.section-topics__list-items__icon--dropdown')
		.removeClass('u-rotate-90');
});
