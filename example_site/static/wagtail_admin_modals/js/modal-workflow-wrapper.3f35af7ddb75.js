// File: static/wagtail_admin_modals/js/modal-workflow-wrapper.js

(function() {
  document.addEventListener('click', function(event) {
    // Find any element with a data-modal-name attribute
    var btn = event.target.closest('[data-modal-name]');
    if (!btn) return;
    event.preventDefault();

    // Launch the Wagtail modal workflow
    ModalWorkflow({
      url: btn.href,
      onload: function(modal, jsonData) {
        // If the JSON payload includes 'html', inject it into the modal body
        if (jsonData.html) {
          modal.body.innerHTML = jsonData.html;
        }
      },
      onclose: function() {
        // Restore focus to the triggering element after close
        btn.focus();
      }
    });
  });
})();
