document.addEventListener('DOMContentLoaded', function() {
  const currentPath = window.location.pathname;
  const menuItems = document.querySelectorAll('.navbar-item');
  
  menuItems.forEach(item => {
    const href = item.getAttribute('href');
    if (href && (currentPath === href || currentPath.startsWith(href + '/') || (href !== '/' && currentPath.includes(href)))) {
      if (href === '/' && currentPath !== '/') {
        return;
      }
      item.classList.add('is-active');
    }
  });
});
