//NOTE: load event listener
window.addEventListener('load', () => {
	const deviceHeight = window.innerHeight;
	const bodyHeight = document.body.scrollHeight;

	// base elements
	const body = document.querySelector('.body');
	const footer = document.querySelector('.footer');
	const container = document.querySelector('.container');

	// class view container elements
	const classSection = document.querySelector('.class-section');

	// subject view container elements
	const subjectSection = document.querySelector('.subject-section');
	const subjectContainer = document.getElementsByClassName('subject-container');

	// topic view container elements
	const topicListItems = document.getElementsByClassName('topicList__items');

	// search
	const searchNoResult = document.querySelector('.alert__heading');

	if (bodyHeight < deviceHeight) {
		footer.classList.add('footerHeight');
		body.classList.add('bodyHeight');
		container.classList.add('containerHeight');

		//NOTE: To check if DOM element in variable is present or not
		if (classSection) {
			classSection.classList.add('classSectionHeight');
		} else if (subjectSection) {
			subjectSection.classList.add('subjectSectionHeight');
			//NOTE: For looping over all DOM elements with same class
			for (let i = 0; i < subjectContainer.length; i++) {
				subjectContainer[i].classList.add('subjectContainerHeight');
			}
		} else if (searchNoResult) {
			searchNoResult.classList.add('headingPrimaryHeight');
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
		if (classSection) {
			classSection.classList.remove('classSectionHeight');
		} else if (subjectSection) {
			subjectContainer.classList.remove('subjectContainerHeight');
		} else if (searchNoResult) {
			searchNoResult.classList.remove('headingPrimaryHeight');
		} else if (topicListItems) {
			topicListItems.classList.remove('topicListItemsHeight');
		}
	}
});
