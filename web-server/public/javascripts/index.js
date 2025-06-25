window.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.mode-card').forEach(card => {
      card.addEventListener('click', () => {
        const mode = card.dataset.mode;
        // Redirige al chat con el modo seleccionado en la querystring
        window.location.href = `/chat?mode=${mode}`;
      });
    });
  });
  