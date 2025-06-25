document.addEventListener('DOMContentLoaded', () => {
  const sidebar = document.getElementById('chatSidebar');
  const wrapper = document.getElementById('chatWrapper');
  const menuToggle = document.getElementById('menuToggle');
  //let currentEvent = 'llama_prompt';

  menuToggle.addEventListener('click', () => {
    sidebar.classList.toggle('open');
    wrapper.classList.toggle('shifted');
  });

  document.querySelectorAll('.chat-sidebar__item').forEach(item => {
    item.addEventListener('click', () => {
      document.querySelectorAll('.chat-sidebar__item')
        .forEach(i => i.classList.remove('active'));
      item.classList.add('active');
      currentEvent = item.dataset.event;
      sidebar.classList.remove('open');
      wrapper.classList.remove('shifted');
      window.currentEvent = currentEvent;
      const messagesEl = document.getElementById('chatMessages');
      if (messagesEl) messagesEl.innerHTML = '';
    });
  });

  window.currentEvent = currentEvent;
});