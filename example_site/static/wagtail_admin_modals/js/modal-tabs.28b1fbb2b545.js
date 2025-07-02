// static/wagtail_admin_modals/js/modal-tabs.js

document.addEventListener('click', function(event) {
  // Find a tab button
  const btn = event.target.closest('[data-tab-key]');
  if (!btn) return;
  event.preventDefault();

  // Find enclosing modal-content
  const modal = btn.closest('.modal-content');
  if (!modal) return;

  const key = btn.dataset.tabKey;

  // Toggle active class on the tab buttons
  modal
    .querySelectorAll('[data-tab-key]')
    .forEach(el => el.classList.toggle('active', el === btn));

  // Show/hide panes
  modal
    .querySelectorAll('[data-tab-pane]')
    .forEach(pane => pane.classList.toggle('active', pane.dataset.tabPane === key));
});
