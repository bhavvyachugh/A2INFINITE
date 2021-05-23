const details = document.getElementsByClassName('detail-list__detail');
const cardSide = document.getElementsByClassName('card__side');

for (let detail of details) {
	if (detail.textContent.includes('None')) detail.style.display = 'none';
}

for (let side of cardSide) {
	if (side.textContent.includes('Subscribed')) {
		side.classList.add('increaseSideHeight');
		side.parentElement.classList.add('increaseCardHeight');
	}
}
