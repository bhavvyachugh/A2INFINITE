//NOTE: load event listener
window.addEventListener('load', () => {
	const deviceHeight = window.innerHeight;
	const bodyHeight = document.body.scrollHeight;

	const body = document.querySelector('.body');
	const footer = document.querySelector('.footer');
	const container = document.querySelector('.container');

	//NOTE: subject view container elements
	const subjectSection = document.querySelector('.subject-section');
	const subjectContainer = document.getElementsByClassName('subject-container');

	//NOTE: topic view container elements
	const topicListItems = document.getElementsByClassName('topicList__items');

	if (bodyHeight < deviceHeight) {
		footer.classList.add('footerHeight');
		body.classList.add('bodyHeight');
		container.classList.add('containerHeight');

		//NOTE: To check if DOM element in variable is present or not
		if (subjectSection) {
			subjectSection.classList.add('subjectSectionHeight');

			//NOTE: For looping over all DOM elements with same class
			for (let i = 0; i < subjectContainer.length; i++) {
				subjectContainer[i].classList.add('subjectContainerHeight');
			}
		} else if (topicListItems) {
			//NOTE: For looping over all DOM elements with same class
			for (let i = 0; i < topicListItems.length; i++) {
				topicListItems[i].classList.add('topicListItemsHeight');
			}
		}
	} else {
		footer.classList.remove('footerHeight');
		body.classList.remove('bodyHeight');
		container.classList.remove('containerHeight');

		//NOTE: To check if DOM element in variable is present or not
		if (subjectContainer) {
			subjectContainer.classList.remove('subjectContainerHeight');
		} else if (topicListItems) {
			topicListItems.classList.remove('topicListItemsHeight');
		}
	}
});
