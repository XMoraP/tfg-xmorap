// public/js/chat.js
document.addEventListener('DOMContentLoaded', () => {
  const socket        = io();
  const messagesEl    = document.getElementById('chatMessages');
  const inputEl       = document.getElementById('messageInput');
  const sendBtn       = document.getElementById('sendBtn');
  const sidebarItems  = document.querySelectorAll('.chat-sidebar__item');

  // 1) Leer y aplicar modo desde la URL
  const params = new URLSearchParams(window.location.search);
  const mode   = params.get('mode') || 'llama_prompt_rag';
  window.currentEvent = mode;

  // 2) Destacar en el sidebar el modo activo
  sidebarItems.forEach(item => {
    item.classList.toggle('active', item.dataset.event === mode);
  });

  // 3) Manejador de envío
  function sendMessage() {
    const text = inputEl.value.trim();
    if (!text) return;
    appendMessage(text, 'user');
    inputEl.value = '';
    socket.emit(window.currentEvent, text);
  }

  // 4) Enganchar eventos
  sendBtn.addEventListener('click', sendMessage);
  inputEl.addEventListener('keydown', e => {
    if (e.key === 'Enter') sendMessage();
  });

  // 5) Recibir respuesta del servidor
  socket.on('respuestaServidor', data => {
    appendMessage(data.error ? '⚠ Hubo un error.' : data.message, 'bot');
  });

  // Función auxiliar para renderizar mensajes
  function appendMessage(text, sender) {
    const msgEl = document.createElement('div');
    msgEl.classList.add('message', sender);

    const avatar = document.createElement('img');
    avatar.src = sender === 'user' 
      ? '/images/user.png' 
      : '/images/bot.png';
    avatar.alt = `${sender} avatar`;
    avatar.classList.add('avatar');

    const textEl = document.createElement('div');
    textEl.classList.add('text');
    textEl.textContent = text;

    msgEl.append(avatar, textEl);
    messagesEl.appendChild(msgEl);
    messagesEl.scrollTop = messagesEl.scrollHeight;
  }
});