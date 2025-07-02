// A tiny script to wire up any .wam-tabs on the page
document.addEventListener('click', function(e) {
  let btn = e.target.closest('.wam-tab-button');
  if (!btn) return;

  e.preventDefault();
  let key = btn.dataset.tabKey;
  let root = btn.closest('.wam-tabs');

  // activate clicked button
  root.querySelectorAll('.wam-tab-button').forEach(el => {
    el.classList.toggle('active', el === btn);
  });

  // show/hide panels
  root.querySelectorAll('.wam-tab-panel').forEach(pane => {
    pane.classList.toggle('active', pane.dataset.tabPane === key);
  });
});
