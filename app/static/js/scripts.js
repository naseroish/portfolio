function scrollToElement(id, offset) {
    const element = document.getElementById(id);
    const offsetTop = element.offsetTop - offset;
    window.scrollTo({top: offsetTop, behavior: 'smooth'});
  }