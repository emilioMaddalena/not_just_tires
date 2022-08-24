// create new elements and assign properties at the same time
// makes writing more compact
const createNewElement = (tag, prop) => Object.assign(document.createElement(tag), prop);
