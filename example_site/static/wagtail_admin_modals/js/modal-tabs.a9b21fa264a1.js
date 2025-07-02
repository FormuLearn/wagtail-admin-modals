// File: static/wagtail_admin_modals/js/modal-tabs.js

document.addEventListener('click', function(event) {
  // look for clicks on any <li> inside a .modal-tabs list
  const tab = event.target.closest('.modal-tabs li');
  if (!tab) return;
  event.preventDefault();

  // find the enclosing modal-content
  const modal = tab.closest('.modal-content');
  if (!modal) return;

  const key = tab.dataset.tab;
  const allTabs  = modal.querySelectorAll('.modal-tabs li');
  const allPanes = modal.querySelectorAll('.modal-tab-pane');

  // toggle active class on tabs
  allTabs.forEach(t => {
    t.classList.toggle('active', t === tab);
  });

  // show the matching pane, hide the rest
  allPanes.forEach(pane => {
    pane.classList.toggle('active', pane.id === 'tab-' + key);
  });
});
