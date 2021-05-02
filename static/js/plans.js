const details = document.getElementsByClassName('detail-list__detail');

for (let detail of details) {
	if (detail.textContent.includes('None')) detail.style.display = 'none';
}
